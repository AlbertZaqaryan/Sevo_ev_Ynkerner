from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('prod/<int:id>/', views.index_detail, name='index_detail'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('change/<int:id>/', views.prod, name='prod'),
    path('contact-us/', views.contact, name='contact'),
]