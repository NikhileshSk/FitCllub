
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("login/",views.login_view,name='login'),
    path("logout/",views.LogoutView.as_view(),name='logout'),
    path("signup/",views.signup,name='signup'),
    path("dashboard",views.dashboard,name='dashboard'),
    path('exercise/', views.exercise_view, name='exercise'),
    path('mark_completed/<str:module_id>/', views.mark_as_completed, name='mark_as_completed'),
    path('update', views.update_view, name='update'),
    path('counter',views.counter,name='counter'),
]
