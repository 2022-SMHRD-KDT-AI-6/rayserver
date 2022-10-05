from django.shortcuts import render
from predict.models import ImgSave
from django.db.models import Q

# filter 함수의 Q함수: OR조건으로 데이터를 조회하기 위해 사용하는 함수
# objects.filter() 는 특정 조건에 해당하면 객체 출력 .get('kw') 은 kw만 반환
# __icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사. 사용법 "필드명"__icontains = 조건값

def searchResult(request):
    
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        products = ImgSave.objects.all().filter(
            Q(mem_seq__icontains=query) | #순번 검색
            Q(exam_result__icontains=query) #점수결과 검색
            #Q((mem.mem_id)__icontains=query) #아이디결과 검색
        )

    return render(request, 'search/search.html', {'query':query, 'products':products})
from django.core.paginator import Paginator
from home.models import PlaceInfo

def searchResult2(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        boards = PlaceInfo.objects.all().filter(
            Q(category__icontains=query) | # 카테고리검색
            Q(name__icontains=query)| # 이름검색
            Q(address__icontains=query)| # 주소검색
            Q(tel__icontains=query) # 전화검색
        )
        page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
        paginator = Paginator(boards, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
        page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
        return render(request, 'search/search2.html', {'query':query, 'page_obj':page_obj})