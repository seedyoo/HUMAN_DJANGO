from django.contrib import admin
from .models import *       # models 모듈

# Register your models here.
# 관리자 페이지에서 polls 애플리케이션을 관리하도록 등록
admin.site.register(Question)
admin.site.register(Choice)