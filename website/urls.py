
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name =""),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout',views.logout, name="logout"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('create-record',views.create_record, name = "create-record"),
    path('update-record/<int:pk>',views.update_record, name="update-record"),
    path('record/<int:pk>',views.singular_record, name="record"),
    path('view-record/<int:pk>', views.view_record, name="view-record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    path('games', views.games, name ="games"),
    path('game-data', views.game.data, name="game-data"),
    
]