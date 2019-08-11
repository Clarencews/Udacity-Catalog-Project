from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from database_setup import Category, Workout, User, Base

engine = create_engine('sqlite:///wodcatalog.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(name="Clarence Stone", email="clarencews@me.com",
             picture='https://media.licdn.com/dms/image/C5603AQHes9ygs35X1Q/profile-displayphoto-shrink_100_100/0?e=1570060800&v=beta&t=Dyxwou_N_Wbil3v2ZkVB7CgZsrOMQuwUaGlQRHXkBJs')
session.add(user1)
session.commit()

category1 = Category(name="Benchmark Workouts", user_id=1)

session.add(category1)
session.commit()

wod1 = Workout(name="Angie",
                user_id=1,
                description="For Time: \r\n100 pull-ups \r\n100 push-ups 100 sit-ups \r\n100 squats ",
                category=category1)
session.add(wod1)
session.commit()

wod2 = Workout(name="Barbara",
                user_id=1,
                description="5 rounds, each for time of: \r\n20 pull-ups \r\n30 push-ups \r\n40 sit-ups \r\n50 squats \r\nRest precisely 3 minutes between each round. ",
                category=category1)
session.add(wod2)
session.commit()

wod3 = Workout(name="Chelsea",
                user_id=1,
                description="Every minute on the minute for 30 minutes perform:\r\n5 pull-ups \r\n10 push-ups \r\n15 squats ",
                category=category1)
session.add(wod3)
session.commit()

wod4 = Workout(name="Cindy",
                user_id=1,
                description="Complete as many rounds as possible in 20 minutes of: \r\n5 pull-ups \r\n10 push-ups \r\n15 squats ",
                category=category1)
session.add(wod4)
session.commit()

wod5 = Workout(name="Diane",
                user_id=1,
                description="21-15-9 reps for time of: \r\n225-lb. deadlifts \r\nHandstand push-ups ",
                category=category1)
session.add(wod5)
session.commit()

wod6 = Workout(name="Elizabeth",
                user_id=1,
                description="21-15-9 reps for time of: \r\n135-lb. cleans \r\nRing Dips ",
                category=category1)
session.add(wod6)
session.commit()

wod7 = Workout(name="Fran",
                user_id=1,
                description="21-15-9 reps for time of: \r\n95-lb. thurster \r\nPull-ups ",
                category=category1)
session.add(wod7)
session.commit()

wod8 = Workout(name="Grace",
                user_id=1,
                description="135-lb. clean and jerks, 30 reps ",
                category=category1)
session.add(wod8)
session.commit()

category2 = Category(name="New Benchmarks", user_id=1)

session.add(category2)
session.commit()

wod1 = Workout(name="Annie",
                user_id=1,
                description="50-40-30-20-10 reps for time:\r\nDouble-unders\r\nSit-ups ",
                category=category2)
session.add(wod1)
session.commit()

wod2 = Workout(name="Eva",
                user_id=1,
                description="5 rounds, each for time of: \r\nRun 800 meters, 30 reps\r\n30 2-pood kettlebell swings \r\n30 Pull-ups ",
                category=category2)
session.add(wod2)
session.commit()

wod3 = Workout(name="Kelly",
                user_id=1,
                description="5 rounds, each for time of: \r\nRun 400 meters  \r\n30 box jumps, 24-inch box \r\n30 wall-ball shots, 20-lb. ball ",
                category=category2)
session.add(wod3)
session.commit()

wod4 = Workout(name="Lynne",
                user_id=1,
                description="5 rounds for max reps of: \r\nPull-ups \r\nBody-weight bench presses ",
                category=category2)
session.add(wod4)
session.commit()

wod5 = Workout(name="Nicole",
                user_id=1,
                description="Complete as many rounds as possible in 20 minutes of: \r\nRun 400 meters \r\nMax rep pull-ups ",
                category=category2)
session.add(wod5)
session.commit()

wod6 = Workout(name="Amanda",
                user_id=1,
                description="9-7-5 reps for time of: \r\nMuscle-ups \r\n135-lb. squat snatches ",
                category=category2)
session.add(wod6)
session.commit()

wod7 = Workout(name="Gwen",
                user_id=1,
                description="Clean and jerk 15-12-9 reps \r\nTouch and go at floor only. Even a re-grip off the floor is a foul. No dumping. Use same load for each set. Rest as needed between sets. ",
                category=category2)
session.add(wod7)
session.commit()

category3 = Category(name="Hero Workouts", user_id=1)

session.add(wod1)
session.commit()

wod1 = Workout(name="CLOVIS",
                user_id=1,
                description="U.S. Army Second Lieutenant Clovis T. Ray, 34, of San Antonio, Texas, assigned to the 2nd Battalion, 35th Infantry Regiment, 3rd Brigade Combat Team, 25th Infantry Division, based in Schofield Barracks, Hawaii, was killed on March 15, 2012, in Kunar province, Afghanistan, when insurgents attacked his unit with an improvised explosive device.\r\nFor time: \r\n10 Mile Run \r\n150 Burpees ",
                category=category3)
session.add(wod1)
session.commit()

wod2 = Workout(name="DANIEL",
                user_id=1,
                description="U.S. Army Sgt. 1st Class Daniel Crabtree, 31,died in Al Kut, Iraq, on June 8, 2006, when an improvised explosive device detonated during combat operations. \r\nFor time: \r\n50 Pull-Ups \r\n400 Meter Run \r\n21 Thrusters (95#/65#) \r\n800 Meter Run \r\n21 Thrusters (95#/65#) \r\n400 Meter Run \r\n50 Pull-Ups ",
                category=category3)
session.add(wod2)
session.commit()

wod3 = Workout(name="TOMMY V",
                user_id=1,
                description="Senior Chief Petty Officer Thomas J. Valentine, 37, died in a training accident in Arizona, on Feb. 13, 2008. \r\nFor time: \r\n21 Thrusters (115#/85#) \r\n12 Ascents, 15-Foot Rope Climb \r\n15 Thrusters (115#/85#) \r\n9 Ascents, 15-Foot Rope Climb \r\n9 Thrusters (115#/85#) \r\n6 Ascents, 15-Foot Rope Climb ",
                category=category3)
session.add(wod3)
session.commit()

wod4 = Workout(name="ARNIE",
                user_id=1,
                description="Los Angeles County Firefighter Specialist Arnaldo Arnie Quinones, 34, was killed in the line of duty on Sunday, Aug. 30, 2009. \r\nFor Time: \r\n21 Turkish Get-Ups, Right Arm (72#/53#) \r\n50 KB Swing \r\n21 Overhead Squats, Left Arm \r\n50 KB Swing \r\n21 Overhead Squats, Right Arm \r\n50 KB Swing \r\n21Turkish Get-Ups, left Arm (72#/53#) ",
                category=category3)
session.add(wod4)
session.commit()

category4 = Category(name="Crossfit Open", user_id=1)

session.add(category4)
session.commit()

wod1 = Workout(name="OPEN 14.5",
                user_id=1,
                description="21-18-15-12-9-6-3 Reps, For Time\r\nThrusters (95/65 lb) \r\nBar Facing Burpees ",
                category=category4)
session.add(wod1)
session.commit()

wod2 = Workout(name="OPEN 15.5",
                user_id=1,
                description="27-21-15-9 Reps for Time \r\nRow (calories) \r\nThrusters (95/65 lb) ",
                category=category4)
session.add(wod2)
session.commit()

wod3 = Workout(name="OPEN 16.3",
                user_id=1,
                description="AMRAP in 7 minutes \r\n10 Power Snatches (75/55 lb) \r\n3 Bar Muscle-Ups",
                category=category4)
session.add(wod3)
session.commit()

wod4 = Workout(name="OPEN 11.1",
                user_id=1,
                description="AMRAP in 10 minutes \r\n30 Double-unders \r\n15 Power Snatches (75/55 lb)",
                category=category4)
session.add(wod4)
session.commit()

workouts = session.query(Workout).all()
for Workout in workouts:
    print "Workout: " + Workout.name + " Added"

categories = session.query(Category).all()
for Category in categories:
    print "Category: " + Category.name + " Added"
