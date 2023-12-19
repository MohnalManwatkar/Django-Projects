"""
URL configuration for curd_operation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('info', views.add_dataPage, name='info'),
    path('update_data/<id>', views.update_dataPage, name='update_data'),
    path('save_updated_data/<id>', views.save_updated_dataPage, name='save_updated_data'),
    path('delete_data/<id>', views.delete_dataPage, name='delete_data')
]
