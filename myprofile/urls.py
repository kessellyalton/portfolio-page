from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume_view, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('contact/', views.contact, name='contact'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('submit_form_1/', views.submit_form_1, name='submit_form_1'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('download/', views.download_resume, name='download_resume'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('portfolio-details-app/', views.portfolio_details_app, name='portfolio-details-app'),
    path('portfolio-details-web/', views.portfolio_details_web, name='portfolio-details-web'),
    path('portfolio-details-card/', views.portfolio_details_card, name='portfolio-details-card'),

    path('portfolio-details-asc/', views.portfolio_details_asc, name='portfolio-details-asc'),
    path('portfolio-details-esp/', views.portfolio_details_esp, name='portfolio-details-esp'),
    path('portfolio-details-emergency/', views.portfolio_details_emergency, name='portfolio-details-emergency'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('pdfs/', views.pdf_list, name='pdf_list'),
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),


]



