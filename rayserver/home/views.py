from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
