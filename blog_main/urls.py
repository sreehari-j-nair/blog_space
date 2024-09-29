from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path("admin/", admin.site.urls),
   path("",views.signup),
   path('signup',views.signup,name="signup"),
   path('signin',views.signin,name="signin"),
   path('homepage',views.homepage,name="homepage"),
   path('newpost',views.newpost,name="newpost"),
   path('profile',views.profile,name="profile"),
   path('signout',views.signout,name="signout")
]