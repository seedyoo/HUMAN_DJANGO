

from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # 게시글
    # '/board/'
    path('', views.BoardList.as_view(), name='board_list'),
    
    # '/board/board/10'
    path('/<int:pk>', views.BoardDetail.as_view(), name='board_detail'),
]