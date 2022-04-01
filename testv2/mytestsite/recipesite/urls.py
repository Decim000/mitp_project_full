
from django.urls import path, include
#from .views import LoginUser
from . import views


urlpatterns = [
    path ('profile/', views.index),
    path('recipe/<int:pk>/', views.recipe, name='recipe'),
    #path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    #path('favs/', views.fav),
    #path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('favs/', views.add_to_wishlist),
    path('login/', views.LoginView.as_view(), name='login'),
    path('saved_recipe/<int:pk>/', views.recipe_showsaved, name='saved_recipe'),
    path('saved_recipe/<int:pk>/edit/', views.RecipeEdit, name='recipe-edit'),
]