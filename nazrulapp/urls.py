from django.urls import path
from tawhidapp.views import *

urlpatterns = [
    path('',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('logout/',logoutPage,name='logout'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('doctor/',doctorPage,name='doctor'),
    path('patient/',patientPage,name='patient'),
    path('edit/<int:id>/',editPage,name='edit'),
    path('delete/<int:id>/',deletePage,name='delete'),
]