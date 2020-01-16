"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

import service
from app import settings
from custom_flatpages.views import flatpage
from service.views import Home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Home.as_view(), name="home"),
                  path('', include('marque.urls')),
                  path('', include('nouveaute.urls')),
                  path('', include('service.urls')),
                  path('', include('contact.urls')),
                  path('search/', include('haystack.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler500 = service.views.error_500
handler404 = service.views.error_404

urlpatterns.append(path('<path:url>', flatpage, name='flatpage'))
