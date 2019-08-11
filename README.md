# Udacity Project: Item Catalog
An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## How to Run Project

### Set up a Facebook auth application.
1. Go to https://developers.facebook.com/
2. Create a developer account. On the top left drop down, select "Create New App"
3. In left menu add product "facebook login"
4. Copy App ID and paste it into line 71 of login.html as the app id.


## Setup via Vagrant Linux Environment 

1. Follow instructions below from udemy on how to set up a vagrant and virtual box.
```
Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run `vagrant --version`   in your terminal to see the version number.
If Vagrant is successfully installed, you will be able to run vagrant --version
in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.

Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: FSND-Virtual-Machine.zip This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Note: If you are using Windows OS you will find a Time Out error, to fix it use the new Vagrant file configuration to replace you current Vagrant file.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
```

2. SSH into Vagrant using the command `vagrant ssh` then  `cd /vagrant` and navigate into parent folder of this repo.


### Setup the Database 
 
  1. create the database with the categories defined in that "db_setup.py". 
  ```
    $ python database_setup.py
  ```
   2. initial the data of the workouts.
  ```
    $ python workouts.py
  ```

### Start the Server
  After doing all that run the following command:
  ```
    $ python project.py
  ```

### Access the Site
1. Visit 0.0.0.0:8000
2. Log via facebook in order to add, edit, or delete workouts.

### JSON End Points

You can view API endpoints by appending `.json` to the URL. 

- To list all available categories `http://localhost:8000/index.json`
- To see all workouts within a category, visit `http://localhost:8000/catalog/[CategoryID].json`
- To view the details of individual workouts, visit `http://localhost:8000/catalog/[CategoryID]/wod/[WorkoutID].json`
