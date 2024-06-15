# django_rest_shop
## Overview
### django_rest_shop is a Django-based e-commerce application that utilizes Django REST Framework for building APIs. This repository includes separate back-end and front-end implementations, making it suitable for developers looking to create a modular and scalable online store.

## Features
- Product Management: Add, edit, and delete products.
- User Authentication: Secure login and registration.
- Cart Management: Add, remove, and update items in the cart.
- Order Processing: Manage orders and transactions.
- API-Driven: Built with Django REST Framework for a robust API.

## Installation
Clone the repository:

`git clone https://github.com/TAnd-dev/django_rest_shop.git`

`cd django_rest_shop`

Navigate to the backend directory:
`cd backend`

Create a virtual environment and activate it:

`python3 -m venv env`

`source env/bin/activate`

Install the dependencies:
`pip install -r requirements.txt`

Apply migrations:
`python manage.py migrate`

Run the development server:
`python manage.py runserver`

Navigate to the frontend directory:
`cd ../frontend`

Install frontend dependencies:
`npm install`

Run the frontend development server:
`npm start`

## Usage
Access the backend API at http://127.0.0.1:8000/api/ and the frontend at http://127.0.0.1:3000/. Use the frontend interface to interact with the e-commerce functionalities, including browsing products, managing the cart, and processing orders.

## Project Structure
- backend/: Contains the Django project and applications.
- frontend/: Contains the React application.
- static/: Static files for the frontend.
- templates/: HTML templates for the backend.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.
