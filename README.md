# KitchenWizard
![h](https://github.com/ndmparvez/KitchenWizard/assets/71454390/5c01b0c6-bd36-47c8-b7b5-ba82e4b6bb6d)

<B>PRE-REQUISITES</B>
To carry on this app you should need:
- Some familiarity with python
- Python installed in the local or cloud enviroinment
- Basic Terminal Commands

Way the project looks after you have cloned it:

![image](https://github.com/ndmparvez/KitchenWizard/assets/71454390/bbc97ffe-bbf4-44c0-9a93-ec6384c75511)

First, start with creating the project directory: 
<br />
```diff
mkdir kitchenWizard  
```
<br />

Next, navigate to the project directory:
<BR />
```diff
cd cloud_flask_app 
```

You will want to create a Python environment if you don’t have one. 
Depending on how Python was installed on your machine, your command will look like: 
<BR />
```diff
sudo apt-get install python3-venv 
Python3 -m venv nasa 
```
 	
The -m flag is for module-name. This command will execute the module venv to create a new virtual environment named nasa. This will create a new directory containing bin, include, and lib subdirectories. And a pyvenv.cfg file. 
 
Next, run the following command:
<BR />
```diff
source nasa/bin/activate 
```
This command will activate the virtual environment. 
Run the following command from your virtual environment to install the needed packages:
<BR />
```diff
nano requirements.txt  
```
	 
copy paste the contents of requirement.txt files and save. 
<BR />
```diff
pip install -r requirements.txt 
```
 
Now that you have installed the packages, you are ready to create the app. 

<b>Step 1 — Adding Main file</b>
<br />
For the main_blueprint, the main blueprint will be used to run the application. First, create main.py:  
```diff
nano main.py 
```

<b>Step 2 — Adding app file</b>
<br />
This Flask web application defines two routes: one for rendering an 'index.html' template and another for handling recipe search requests. It utilizes the RecipeService class, initialized with a Spoonacular API key, to fetch recipes based on user input (query, diet, cuisine) through a form. The retrieved recipe data is returned in JSON format. The app runs in debug mode when executed directly.  
```diff
nano app.py 
```
<b>Step 4 — Creating Templates </b>
<br />
Next, create the templates that are used in the app. This is the first step before you can implement the actual login functionality. 
<br />
The app will use six templates: 
 - index.html 
 - about.html 
 - blog-post.html 
 - contact.html
 - elements.html
 - recipe-post.html 
 <br />
 

create templates/index.html: 
```diff
nano project/templates/index.html 
```   
This code will create a basic index page with a title and subtitle. 

 
Next, create templates/about.html: 
```diff
nano project/templates/about.html  
```
 
Next, create templates/blog-post.html: 
```diff
nano project/templates/blog-post.html  
```
 
Next, create templates/contact.html: 
```diff
nano project/templates/contact.html  
```

Next, create templates/elements.html: 
```diff
nano project/templates/elements.html  
```

Next, create templates/recipe-post.html: 
```diff
nano project/templates/recipe-post.html  
```
 	 

<b>Step 5 — Creating service layer </b>
<br />
The RecipeService class uses the Spoonacular API to fetch recipes based on specified parameters. The get_recipes_from_api method searches for recipes with a query, diet, and cuisine. The get_recipes_instruction_api method extracts recipe instructions from a given URL. The generate_response method, though unused, aims to return API responses or error messages.
<br />

<BR />
Let’s start by creating a service layer directory:
<BR />
```diff
mkdir service_layer
```

Create the User model: 
```diff
nano project/recipe_service.py 
```
<br />

<b>Step 8 — Amazon EC2 </b>
<br />
We are hosting our web app through AWS EC2.
To host a Flask web application on Amazon EC2, begin by launching an EC2 instance and connecting to it via SSH. Install necessary software and upload your Flask app code. Install required Python packages, run the Flask app on the instance, and configure the security group to allow incoming traffic on the designated port. Access your app through the public IP address or domain name of the EC2 instance. For a production environment, consider using Gunicorn as a production server, Nginx as a reverse proxy, and ensure proper security practices. Optionally, associate a domain name and implement SSL for secure connections.
<br /> 
 

<b>Step 8 — Run the application </b>
<br />
The FLASK_DEBUG environment variable is enabled. This will enable a debugger that will display application errors in the browser. 
<br /> 
Ensure that you are in the kitchenWizard directory and then run the project: 
```diff
python3 main.py   
```
 
 To run the app, open the dedicated aws site address: Home: 
 <p align="center">
  ![image](https://github.com/ndmparvez/KitchenWizard/assets/71454390/2601cf8a-1714-4d94-aee4-6136b9f08e27)
</p> 
 	 
 
<b>Conclusion </b>
<br />
We built a login system for an app using Flask-Login and Flask-SQLAlchemy in this app. By initially constructing a user model and saving the user's information, we have demonstrated how to authenticate a user. Then we had to check that the user's password was correct by hashing it and comparing it to the one saved in the database. Finally, we introduced authorisation to the app by using the @login required decorator on a profile page to restrict access to only logged-in users. 
<br />
For simple apps, the code you wrote in this article will suffice, but if you want more functionality right away, you might consider using the Flask-User or Flask-Security libraries, which are both built on Flask. Finally, we have have demonstrated the use of Nasa APOD API to display picture of the day and randomly generated picture of data by passing a random date to the API. 

