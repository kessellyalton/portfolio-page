from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import bleach
from django.urls import reverse
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200, default='Untitled')
    author = models.CharField(max_length=100, default='Anonymous')
    content = CKEditor5Field('Content')
    date_posted = models.DateTimeField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional image field

    def save(self, *args, **kwargs):
        self.content = bleach.clean(
            self.content,
            tags=['p', 'strong', 'em', 'a'],
            attributes={'a': ['href', 'title']},
            strip=True
        )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.pk])


class Contact(models.Model):
    name = models.CharField(max_length=100, default='John Doe')
    email = models.EmailField(default='example@example.com')
    subject = models.CharField(max_length=200, default='No Subject')
    message = models.TextField(default='No message')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = models.CharField(max_length=255, blank=True, default='No description provided')
    uploaded_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.file.name


class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
