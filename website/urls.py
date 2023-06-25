from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login', views.login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete_record'),
    path('update/<int:pk>', views.update_record, name='update_record'),
    path('add_record', views.add_record, name='add_record'),

]
