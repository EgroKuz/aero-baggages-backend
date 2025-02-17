"""
URL configuration for rip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from baggage_registration import views
from rip import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baggages/', views.baggages, name='baggages'),
    path('baggage/<int:baggage_id>/', views.baggage, name='baggage'),
    path('migration/<int:migration_id>/', views.migration, name='migration')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)