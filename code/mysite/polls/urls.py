
from django.urls import path
from . import views


urlpatterns = [
    # ""(루트) 경로 요청, views.py 파일의 index 함수 호출
    # name="경로 이름"
    # http://localhost:8000/polls  -->  index()
    path("", views.index, name="index"),
]
