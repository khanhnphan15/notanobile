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
  path('meals/<int:meal_id>/pair_wine/<int:wine_id>/', views.pair_wine, name='pair_wine'),
  path('meals/<int:meal_id>/unpair_wine/<int:wine_id>/', views.unpair_wine, name='unpair_wine'),

  # path('reservation/', views.reserve_table, name='reserve_table'),
  path('reservations/', views.ReservationsList.as_view(), name='reservations_index'),
  path('reservations/<int:pk>', views.ReservationsDetail.as_view(), name='reservations_detail'),
  path('reservations/create/', views.ReservationsCreate.as_view(), name='reservations_create'),
  path('reservations/<int:pk>/update/', views.ReservationsUpdate.as_view(), name='reservations_update'),
  path('reservations/<int:pk>/delete/', views.ReservationsDelete.as_view(), name='reservations_delete'),
  #path for Wine
  path('wines/', views.WineList.as_view(), name='wine_index'),
  path('wines/<int:pk>', views.WineDetail.as_view(), name='wine_detail'),
  path('wines/create/', views.WineCreate.as_view(), name='wine_create'),
  path('wines/<int:pk>/update/', views.WineUpdate.as_view(), name='wine_update'),
  path('wines/<int:pk>/delete/', views.WineDelete.as_view(), name='wine_delete'),

  path('contact', views.send_email, name='send_email'),
  path('send_success/', views.send_success, name='send_success'),
  path('accounts/signup/', views.signup, name='signup'),
  path('meals/<int:meal_id>/add_photo/', views.add_photo, name='add_photo'),

]