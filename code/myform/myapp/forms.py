from django import forms

# Form 양식 만들기
class NameForm(forms.Form):
    your_name = forms.CharField(label="이름", max_length=100)
    
    # 화면에 렌더링 되는 코드
    '''
        <label for="your_name">이름 : </label>
        <input id="your_name" type="text" 
               name="your_name" maxlength="100" required>
    '''
    
    
    