from django.urls import path
from . import views


urlpatterns = [
  path('', views.Al_emam, name = 'Al emam'),
  path('page1', views.Page1, name = 'page1'),
  path('page2', views.Page2, name = 'page2'),
  path('page3', views.Page3, name = 'page3'),
  path('page4', views.Page4, name = 'page4'),
  path('page5', views.Page5, name = 'page5'),
  path('page6', views.Page6, name = 'page6'),
]