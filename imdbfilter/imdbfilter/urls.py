
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imdbapi/', views.MoviesDetailsModelViewSet.as_view()),
]