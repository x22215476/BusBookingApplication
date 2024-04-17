from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),
    path('userlogin/', views.login_user, name="login-user"),
    path('user-register/', views.registerUser, name="register-user"),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.home, name='home-page'),

    path('location/', views.location_mgt, name='location-page'),
    path('manage_location/', views.manage_location, name='manage-location'),
    path('save_location/', views.save_location, name='save-location'),
    path('manage_location/<int:pk>/', views.manage_location, name='manage-location-pk'),
    path('delete_location/', views.delete_location, name='delete-location'),
    path('bus/', views.bus_mgt, name='bus-page'),
    path('manage_bus/', views.manage_bus, name='manage-bus'),
    path('save_bus/', views.save_bus, name='save-bus'),
    path('manage_bus/<int:pk>/', views.manage_bus, name='manage-bus-pk'),
    path('delete_bus/', views.delete_bus, name='delete-bus'),
    path('schedule/', views.schedule_mgt, name='schedule-page'),
    path('manage_schedule/', views.manage_schedule, name='manage-schedule'),
    path('save_schedule/', views.save_schedule, name='save-schedule'),
    path('manage_schedule/<int:pk>/', views.manage_schedule, name='manage-schedule-pk'),
    path('delete_schedule/', views.delete_schedule, name='delete-schedule'),
    path('scheduled_trips/', views.scheduled_trips, name='scheduled-trips-page'),
    path('manage_booking/', views.manage_booking, name='manage-booking'),
    path('manage_booking/<int:schedPK>/', views.manage_booking),
    path('save_booking/', views.save_booking, name='save-book'),
    path('booking/', views.bookings, name='booking-page'),
    path('veiw_booking/<int:pk>/', views.view_booking, name='veiw-booking'),
    path('pay_booked/', views.pay_booked, name='pay-booked'),
    path('delete_booking/', views.delete_booking, name='delete-booking'),
    path('find_trip/', views.find_trip, name='find-trip-page'),
]
