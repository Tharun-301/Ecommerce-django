from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('', views.dashboard, name='dashboard'),


  path('activate/<uidb64>/<token>/', views.activate, name='activate'),
  path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
  path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
  path('resetPassword/', views.resetPassword, name='resetPassword'),


  #Dasboard
  path('wishlist/', views.wishlist, name='wishlist'),
  path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
  path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
  path('edit_profile/', views.edit_profile, name='edit_profile'),
  path('change_password/', views.change_password, name='change_password'),
]