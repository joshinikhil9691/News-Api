from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoryView.as_view(), name='news_scrapper')
]