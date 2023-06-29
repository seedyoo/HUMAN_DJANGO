from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from polls.models import Question, Choice

# Create your views here.
# 설문 목록 뷰
def index(request):
    # return HttpResponse('Hello')
    # 설문 목록을 조회
    question_list = Question.objects.all()  # Question 테이블의 전체목록
    context = {'question_list' : question_list}
    return render(request, 'polls/index.html', context)


# 설문 뷰
def detail(request, question_id):
    # question_id 로 데이터 조회
    question = get_object_or_404(Question, pk=question_id)
    
    # 응답할 템플릿을 지정 (detail.html)
    return render(request, 'polls/detail.html', {'question' : question})
    # render()
    # : 요청객체(request)를 지정해주고, 응답할 화면을 지정
    #  HttpResponse 객체를 반환
    #   - 클라이언트에게 응답할 내용
    #   - 화면을 렌더링한 결과 포함
    
    
    
    
    
    