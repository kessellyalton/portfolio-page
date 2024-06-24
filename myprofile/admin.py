from django.contrib import admin
from .models import Blog, Contact, Resume, PDFFile

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    search_fields = ['title', 'author']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['file', 'description', 'uploaded_at']
    search_fields = ['description']

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
