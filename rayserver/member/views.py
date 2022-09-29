from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from .models import Members
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response


def index(request):
    context = {}
    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/index.html', context)

@csrf_exempt
def member_reg(request):
    if request.method == "GET":
        return render(request, 'home/pages/samples/registern.html')
    elif request.method == "POST":
        context = {}
        mem_id = request.POST["mem_id"]
        mem_pw = request.POST["mem_pw"]
        mem_pw2 = request.POST["mem_pw2"]
        mem_name = request.POST["mem_name"]
        mem_birth_y = request.POST["mem_birth_y"]
        mem_birth_m = request.POST["mem_birth_m"]
        mem_birth_d = request.POST["mem_birth_d"]
        mem_birth = mem_birth_y+"-"+mem_birth_m+"-"+mem_birth_d
        mem_gender = request.POST["mem_gender"]
        mem_type = request.POST["mem_type"]
        mem_pw_crypted = make_password(mem_pw)    # 암호화
        print(mem_birth)

        if mem_pw != mem_pw2:
            context = {}
            context['message'] = "비밀번호 재확인 하십시오"
            return render(request, 'home/pages/samples/registern.html', context)

        # 비밀번호 확인하기


        # 회원가입 중복체크
        rs = Members.objects.filter(mem_id=mem_id)
        if rs.exists():
            context['message'] = mem_id + "가 중복됩니다."
            return render(request, 'home/pages/samples/registern.html', context)
        else:
            Members.objects.create(
                mem_id=mem_id, mem_pw=mem_pw_crypted,  mem_name=mem_name, mem_birth=mem_birth, mem_gender=mem_gender, mem_type=mem_type,
                mem_joindate=datetime.now())
            context['message'] = mem_name + "님 회원가입 되었습니다."
            # return render(request, 'home/index.html', context)
            return redirect('/',context)

@csrf_exempt
def member_login(request):
    if request.method == "GET":
        return render(request, 'home/pages/samples/loginn.html')
    elif request.method == "POST":
        context = {}

        mem_id = request.POST.get('mem_id')
        mem_pw = request.POST.get('mem_pw')

        # 로그인 체크하기
        rs = Members.objects.filter(mem_id=mem_id).first()
        

        print(mem_id + '/' + mem_pw)
        print(rs)
        #if rs.exists():
        if rs is None:
            print(Response(dict(msg="해당 ID의 사용자가 없습니다.")))
            return render(request, "home/pages/samples/loginn.html", status=401)
        if check_password(mem_pw, rs.mem_pw):
            # OK - 로그인
            request.session['m_id'] = mem_id
            request.session['m_name'] = rs.mem_name
            context['m_id'] = mem_id
            context['m_name'] = rs.mem_name
            context['message'] = rs.mem_name + "님이 로그인하셨습니다."
            # return render(request, 'home/index.html', context)
            return redirect('/',context)
        else:
            context['message'] = "로그인 실패. 패스워드 불일치\\n\\n확인하신 후 다시 시도해 주십시오."
            return render(request, 'home/pages/samples/loginn.html', context)
@csrf_exempt
def member_logout(request):
    request.session.flush()
    return redirect('/')

