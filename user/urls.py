from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.home, name ='home'),
    path('user_form',views.user_form, name ='user-form'),
    path('update_rec/<int:pk>',views.update_rec, name ='update_rec'),
    path('delete/<int:pk>',views.delete, name ='delete'),
    
]
