from django.shortcuts import render
from django.http import HttpResponse
from guestbook.models import *

# Create your views here.

# 주소만 입력했을 경우
def index(request) :
    return render(request, 'index.html')

# show_content
def show_content(request) :
    
    # 저장된 데이터를 가져온다.
    m1 = GuestBookModel.objects.order_by('-id')
    # print(m1)
    
    # html을 구성하기 위한 데이터를 딕셔너리에 담는다.
    data_dict = {
        'result_list' : m1
    }
    
    return render(request, 'content.html', data_dict)

# add_content
def add_content(request) :
    
    # post로 요청될 때 전달된 데이터를 추출한다.
    writer = request.POST['writer']
    content = request.POST['content']
    
    # print(writer)
    # print(content)
    
    # 저장한다.
    m1 = GuestBookModel(writer=writer, content=content)
    m1.save()
    
    a1 = '''
            <script>
                alert('저장되었습니다')
                location.href = 'show_content'
            </script>
         '''
         
    return HttpResponse(a1)

# delete_content
def delete_content(request) :
    
    # id 값을 추출한다.
    id = request.GET['id']
    
    # 삭제처리
    m1 = GuestBookModel.objects.get(id=id)
    m1.delete()
    
    a1 = '''
            <script>
                alert('삭제되었습니다')
                location.href = 'show_content'
            </script>
         '''
    return HttpResponse(a1)