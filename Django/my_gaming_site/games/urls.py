from django.urls import path
from .views import (
    home,
    number_guessing,
    tic_tac_toe,
    snake_game,
    peak_game,
    game_2048,
    signup,
    user_login,
    profile_view
)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', profile_view, name='profile'),
    path('number-guessing/', number_guessing, name='number_guessing'),
    path('tic-tac-toe/', tic_tac_toe, name='tic_tac_toe'),
    path('snake/', snake_game, name='snake_game'),
    path('peak/', peak_game, name='peak_game'),
    path('2048/', game_2048, name='game_2048'),
]
