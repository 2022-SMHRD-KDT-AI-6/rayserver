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
        )

    return render(request, 'search/search.html', {'query':query, 'products':products})

from django.views.generic import CreateView, DetailView,TemplateView,View

class StoreView(TemplateView):
    template_name = "predict/all.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Data = 장바구니데이타(self.request)
        # cartItems = Data['cartItems']
        # products = ImgSave.objects.all().order_by('-mem_seq')
        # request.session['m_id'] = mem_id
        # mem_id = request.session.get('m_id', '')
        # print('a :  '+context['m_id'])
        
        
        mem_id = self.request.session.get("m_id")
        products = ImgSave.objects.filter(mem_id=mem_id).order_by('-mem_seq')
        context['products'] = products
        # context['cartItems'] = cartItems
        print(context)
        return context