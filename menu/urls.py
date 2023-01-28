from django.urls import path
from .views import MainView, MenuView, CategoryView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('menu/<slug:menu_slug>', MenuView.as_view(), name='menu'),
    path('<slug:menu_slug>/<slug:category_slug>', CategoryView.as_view(), name='category'),
]