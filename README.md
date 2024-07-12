# MedConnect

MedConnect is an online pharmacy web application designed to provide users with a seamless shopping experience for their healthcare needs. The application allows users to browse products, add items to their cart, upload prescriptions, and proceed to checkout, all while maintaining user authentication and security.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Secure user registration, login, and logout functionalities.
- **Product Browsing**: Users can browse a wide range of healthcare products.
- **Shopping Cart**: Users can add products to their cart, adjust quantities, and remove items.
- **Prescription Upload**: Users can upload their prescriptions for verification.
- **Order Summary**: Users can review their cart and see the order summary before checkout.
- **Responsive Design**: The application is fully responsive and works on both desktop and mobile devices.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: SQLite (for development), PostgreSQL (for production)
- **Other Libraries**: Django REST Framework, Pillow (for image handling), etc.

## Installation

To run this project locally, follow these steps:

**Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/medconnect.git
   cd medconnect
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate` 
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   # Open your browser and go to http://127.0.0.1:8000.
   ```

## Project Structure
 ```bash
medconnect/
├── manage.py
├── README.md
├── requirements.txt
├── app/                     # Main application
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── upload_prescription.html
│   │   ├── prescription_list.html
│   │   └── about_us.html
│   └── static/
│       ├── css/
│       │   ├── main.css
│       │   ├── home.css
│       │   ├── cart.css
│       │   ├── checkout.css
│       │   ├── upload_prescription.css
│       │   ├── prescription_list.css
│       │   └── about_us.css
│       └── js/
├── accounts/                # User accounts application
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── product/                 # Product application
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
 ```
