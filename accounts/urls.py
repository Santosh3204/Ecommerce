from django.contrib import admin
from django.urls import path
from .views import Register, Login, logout_user, dropdown, profile, addtocart, addtocart_view, addtocart_inactiveuser, deleteitem, increase_quantity, decrease_quantity, editprofile, update, buynow, handlerequest



urlpatterns = [
   path('register/', Register, name="Register"),
   path('login/', Login, name="Login"),
   path('logout/', logout_user, name="logout"),
   path('dropdown/', dropdown, name="dropdown"),
   path('profile/<int:userid>/', profile, name="profile"),
   path('addtocart/<int:userid>/<int:itemsid>/', addtocart, name="addtocart"),
   path('addtocart/<int:userid>', addtocart_view, name="addtocart_view"),
   path('addtocart_inactiveuser', addtocart_inactiveuser, name="addtocart_inactiveuser"),
   path('deleteitem/<int:itemid>/<int:userid>/', deleteitem, name="deleteitem"),
   path('increase_quantity/<int:itemid>/<int:userid>/', increase_quantity, name="increase_quantity"),
   path('decrease_quantity/<int:itemid>/<int:userid>/', decrease_quantity, name="decrease_quantity"),
   path('editprofile/<int:userid>/', editprofile, name="editprofile"),
   path('update/<int:userid>/', update, name="update"),
   path('buynow/<int:itemid>/<int:userid>/', buynow, name="buynow"),
   path('handlerequest/', handlerequest, name="handlerequest"),
   
]