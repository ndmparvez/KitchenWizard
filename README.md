# KitchenWizard

<B>Architecture</B>
![image](https://github.com/ndmparvez/KitchenWizard/assets/71454390/0f6e231c-3364-4455-943b-0eb820780716)

<B>PRE-REQUISITES</B>
To carry on this app you should need:
- Some familiarity with python
- Python installed in the local or cloud enviroinment
- Basic Terminal Commands

Way the project looks after you have cloned it:

![image](https://github.com/ndmparvez/KitchenWizard/assets/71454390/06ec02c6-e28d-4ef5-9b15-be1ee9a5a1a8)

First, start with creating the project directory: 
<br />
```diff
mkdir kitchenWizard  
```
<br />

Next, navigate to the project directory:
<BR />
```diff
cd kitchenWizard  
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
<b>Step 3 — Creating Templates </b>
<br />
Next, create the templates that are used in the app. This is the first step before you can implement the actual login functionality. 
<br />
The app will use three templates: 
 - index.html 
 - recipe-post.html
 - signup.html
 <br />
 

create templates/index.html: 
```diff
nano project/templates/index.html 
```   
This code will create a basic index page with a title and subtitle. 

Next, create templates/recipe-post.html: 
```diff
nano project/templates/recipe-post.html  
```

Next, create templates/signup.html: 
```diff
nano project/templates/signup.html  
```
 	 

<b>Step 4 — Creating static layer </b>
<br />
 the "static" folder is commonly used to store static assets like CSS files. It organizes resources like stylesheets and images separate from dynamic code. This structure aids in managing and deploying assets in web development projects.
<br />

<BR />
Let’s start by creating a static layer directory:
<BR />

```diff
mkdir static
```

<b>Step 5 — Intialize it in Amazon EC2 </b>
<br />
We are hosting our web app through AWS EC2.
To host a Flask web application on Amazon EC2, begin by launching an EC2 instance and connecting to it via SSH. Install necessary software and upload your Flask app code. Install required Python packages, run the Flask app on the instance, and configure the security group to allow incoming traffic on the designated port. Access your app through the public IP address or domain name of the EC2 instance. For a production environment, consider using Gunicorn as a production server, Nginx as a reverse proxy, and ensure proper security practices. Optionally, associate a domain name and implement SSL for secure connections.
<br /> 

<b>MariaDB </b>
<br />
In deploying MariaDB within an AWS cloud application, set up a MariaDB database on Amazon RDS, specifying key parameters through the AWS Management Console, such as version and security configurations. Establish a security group to manage inbound access to the MariaDB instance, ensuring connections from your application server are permitted. Retrieve the MariaDB endpoint and port from the RDS console and configure your application code to connect using these details along with the assigned username and password. Implement database operations in your application code, utilizing SQL queries or an ORM library as needed. For optimal performance, employ AWS CloudWatch for monitoring, and consider scaling options like adjusting instance size or introducing read replicas to meet the evolving needs of your cloud-based application.
<br /> 

<b>Hash based Memory authentication Code </b>
<br />
In securing password authentication for an AWS cloud application, adopt a robust approach by employing a cryptographic hash function like bcrypt or Argon2 during user registration to hash and securely store passwords in your chosen AWS data store such as Amazon RDS or DynamoDB. Implement a secure login process by hashing entered passwords and comparing them to the stored hashes during authentication. Utilize HTTPS to encrypt data in transit, and enforce AWS Identity and Access Management (IAM) for resource access control. Regularly update your system, employ AWS CloudWatch for monitoring, and consider AWS Key Management Service (KMS) for key management. Implementing these measures enhances the overall security posture of your cloud-based application, safeguarding user credentials against potential threats.
<br /> 


 

<b>Step 6 — Run the application </b>
<br />
The FLASK_DEBUG environment variable is enabled. This will enable a debugger that will display application errors in the browser. 
<br /> 
Ensure that you are in the kitchenWizard directory and then run the project: 
```diff
python3 main.py   
```
 
 To run the app, open the dedicated aws site address: Home: 
 ![image](https://github.com/ndmparvez/KitchenWizard/assets/71454390/2601cf8a-1714-4d94-aee4-6136b9f08e27)

 	  
<b>Conclusion </b>
<br />
In conclusion, this project represents a successful implementation of a web application hosted on AWS EC2, utilizing the Flask framework in Python. The application seamlessly integrates with the Spoonacular API, allowing users to search for recipes based on their preferences such as query terms, dietary restrictions, and cuisine types. The AWS infrastructure ensures the scalability and availability of the application, providing a reliable platform for users to access recipe information. The development process included considerations for security, performance, and best practices, showcasing a robust and well-rounded implementation. As a result, this web app serves as an effective and user-friendly tool for exploring and discovering a diverse range of recipes, demonstrating the capabilities of Flask and AWS in building and deploying web applications.

