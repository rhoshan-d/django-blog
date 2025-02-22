<img  style="display: block; margin: auto; height: 100px;"  src="documentation/project_images/motordrive_homepage.png"  alt="motordrive logo"/>

</br>

  

# Motordrive vehicle blog:<br>

## The Ultimate Platform for Car Enthusiasts

Welcome to MotorDrive, your dedicated hub for car enthusiasts! Whether you're showcasing your vehicle builds, browsing others’ projects, or simply immersing yourself in the car community, MotorDrive has everything you need. Explore a platform built for gearheads to share, connect, and celebrate everything on four wheels!

  

## Deployed Site:

[Click here to view deployed site on Heroku](https://motordrive-bb11300a48d1.herokuapp.com/)

  

![motordrive Mockup](documentation/project_images/motordrive_mockup.png)

  

## Table of Contents

- [Introduction](#introduction)
- [UX](#ux)
  - [Account Creation and Login](#account-creation-and-login)
  - [Dashboard Overview](#dashboard-overview)
  - [Vehicle Build Management](#vehicle-build-management)
- [Project Planning](#project-planning)
  - [Wireframes](#wireframes)
  - [Database Schema](#database-schema)
- [Models](#models)
- [Agile Methodologies](#agile-methodologies)
  - [Epics](#epics)
  - [User stories](#user-stories)
  - [Kanban board](#kanban-board)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks](#frameworks)
  - [Libraries & Packages](#libraries--packages)
- [Future Features](#future-features)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Heroku](#Heroku-Deployment)
  - [GitHub](#github)
- [Credits](#credits)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

  

## Introduction

Introducing MotorDrive, the ultimate platform for car lovers and gearheads to share their vehicle builds, connect with other enthusiasts, and showcase their automotive passion. From custom mods to classic restorations, MotorDrive provides a space for users to upload pictures, detail their projects, and browse builds from the community. Whether you're just starting a build or already have a finished masterpiece, MotorDrive is your go-to platform.

  

## UX

The user experience of MotorDrive is designed to be straightforward and engaging, offering users an easy way to showcase and manage their vehicle builds, interact with other users, and explore the latest posts from the car community.



### Flowchart

The flowchart below illustrates the user flow and interactions within the MotorDrive application. It provides a visual representation of the steps a user takes to navigate through the application, from the home page to managing vehicle projects.

<p align="center">
  <img src="documentation/project_images/motordrive_flowchart.png" alt="MotorDrive Flowchart" width="75%">
</p>
  

### Account Creation and Login:

<p>

<img  src="documentation/project_images/motordrive_signup_page.png"  width="33%"  alt="Signup view"/>

<img  src="documentation/project_images/motordrive_signin_page.png"  width="33%"  alt="Signin view"/>

<img  src="documentation/project_images/motordrive_signout_page.png"  width="33%"  height="185px"  alt="Signout view"/>

</p>

Users can quickly create an account by entering essential details like name, email, and a password. After signing up, logging in is seamless, and all personal data is securely handled using Django's **allauth** package.

  

### Homepage Overview:

<p>

<img  src="documentation/project_images/motordrive_homepage.png"  width="45%"  alt="Homepage view"/>

</p>

Once logged in, users are welcomed by a clean, user-friendly dashboard. This serves as their central hub to manage their vehicle projects, view their posts, and track any updates from other car enthusiasts. The layout ensures quick navigation and access to important actions like adding or editing vehicle builds.

  

### Vehicle Build Management:

The core functionality of MotorDrive revolves around its ability to allow users to create, edit, and manage their vehicle projects. Users are notified of successful actions such as creating, editing, or deleting posts throughout their experience.

  

-  **Create**: Users can easily upload their vehicles by filling out a detailed form that includes fields for car make, model, year, and a description of the build. Users are required to upload images of their car if creating a post.

<p>

<img  src="documentation/project_images/motordrive_new_post_form.png"  width="45%"  alt="New Vehicle Project Form"/>

</p>

  

- **Read**: All user posts are displayed on the 'Projects' page, where users can explore builds, view vehicle details, and admire uploaded images. Logged in users can like the posts also.

<p>

<img  src="documentation/project_images/motordrive_projects_page.png"  width="45%"  alt="Vehicles Projects Page"/>

</p>

  

-  **Update**: Users can easily edit their posts, changing any details or updating the build progress by modifying the description in the form. The editing process is intuitive, with the form pre-populated with the current data.

<p>

<img  src="documentation/project_images/motordrive_edit_post_form.png"  width="45%"  alt="Edit Vehicle Project Form"/>

</p>

  

- **Delete**: If a user decides to remove a post, they can do so with a simple click. Deleting a post removes it from the 'Projects' page, maintaining a clean and updated vehicle showcase. There is a confirmation prompt before the post is permanently deleted to avoid accidental deletion.

<p>

<img  src="documentation/project_images/motordrive_confirm_delete.png"  width="45%"  alt="Delete Vehicle Project Confirmation"/>

</p>

  

## Project Planning

  

### Wireframes

Created using Wireframe.cc

#### Dashboard Overview

<p>

<img  src="documentation/wireframes/motordrive_home_desktop.png"  height="300px"  alt="desktop home page wireframe"/>

<img  src="documentation/wireframes/motordrive_home_mobile_desktop.png"  height="300px"  alt="mobile wireframe"/>

</p>

  

#### Projects Page

<p>

<img  src="documentation/wireframes/motordrive_projects_page_wireframe.png"  height="300px"  alt="car projects page wireframe"/>

</p>

  

### Database Schema

<img  src="documentation/project_images/motordrive_erd.png"  width="75%"  alt="Database Schema"/>

  

## Models

### User
The User model is based on Django's built-in authentication system, managing essential user information such as username, password, and email. It also allows users to have profiles where their builds are displayed.

### Vehicle
The Vehicle model represents user submitted vehicles. Each vehicle post includes fields for the car's make, model, year, description, images. Users can manage their own vehicle posts, including the option to edit or delete them.

### Build Post
The Build Post model connects user submitted vehicle information with the broader 'Projects' page, where all cars are showcased. It stores relevant data like vehicle details, image links, and build progress.

### Comment
The Comment model allows users to leave comments on articles on the homepage. Each comment is associated with a specific post and includes fields for the author, body, creation date, and approval status. Users can manage their own comments, including the option to edit or delete them.

### Vehicle Project
The Vehicle Project model represents detailed information about user submitted vehicle projects. Each project includes fields for the title, slug, owner, vehicle image, make, model, year, description, creation date, and update date. Users can manage their own vehicle projects, including the option to edit or delete them.

### Project Like
The Project Like model allows users to like vehicle projects. Each like is associated with a specific project and user, and includes a creation date. This model helps track user engagement with vehicle projects.

### About
The About model stores information about the website or project. It includes fields for the title, profile image, content, and update date. This model is used to display the "About" page content.

### Collaborate Request
The Collaborate Request model allows users to submit collaboration requests. Each request includes fields for the name, email, message, and read status. This model helps manage user submitted collaboration requests.

  

## Agile Methodologies

Development of MotorDrive followed agile methodologies, ensuring continuous delivery and integration of user feedback throughout the process.

  

### Epics

The development was split into several epics: User Authentication, Build Post Management, and Vehicle Showcases. Each epic consisted of multiple user stories to help track the progress.

  

### User Stories

- As a user, I can create an account to create, view & like vehicle builds.
- As a user, I can upload images of my vehicle to share with the community.
- As a user, I can delete a build post if I no longer want it displayed on the site.
- As a user, I can browse a page of vehicle projects and view the details of any post.
- As a user, I can like a vehicle project to show my appreciation.
- As a user, I can edit my vehicle build posts to update information or images.
- As a user, I can view other users projects to see their vehicle build.
- As a user, I can submit a collaboration request to share my ideas or projects.
- As a user, I can view the "About" page to learn more about the website.
- As a developer, I can deploy the app to Heroku to make it accessible to users.

  

### Kanban board

[Click here to view Kanban board on Github](https://github.com/users/rhoshan-d/projects/2)

  

## Future Features

- Add a commenting system for users to discuss vehicle builds.

- Implement a search function for users to filter builds by car make or model.

- Allow users to like and share vehicle projects on social media.

  

## Technologies Used

  

### Languages

- HTML

- CSS

- JavaScript

- Python

  

### Frameworks

- Django - Python framework used for development.

- Bootstrap 5 - Used for styling the application.

  

### Libraries & Packages

- Django Allauth - For user authentication
- Crispy Forms - For rendering Django forms  
- Cloudinary - For image hosting and management
- Bootstrap 5 - For responsive frontend design
- Whitenoise - For serving static files

  

### Tools & Programs

- VSCode

- GitHub

- Heroku

- dbdiagram - for database schema creation.

- Balsamiq - for wireframes.

  

## Testing

For full testing results see [TESTING.md](/TESTING.md)

  

## Deployment

  

### Heroku Deployment

Heroku was utilized to deploy the site. Follow these steps to deploy your application:

#### Preparing Your Project

1. Open your terminal within your project environment and create a requirements file by running:
    ```sh
    pip freeze --local > requirements.txt
    ```
2. In the root directory of your project, create a file named `Procfile` (with a capital "P"). Inside this file, add the following line:
    ```plaintext
    web: python run.py
    ```
3. Ensure you are using a database or object storage instead of writing to the local filesystem.

#### Setting Up Heroku

1. Log in to your Heroku account and create a new application.
2. Provide a unique name for your app and complete the necessary setup for your language.
3. Click 'Create App'.
4. Go to the 'Settings' tab and click Reveal Config Vars. Add the required key-value pairs for your configuration settings, making sure not to include `DEBUG`, `DEVELOPMENT`, or `DB_URL`. And make sure to not use quotes around any of the values.
5. Navigate to the 'Deploy' tab and in the 'Deployment method' section, choose 'GitHub'.
6. Search for your repository and click 'Connect'.
7. Optionally, enable 'Automatic Deploys' to automatically deploy changes pushed to GitHub.
8. In the 'Manual Deploy' section, click 'Deploy Branch' to initiate the build process.

#### Finalizing Deployment

1. If you make any changes to your models, you will need to manually run migrations on Heroku.
2. Once the deployment is complete, click the 'Open app' button to view your live application.
3. Note: The deployed application will load, but the new database will be empty, so you will need to add some initial data.

### How to Run This Project Locally

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the environment variables:**
    Create a `.env` file in the root directory and add the necessary environment variables. For example:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=your_database_url
    ```

4. **Apply the migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the project:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

Now you should be able to run the project locally and access it in your web browser.

### GitHub

GitHub was used for version control and project management.

  

## Credits

- [startbootstrap.com](https://startbootstrap.com/) for some initial templates.

- [Unsplash](https://unsplash.com/) for free images used for car builds.

- [dbdiagram.io](https://dbdiagram.io) - Used to generate the database entity relationship diagram (ERD).

- [Am I Responsive](https://ui.dev/amiresponsive) - Used to create responsive design mockups across different device viewports.

  

### Acknowledgements

- Code Institute
- ChatGTP for wording
- YouTube, Google, and Stack Overflow for various tutorials and solutions.