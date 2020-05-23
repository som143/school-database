from django.urls import path
from school import views
urlpatterns = [
    path('registration', views.registration),
    # path('registration', views.registration, name= 'registration'),
    path('signin', views.signin, name= 'signin'),
    path('home/',views.home),
    path('classes/',views.classes, name="classes"),
    path('classes/<classes>',views.classes, name="classes"),
    path('summary',views.summary),
    path('add',views.add),
    path('home_add',views.home_add),
    path('delete/<id>',views.delete),
    # path('add_2',views.add_2),
    # path('add_3',views.add_3),
    # path('classes_2',views.classes_2, name="classes"),
    # path('classes_3',views.classes_3, name= "classes"),
    
]
