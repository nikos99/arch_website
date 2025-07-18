"""arch_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
   path('', views.home,name="home"),
   path('contact.html', views.contact,name="contact"),
   path('about.html', views.about,name="about"),
   path('index.html', views.index,name="index"),
   path('projects.html', views.projects,name="projects"),
   path('services.html', views.services,name="services"),
   path('studio.html', views.studio,name="studio"),
    path('commercial.html', views.commercial,name="commercial"),

]

