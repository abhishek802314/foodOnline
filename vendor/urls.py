from django.urls import path
from . import views
from accounts import views as AccountViews
urlpatterns = [
    path('', AccountViews.vendorDashboard, name='venderDashboard'),
    path('profile/', views.vprofile, name='vprofile'),
]
