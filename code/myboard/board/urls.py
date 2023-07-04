

from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # 게시글
    # 게시글 목록 - '/board/'
    path('', views.BoardList.as_view(), name='board_list'),
    
    # 게시글 조회 - '/board/board/10'
    path('<int:pk>', views.BoardDetail.as_view(), name='board_detail'),

    # 게시글 쓰기 - '/board/insert'
    path('insert/', views.BoardInsert.as_view(), name='board_insert'),
    
    # 게시글 수정 - '/board/update'
    path('<int:pk>/update', views.BoardUpdate.as_view(), name='board_update'),
    
    
    
]