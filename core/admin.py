from django.contrib import admin
from .models import TeamMember, FeaturedProject, Testimonial, ContactMessage, FAQ


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'order', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'position', 'email')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'name')


@admin.register(FeaturedProject)
class FeaturedProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'project_type', 'order', 'is_featured', 'created_at')
    list_filter = ('project_type', 'is_featured', 'created_at')
    search_fields = ('title', 'location', 'description')
    list_editable = ('order', 'is_featured')
    ordering = ('order', '-created_at')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'order', 'is_active', 'created_at')
    list_filter = ('rating', 'is_active', 'created_at')
    search_fields = ('client_name', 'content')
    list_editable = ('order', 'is_active')
    ordering = ('order', '-created_at')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    def has_add_permission(self, request):
        # Prevent adding messages through admin (only through contact form)
        return False


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('question', 'answer')
    list_editable = ('order', 'is_active')
    ordering = ('category', 'order')
