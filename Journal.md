https://github.com/hussain-mustafa990/automax_django_web_app

### VS code Extensions
Django by Robert Solis
Django template by bibhasdn
Material Icon by Philip kief
Django by Baptiste Darthenay


### 1- Create project file
```
mkdir my_project
cd my_project
```

### 2- Create virtaul env named `venv`
```
python -m venv venv
```

### 3- Activate the env
```
source venv/bin/activate
```


### 4- Install django in your virtualenv and check for django sub-commands using the django-admin.
```
python -m pip install django
python -m pip show django
django-admin help
```

### 5- start project inside the project folder
```
django-admin startproject automax
```
- Change the name of the main-level folder of the project from automax to src. i.e the folder that contains subfolders called automax and manage.py

### 6- run the development server
```
python manage.py runserver
```
### NOTE:
- Manage.py file: 
The manage.py file is a utility file that allows us interact with our project via the commandline. from the `src` folder run the `python manage.py --help` command to see a list of commands that can be used to interact with your projects. An example is the command we used to run the development server earlier. Another example is the `python manage.py migrate` that will be used below for migrations.

- Migrations: Django has a built-in ORM i.e object relation mapper. ThIS basically abstracts away the complexity of interacting with a database.The ORM allows us to write python code that can interact with a sql databse on it's own. When we make changes to our code, they need to translated to sql code, that is MIGRATION. 
After these migrations have been done and we have sql code, we need to instruct django to APPLY THESE MIGRATIONS TO THE DATABASE so that the DB has an updated schema and can interact with our application. 

The use the `python manage.py migrate` command to instruct django to apply the migrations.  

### Understanding the Django Project structure
- src: This is the source of everything.
- automax: This reflects the name we gave the project when it was started. This sub-folder is an app within the django app. every other app that we will create during the course of creating the project will be linked to this app. Django projects are generally a composition of smaller sub-apps that come together to form the complete application.

A section/app will be used sorely for authenticating users, another section/app will be used for the views/landing page. All these apps will be attached to the main app i.e the automax app so that it has the ability to authenticate users. But all the logic pertaining to authentication is kept containerized within the  authentication app.

`toggle_full_path`

Class 60: Fixing Minor bugs:
- When user profiles are deleted, the location attached to it should also be deleted. This was fixed

- Adding links to the buttons(i.e login and register) on the main page

- Fix the nav bar on the main page so that when the user is logged in it oly displays Home but, when the user is not logged in it displays Login. (using conditionals in template tags)

Class 62: Implementing Header and Log out feature
- Implemented header and logout button in the nav bar when the user is logged in. (Did this in the template base.html)

- Implemented the logout button to redirect to the main page by adding the logout view and attached it to a url that redirects to the main page 

Class 63: UUID Fields and ForeignKey Relationship
Create the model for the car listing page. i.e the listing model. Implement the UUID field

Relationship between a listing and a seller, the seller in this case is a profile in our application
The relationship is going to be one to many. One listing can have a relationship with one profile, however a profile can have many different listings. A useer van have different listings but a listing can have only one user. This is a one to many relationship. 

This relationship is always placed wherever the one side of this relationshop is. In this case it is placed in the listing and not in the profile that can have many listings.

Class 64: Listing model
Continue defining fields in the listing model started in 64.

Class 65: Adding Listing data.

Class 66: Adding Section Data HomePage
Adding UI components to the homepage

CLass 67: Include Django Template
Implement the car listings showing on the home page. The concept of including templates within templates is implemented.

We take a template with some html within it and inject it into the template we are working in. In this case, the home.html file wants to include some html from another file(listing_car.html in the components folder), one was to do this is by including templates from another template.

CLass 68: Creating the list view

CLass 69: Django Custom Forms
Creating the custom form to list cars. This form is used in the list.html 

CLass 70: Handling Form Data
Adding the post request method to the list_view function for data to be received and handled by the form.

CLass 71: Django Filter:
Add a filter column to the home page to allow filtering the car listing.

CLass 73: Django URL Parameters:
We begin the creation of the view page(listing.html) on the home page in this video and conceptually understand how to link each view button with the corressponding UUID of the listing.

CLass 74: Read Only Fields Django Admin
Added the ID field i.e the UUID of the listing model admin as a readonly field in the admin panel.

CLass 76: URL PARAMETERS DJANGO TEMPLATES
The home page i.e `home.html` includes the `listing_car.html` page which has the view button. 
In this video we will be Linking the view button to the car view page/listing page i.e `listing.html` created in class 71

CLass 77: Displaying Additional Listing Data
In this video we complete the UI of the `listing.html` page

CLass 78: Decorate Class Based Views
In this video , we will create the profile view page.
 we will use a class based view to create the function.
 We created the page and attached it's url to the profile button as well as implemented the login required feature

CLass 79: Displaying Data Within Forms
Finish the profile page, Work on the logic for the 3 forms displayed on the profile page UI


CLass 80: saving data profile page
Still working on the forms. Worked on the POST request i.e  when a user edits his data on his profile via the form and saves it on the server

CLass 81: Django Filter Model QuerySet
In this video we used a django filter framework to add the particular user listings to their profile

CLass 81: Addiing Edit Page

<!-- -->

