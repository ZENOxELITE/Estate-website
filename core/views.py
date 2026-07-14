from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import OperationalError
from .models import TeamMember, FeaturedProject, Testimonial, FAQ
from .forms import ContactForm


def home(request):
    """Home page view"""
    try:
        testimonials = Testimonial.objects.filter(is_active=True)[:3]
    except OperationalError:
        # Database not migrated yet
        testimonials = []
    
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About Us page view"""
    try:
        team_members = TeamMember.objects.filter(is_active=True)
    except OperationalError:
        team_members = []
    
    context = {
        'team_members': team_members,
    }
    return render(request, 'core/about.html', context)


def services(request):
    """Services page view"""
    return render(request, 'core/services.html')


def projects(request):
    """Featured Projects page view"""
    try:
        featured_projects = FeaturedProject.objects.filter(is_featured=True)
    except OperationalError:
        featured_projects = []
    
    context = {
        'projects': featured_projects,
    }
    return render(request, 'core/projects.html', context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            except OperationalError:
                messages.error(request, 'Database not configured. Please run migrations first.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def testimonials(request):
    """Testimonials page view"""
    try:
        all_testimonials = Testimonial.objects.filter(is_active=True)
    except OperationalError:
        all_testimonials = []
    
    context = {
        'testimonials': all_testimonials,
    }
    return render(request, 'core/testimonials.html', context)


def faq(request):
    """FAQ page view"""
    try:
        faqs = FAQ.objects.filter(is_active=True)
    except OperationalError:
        faqs = []
    
    # Group FAQs by category
    faq_categories = {}
    for faq_item in faqs:
        if faq_item.category not in faq_categories:
            faq_categories[faq_item.category] = []
        faq_categories[faq_item.category].append(faq_item)
    
    context = {
        'faq_categories': faq_categories,
    }
    return render(request, 'core/faq.html', context)
