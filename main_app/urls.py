from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),\
  path('Wishitem/create', views.WishitemAdd.as_view(), name='wish_item_add'),
  path('Wishitem/<int:pk>/delete', views.WishitemDelete.as_view(), name='delete_wish_item'),
]
