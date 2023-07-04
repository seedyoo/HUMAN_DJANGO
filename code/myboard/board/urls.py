

from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    # 게시글
    # '/boards/'
    path('', views.BoardList.as_view(), name='board_list'),
    
    # '/boards/board/10'
    path('/<int:pk>', views.BoardDetail.as_view(), name='board_detail'),
]