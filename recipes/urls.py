from django.urls import path
from recipes import views

# comando para criar uma url, o mesmo detém as duas configurações criadas no arquivo views
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe)
]

