from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('about/', views.about, name='about'),
  path('about/', views.aboutus_list, name='about'),
  path('meals/', views.meals_index, name='index'),
  path('meals/<int:meal_id>/', views.meals_detail, name='detail'),
  path('meals/create/', views.MealCreate.as_view(), name='meals_create'),
  path('meals/<int:pk>/update/', views.MealUpdate.as_view(), name='meals_update'),
  path('meals/<int:pk>/delete/', views.MealDelete.as_view(), name='meals_delete'),
  path('reservation/', views.reserve_table, name='reserve_table'),
  path('contact', views.send_email, name='send_email'),
  path('send_success/', views.send_success, name='send_success'),
  path('accounts/signup/', views.signup, name='signup'),
  path('meals/<int:meal_id>/add_photo/', views.add_photo, name='add_photo'),

]