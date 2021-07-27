# rankme
A django application that can help you track the quality of your projects by having other developers rank your posted projects. The projects are rated based on their usability, content and Design

##  Live Link 
To view the site, click [here](https://rankme254.herokuapp.com/)

## Admin Dashboard credentials
username : u57464
password :admin2020
## Screenshots 
###### Home page
<img src= "https://user-images.githubusercontent.com/51013354/127123660-0aa29934-aed4-4452-893a-56b3eb1304c5.png" >

## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## Setup and Installation  
To get the project follow these steps:

##### Cloning the repository:  
 ```bash 
https://github.com/ThiraTheNerd/rankme.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd rankme 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
``` 
 ##### Setup Database
 Create a .env file and fill in the configurations for your database and application.
 python manage.py makemigrations projects
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  

  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug
## Contact Information   
If you have any question or contributions, please email me at [thiragithinji@gmail.com] 

## License 
* Copyright (c) 2021 **ThiraTheNerd**
