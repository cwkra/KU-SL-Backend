"""
URL configuration for kusl_backend project.

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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

api_url = [
    path('auth/', include('authentication.urls')),
    path('event/', include('event.urls')),
    path('announcement/', include('announcement.urls')),
    path('qualification-question/', include('qualification_question.urls')),
    path('student-loan-request-record/', include('student_loan_request_record.urls')),
    path('volunteer-activities-hours-record/', include('volunteer_activities_hours_record.urls')),
    path('notification/', include('notification.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(api_url)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
