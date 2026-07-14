# Estate Agency Website - Complete Documentation Guide

## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Updating Content](#updating-content)
4. [Managing Database Models](#managing-database-models)
5. [Customizing Design & Styling](#customizing-design--styling)
6. [Adding/Removing Pages](#addingremoving-pages)
7. [Form Modifications](#form-modifications)
8. [Admin Panel Guide](#admin-panel-guide)
9. [SEO Optimization](#seo-optimization)
10. [Deployment Guide](#deployment-guide)
11. [Troubleshooting](#troubleshooting)

---

## Project Structure

```
estate_agency/
├── estate_agency/          # Main project folder
│   ├── settings.py         # Project settings & configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── core/                   # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL routing
│   ├── forms.py           # Form definitions
│   └── admin.py           # Admin panel configuration
├── templates/              # HTML templates
│   ├── base.html          # Base template (used by all pages)
│   ├── components/        # Reusable components
│   │   ├── navbar.html
│   │   └── footer.html
│   └── core/              # Page templates
│       ├── home.html
│       ├── about.html
│       ├── services.html
│       ├── projects.html
│       ├── contact.html
│       ├── testimonials.html
│       └── faq.html
└── static/                 # Static files (CSS, JS, images)
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

---

## Getting Started

### Initial Setup

1. **Install Python** (3.8 or higher)
2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create Admin User:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access Website:** http://localhost:8000
8. **Access Admin Panel:** http://localhost:8000/admin

---

## Updating Content

### 1. Changing Static Text Content

**Home Page (templates/core/home.html):**

```html
<!-- Change hero title -->
<h1 class="display-3 fw-bold mb-4">Your Dream Home Awaits</h1>

<!-- Change hero tagline -->
<p class="lead mb-5">Expert real estate services...</p>

<!-- Change statistics -->
<div class="col-md-3 col-6">
  <div class="stat-number">500+</div>
  <div class="stat-label">Properties Sold</div>
</div>
```

**About Page (templates/core/about.html):**

```html
<!-- Update mission statement -->
<div class="col-lg-6">
  <h3 class="section-subtitle">Our Mission</h3>
  <p>Your custom mission text here...</p>
</div>
```

### 2. Updating WhatsApp Number

**Search and replace** `+1234567890` with your actual number in:
- `templates/components/navbar.html`
- `templates/components/footer.html`
- `templates/core/home.html`
- `templates/core/contact.html`

```html
<!-- Example -->
<a href="https://wa.me/YOUR_NUMBER" class="btn btn-success">
  <i class="bi bi-whatsapp"></i> WhatsApp
</a>
```

### 3. Updating Contact Information

**Footer (templates/components/footer.html):**

```html
<p><i class="bi bi-geo-alt"></i> 123 Main Street, City, State 12345</p>
<p><i class="bi bi-telephone"></i> +1 (234) 567-8900</p>
<p><i class="bi bi-envelope"></i> info@estateagency.com</p>
```

**Contact Page (templates/core/contact.html):**

```html
<!-- Update office details -->
<h5><i class="bi bi-geo-alt-fill text-primary"></i> Office Address</h5>
<p>123 Main Street<br>City, State 12345</p>
```

### 4. Updating Google Maps Embed

In `templates/core/contact.html`, replace the iframe src:

```html
<iframe 
  src="https://www.google.com/maps/embed?pb=YOUR_EMBED_CODE"
  width="100%" 
  height="400" 
  style="border:0;" 
  allowfullscreen="" 
  loading="lazy">
</iframe>
```

**How to get your embed code:**
1. Go to Google Maps
2. Search your address
3. Click "Share" → "Embed a map"
4. Copy the iframe src URL

### 5. Updating Social Media Links

**Footer (templates/components/footer.html):**

```html
<div class="social-links">
  <a href="https://facebook.com/yourpage"><i class="bi bi-facebook"></i></a>
  <a href="https://twitter.com/yourhandle"><i class="bi bi-twitter"></i></a>
  <a href="https://instagram.com/yourprofile"><i class="bi bi-instagram"></i></a>
  <a href="https://linkedin.com/company/yourcompany"><i class="bi bi-linkedin"></i></a>
</div>
```

---

## Managing Database Models

### Adding New Fields to Models

**Example: Adding phone number to TeamMember**

1. **Edit core/models.py:**

```python
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)  # NEW FIELD
    email = models.EmailField(blank=True)  # NEW FIELD
    order = models.IntegerField(default=0)
```

2. **Create and run migration:**

```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Update admin.py if needed:**

```python
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone', 'email', 'order')
    list_editable = ('order',)
```

### Deleting a Model

1. **Remove from core/models.py**
2. **Remove from core/admin.py**
3. **Create migration:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Creating a New Model

**Example: Adding a Blog model**

1. **Add to core/models.py:**

```python
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
```

2. **Register in core/admin.py:**

```python
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    list_filter = ('published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
```

3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## Customizing Design & Styling

### Changing Colors

**Edit static/css/style.css:**

```css
:root {
    /* Primary brand color */
    --primary-color: #2c5f7f;  /* Change this */
    
    /* Accent color */
    --accent-color: #d4a574;   /* Change this */
    
    /* Dark colors */
    --dark-color: #1a1a1a;
    
    /* Light colors */
    --light-bg: #f8f9fa;
}
```

### Changing Fonts

**Edit templates/base.html:**

```html
<!-- In the <head> section, add Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
```

**Edit static/css/style.css:**

```css
:root {
    --heading-font: 'Playfair Display', serif;
    --body-font: 'Poppins', sans-serif;
}

body {
    font-family: var(--body-font);
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--heading-font);
}
```

### Modifying Layout & Spacing

**Change container width in style.css:**

```css
.container {
    max-width: 1200px; /* Change this value */
}
```

**Change section padding:**

```css
.section-padding {
    padding: 80px 0; /* Change these values */
}
```

### Adding Custom CSS

**In static/css/style.css, add your custom styles at the bottom:**

```css
/* Custom Styles */
.my-custom-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 12px 30px;
    border-radius: 8px;
}
```

---

## Adding/Removing Pages

### Adding a New Page

**Step 1: Create View (core/views.py):**

```python
def blog(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'core/blog.html', {'posts': posts})
```

**Step 2: Add URL (core/urls.py):**

```python
urlpatterns = [
    # ... existing urls ...
    path('blog/', views.blog, name='blog'),
]
```

**Step 3: Create Template (templates/core/blog.html):**

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Blog - Estate Agency{% endblock %}

{% block content %}
<div class="page-header">
    <div class="container">
        <h1>Our Blog</h1>
        <p>Latest news and insights</p>
    </div>
</div>

<section class="section-padding">
    <div class="container">
        <div class="row">
            {% for post in posts %}
            <div class="col-md-4 mb-4">
                <div class="blog-card">
                    <img src="{{ post.image.url }}" alt="{{ post.title }}">
                    <h3>{{ post.title }}</h3>
                    <p>{{ post.content|truncatewords:30 }}</p>
                    <a href="{% url 'blog_detail' post.slug %}">Read More</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
```

**Step 4: Add to Navigation (templates/components/navbar.html):**

```html
<li class="nav-item">
    <a class="nav-link" href="{% url 'blog' %}">Blog</a>
</li>
```

### Removing a Page

1. **Remove URL from core/urls.py**
2. **Remove view from core/views.py**
3. **Delete template file**
4. **Remove navigation link from navbar.html**

---

## Form Modifications

### Changing Contact Form Fields

**Edit core/forms.py:**

```python
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        # Add or remove fields here
        
    # Add custom field
    preferred_contact = forms.ChoiceField(
        choices=[('email', 'Email'), ('phone', 'Phone')],
        widget=forms.RadioSelect
    )
```

**Update core/models.py:**

```python
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    preferred_contact = models.CharField(max_length=10, blank=True)  # NEW
    created_at = models.DateTimeField(auto_now_add=True)
```

**Run migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

### Adding Form Validation

**In core/forms.py:**

```python
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            raise forms.ValidationError('Please enter a valid phone number')
        return phone
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError('Message must be at least 10 characters')
        return message
```

### Email Notifications on Form Submission

**Edit core/views.py:**

```python
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification
            send_mail(
                subject=f'New Contact: {contact_message.subject}',
                message=f'From: {contact_message.name}\nEmail: {contact_message.email}\n\n{contact_message.message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['your-email@example.com'],
                fail_silently=False,
            )
            
            messages.success(request, 'Thank you! We will contact you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})
```

**Add to settings.py:**

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

---

## Admin Panel Guide

### Accessing Admin Panel

1. Go to http://localhost:8000/admin
2. Login with superuser credentials
3. You'll see all registered models

### Customizing Admin Display

**Edit core/admin.py:**

```python
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    # What columns to show in list view
    list_display = ('name', 'position', 'order')
    
    # Which fields can be edited directly in list view
    list_editable = ('order',)
    
    # Add filters in sidebar
    list_filter = ('position',)
    
    # Add search functionality
    search_fields = ('name', 'position', 'bio')
    
    # Organize fields in edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'image')
        }),
        ('Details', {
            'fields': ('bio', 'order')
        }),
    )
```

### Adding Bulk Actions

```python
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_featured', 'created_at')
    actions = ['mark_as_featured', 'unmark_as_featured']
    
    def mark_as_featured(self, request, queryset):
        queryset.update(is_featured=True)
        self.message_user(request, 'Selected testimonials marked as featured')
    mark_as_featured.short_description = 'Mark as featured'
    
    def unmark_as_featured(self, request, queryset):
        queryset.update(is_featured=False)
        self.message_user(request, 'Selected testimonials unmarked')
    unmark_as_featured.short_description = 'Remove featured status'
```

### Creating a Custom Admin Dashboard

**Create core/admin_views.py:**

```python
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    from .models import ContactMessage, TeamMember, Testimonial
    
    context = {
        'total_messages': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(read=False).count(),
        'team_members': TeamMember.objects.count(),
        'testimonials': Testimonial.objects.count(),
    }
    return render(request, 'admin/dashboard.html', context)
```

---

## SEO Optimization

### Page-Specific Meta Tags

**Edit each page template:**

```html
{% block title %}Custom Page Title - Estate Agency{% endblock %}

{% block meta %}
<meta name="description" content="Custom page description here">
<meta name="keywords" content="real estate, property, buying, selling">
<meta property="og:title" content="Custom Page Title">
<meta property="og:description" content="Custom page description">
<meta property="og:image" content="{% static 'images/og-image.jpg' %}">
{% endblock %}
```

### Adding Structured Data

**In base.html, add JSON-LD:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Estate Agency",
  "image": "{% static 'images/logo.png' %}",
  "telephone": "+1-234-567-8900",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  }
}
</script>
```

### Creating Sitemap

**Install django sitemap:**

```bash
pip install django-contrib-sitemaps
```

**Add to settings.py:**

```python
INSTALLED_APPS = [
    # ... existing apps ...
    'django.contrib.sitemaps',
]
```

**Create core/sitemaps.py:**

```python
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'services', 'projects', 'contact', 'testimonials', 'faq']

    def location(self, item):
        return reverse(item)
```

**Update estate_agency/urls.py:**

```python
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # ... existing patterns ...
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
```

---

## Deployment Guide

### Preparing for Production

**1. Update settings.py:**

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
```

**2. Collect static files:**

```bash
python manage.py collectstatic
```

**3. Create requirements.txt:**

```bash
pip freeze > requirements.txt
```

### Deployment to Heroku

**1. Install Heroku CLI and login:**

```bash
heroku login
```

**2. Create Procfile:**

```
web: gunicorn estate_agency.wsgi
```

**3. Install gunicorn:**

```bash
pip install gunicorn
pip freeze > requirements.txt
```

**4. Create heroku app:**

```bash
heroku create your-app-name
```

**5. Set environment variables:**

```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
```

**6. Deploy:**

```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

**7. Run migrations:**

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Deployment to Digital Ocean/VPS

**1. Install dependencies on server:**

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

**2. Clone your repository**

**3. Set up virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**4. Configure Gunicorn:**

```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 estate_agency.wsgi
```

**5. Set up Nginx as reverse proxy**

**6. Configure SSL with Let's Encrypt**

---

## Troubleshooting

### Common Issues & Solutions

**1. Static files not loading**

```bash
python manage.py collectstatic
```

Make sure `STATIC_ROOT` is set in settings.py

**2. Database migrations error**

```bash
# Reset migrations (WARNING: Loses data)
python manage.py migrate --fake core zero
python manage.py migrate core
```

**3. Admin CSS not loading**

Run `python manage.py collectstatic` and check `STATIC_URL` in settings.py

**4. Image uploads not working**

Check `MEDIA_ROOT` and `MEDIA_URL` in settings.py. Ensure directory exists and has write permissions.

**5. Form not submitting**

Check CSRF token in template:
```html
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

**6. Port already in use**

```bash
# Kill process on port 8000
# Mac/Linux:
lsof -ti:8000 | xargs kill -9

# Windows:
netstat -ano | findstr :8000
taskkill /PID [PID_NUMBER] /F
```

**7. Template not found error**

Check `TEMPLATES` setting in settings.py. Ensure `'DIRS': [BASE_DIR / 'templates']` is set.

**8. Module not found error**

```bash
pip install -r requirements.txt
```

Make sure virtual environment is activated.

---

## Quick Reference Commands

```bash
# Start development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Django shell
python manage.py shell

# Check for issues
python manage.py check

# Run tests
python manage.py test

# Create app backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```

---

## Support & Resources

- **Django Documentation:** https://docs.djangoproject.com/
- **Bootstrap 5 Docs:** https://getbootstrap.com/docs/5.3/
- **Bootstrap Icons:** https://icons.getbootstrap.com/

---

**Last Updated:** [Current Date]
**Version:** 1.0
