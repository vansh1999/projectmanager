## Project Manager

Project Manager is a simple task management application built using Django. It provides CRUD (Create, Read, Update, Delete) functionality to manage tasks. The UI allows users to add tasks, edit them, and delete tasks easily, all from a single page interface.

### Project Structure

``` 
projectmanager/
│
├── projectmanager/         # Main project settings and URL configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL dispatcher
│   
│
├── tasks/                  # Main app folder
│   ├── migrations/         # Migrations files for database changes
│   ├── models.py           # Task model
│   ├── views.py            # Views handling the logic for task management
│   ├── forms.py            # Forms for task creation and editing
│   ├── urls.py             # URL routing for tasks app
│   ├── templates/          # Templates for the app
│       ├── index.html      # Main page to add and display tasks
│       ├── edit_task.html  # Page to edit a specific task
│   
│
├── env/                    # Virtual environment directory
├── manage.py               # Django’s management script
└── README.md               # Project documentation (this file)

```

### Screenshots

![Screenshot 2024-10-05 at 2 59 46 PM](https://github.com/user-attachments/assets/2f13573e-0a24-4fc3-b794-8a84d4e5a02a)

![Screenshot 2024-10-05 at 3 02 49 PM](https://github.com/user-attachments/assets/c9d5c13a-ee54-4b4d-bb5d-52bb0882ce22)

### Setup Instructions

1. Clone the Repository

```$ git clone https://github.com/vansh1999/projectmanager.git ```

``` $ cd projectmanager ```

2. Create and Activate Virtual Environment

``` $ python3 -m venv env ```

``` $ source env/bin/activate ```

3. Run the Application

``` $ python manage.py runserver ```

Open your web browser and go to http://127.0.0.1:8000/ to view the app.














