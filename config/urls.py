"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from generator.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services', TemplateView.as_view(template_name='services.html'), name='services'),
    path('teams', TemplateView.as_view(template_name='teams.html'), name='teams'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('dashboard', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('get_started', TemplateView.as_view(template_name='get_started.html'), name='get_started'),
    path('faq', TemplateView.as_view(template_name='faq.html'), name='faq'),
    #  generation 
    # upload excel file
    path('upload', upload, name='upload'),
    # list uploads
    path('list', list_files, name='list'),
    # view file data
    path('view/<int:id>', view_file, name='view'),
    # delete upload
    path('delete/<int:id>', delete_file, name='delete'),
    # generate certificate
    path('generate/<int:dataid>', generate_certificate, name='generate'),
    # list certificates
    path('list_cert', list_certificates, name='list_cert'),
    # download certificate
    path('download/<int:id>', download_certificate, name='download'),
    # view certificate
    path('view_cert/<int:id>', view_certificate, name='view_cert'),
    # delete certificate
    path('delete_cert/<int:id>', delete_certificate, name='delete_cert'),
    # report changes
    path('report', report_changes, name='report'),
    # list reports
    path('list_reports', list_reports, name='list_reports'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
