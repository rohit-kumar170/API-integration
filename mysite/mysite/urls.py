from django.contrib import admin
from django.urls import path,include
from Test import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("google_sso/", include("django_google_sso.urls", namespace="django_google_sso")),
    path('',views.index,name='index'),
    path('auth/',include('users.urls')),
]
