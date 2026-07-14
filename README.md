# Estate Agency Website

A modern, professional estate agency website built with Django.

## Features

- Home page with hero banner and services preview
- About Us page with team information
- Services page with detailed service cards
- Featured Projects showcase
- Contact page with working form and Google Maps integration
- Testimonials page
- FAQ page
- Responsive design with Bootstrap 5
- Django admin panel for content management

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ to view the website
7. Visit http://127.0.0.1:8000/admin/ to access the admin panel

## Admin Panel

The admin panel allows you to manage:
- Team members
- Featured projects
- Testimonials
- Contact messages
- FAQs

## Customization

- Update the company information in templates
- Add your Google Maps embed code in the contact page
- Customize colors and styling in static/css/custom.css
- Update WhatsApp number in templates
