# Django Cooking Application

This Django project is a cooking application that allows users to browse recipes and categories, view recipe details, and manage recipe data.

## Features

- Display all recipes with their ingredients and categories.
- View details of each recipe, including ingredients and associated categories.
- Browse recipes by category.
- API endpoints to retrieve recipe and category data.

## Setup

1. *Clone the repository:*

    bash
    git clone https://github.com/your_username/django-cooking-app.git
    

2. *Install dependencies:*

    bash
    pip install -r requirements.txt
    

3. *Apply database migrations:*

    bash
    python manage.py migrate
    

4. *Populate the database with sample data:*

    bash
    python utils/populate_data.py
    

## Usage

1. *Run the development server:*

    bash
    python manage.py runserver
    

2. *Access the application:*

    Open your web browser and go to [http://localhost:8000](http://localhost:8000) to view the application.
