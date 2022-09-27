from http.client import HTTPResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from predict.models import ImgSave
import json
from django.http import JsonResponse
from django.views import View

# Create your views here.

def index(request):
    context = {}
    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/index.html', context)



def home_view(request):
    context = {}
    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/index2.html', context)

def introcom_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/pages/samples/뉴로젠.html', context)

def introrey_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/pages/samples/프로젝트소개.html', context)

def introteam_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/pages/samples/기억할레이.html', context)

def imgresult_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'predict/all.html', context)



class ChartView(View):
    def get(self, request):
        results = []
        object = ImgSave.objects.all()
        num = 0
        cnt = 0
        for i in object:
            if i.exam_result=="":
                i.exam_result=0
            num +=float(i.exam_result)
            cnt +=1
            results.append({
                "score":i.exam_result
            })
        print(num)
        print(cnt)
        avg = num/cnt
        print(avg)
        # return HTTPResponse(avg)
        return JsonResponse({"results":results},status=200)

