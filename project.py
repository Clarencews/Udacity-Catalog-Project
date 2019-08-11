from flask import (Flask, render_template, url_for, request, redirect, jsonify, make_response, flash)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Workout, User
from flask import session as login_session
import random
import string
import json
import httplib2
import requests
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

app = Flask(__name__)

# Connect to Database
engine = create_engine('sqlite:///wodcatalog.db?check_same_thread=False')
Base.metadata.bind = engine

# Create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# User Helper Functions


def createUser(login_session):
    newUser = User(
        name=login_session['username'],
        email=login_session['email'],
        picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except BaseException:
        return None


@app.route('/')
@app.route('/home')
@app.route('/index.json', endpoint="index-json")
def home():

    categories = session.query(Category).all()

    workouts = session.query(Workout).order_by(Workout.id.desc()).all()

    if request.path.endswith('.json'):
        return jsonify(json_list = [category.serialize for category in categories])

    if 'username' not in login_session:
        return render_template('publicIndex.html',
            categories=categories,
            workouts=workouts)
    else:
        return render_template(
            'index.html',
            categories=categories,
            workouts=workouts)

# show workouts by category
@app.route('/catalog/<int:cat_id>')
@app.route('/catalog/<int:cat_id>.json', endpoint="category-json")
def showCategory(cat_id):
    categories = session.query(Category).all()

    # Get name of category
    category = session.query(Category).filter_by(id=cat_id).first()
    categoryName = category.name

    # Get all workouts of a specific category
    workouts = session.query(Workout).filter_by(category_id=cat_id).all()

    # Get count of category's wrokouts
    workoutsCount = session.query(Workout).filter_by(category_id=cat_id).count()

    if request.path.endswith('.json'):
        return jsonify(json_list = [workout.serialize for workout in workouts])

    return render_template(
        'category.html',
        categories=categories,
        workouts=workouts,
        categoryName=categoryName,
        workoutsCount=workoutsCount)


@app.route('/catalog/<int:cat_id>/wod/<int:wod_id>')
@app.route('/catalog/<int:cat_id>/wod/<int:wod_id>.json', endpoint="workout-json")
def showWorkout(cat_id, wod_id):
    # Get category character
    workout = session.query(Workout).filter_by(id=wod_id).first()
    # Get creator of character
    creator = getUserInfo(Workout.user_id)

    if request.path.endswith('.json'):
        return jsonify(workout = [workout.serialize])

    if 'username' not in login_session:
        return render_template('publicWod.html',
                               workout=workout,
                               creator=creator)
    else:
        return render_template('wod.html',
           workout=workout,
           creator=creator)


@app.route('/catalog/add', methods=['GET', 'POST'])
def addWorkout():
    # Check if user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':

        if not request.form['name']:
            flash('Please name your workout!')
            return redirect(url_for('addWorkout'))

        if not request.form['description']:
            flash('Please add workout details!')
            return redirect(url_for('addWorkout'))

        newWorkout = Workout(
            name=request.form['name'],
            description=request.form['description'],
            category_id=request.form['category'],
            user_id=login_session['user_id'])
        session.add(newWorkout)
        session.commit()
        return redirect(url_for('home'))
    else:
        # Get all categories
        categories = session.query(Category).all()
        return render_template('addwod.html', categories=categories)


@app.route(
    '/catalog/<int:cat_id>/wod/<int:wod_id>/edit',
    methods=[
        'GET',
        'POST'])
def editWorkout(cat_id, wod_id):
    # Check if user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # Get category of workout
    workout = session.query(Workout).filter_by(id=wod_id).first()
    # Get creator of workout
    creator = getUserInfo(Workout.user_id)
    # Session query for edited character content
    editedWod = session.query(Workout).filter_by(id=wod_id).first()
    # Check if logged in user is creator of category character
    # if creator.id != login_session['user_id']:
    #     return redirect(url_for('home'))
    # Get all categories 
    categories = session.query(Category).all()
    if request.method == 'POST':
        if request.form['name']:
            editedWod.name = request.form['name']
        if request.form['description']:
            editedWod.description = request.form['description']
        if request.form['category']:
            editedWod.category_id = request.form['category']
        session.add(editedWod)
        session.commit()
        return redirect(
            url_for('home'))
    else:
        return render_template(
            'editWod.html',
            categories=categories,
            workout=workout, wod=editedWod)


@app.route(
    '/catalog/<int:cat_id>/cat/<int:wod_id>/delete',
    methods=[
        'GET',
        'POST'])
def deleteWorkout(cat_id, wod_id):
    # Check if user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # Get category workout
    workout = session.query(Workout).filter_by(id=wod_id).first()
    # Get creator of workout
    creator = getUserInfo(Workout.user_id)

    if request.method == 'POST':
        session.delete(workout)
        session.commit()
        return redirect(
            url_for('home'))
    else:
        return render_template('deleteWod.html', workout=workout)


@app.route('/login')
def login():
    # Create anti-forgery state token
    state = ''.join(
        random.choice(
            string.ascii_uppercase +
            string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/logout')
def logout():
    fbdisconnect()
    del login_session['facebook_id']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['provider']

    return redirect(url_for('home'))


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    userinfo_url = "https://graph.facebook.com/me"

    url = '%s?access_token=%s&fields=name,id,email,picture' % (userinfo_url, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]
    login_session['access_token'] = access_token
    login_session['picture'] = data["picture"]["data"]["url"]
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (
        facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=8000)
