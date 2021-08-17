from django.urls import path,include
from . import views



urlpatterns = [
  path('', views.home, name='home'),
  path("accounts/", include("django.contrib.auth.urls"),name="login"),
  path('result/', views.result, name='result'),
  path("students/list", views.PlacementList.as_view(), name="placementlist"),
  path("students/create",views.PlacementCreate.as_view(),name="studentcreate"),
  path("logout/", views.logout_view, name="logout"),
  path("signup/", views.SignUp.as_view(), name="signup"),
]

