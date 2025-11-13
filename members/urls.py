from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='home'), # remember this is our main location whenver we run our website
    path('members/', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
    path('testing/',views.testing, name= 'testing'),
]

