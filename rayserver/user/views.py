#views.py
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializer import LoginUserSerializer
from .models import LoginUser, JoinTable
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
# Create your views here.



from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def home_view(request):
    context = {}
    # m_id 세션변수 값이 없다면 ''을 넣어라
    context['m_id'] = request.session.get('m_id','')
    context['m_name'] = request.session.get('m_name','')
    return render(request, "user/index.html", context)

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        print("request "+ str(request))
        print("body "+ str(request.body))
        user_id = request.POST.get("user_id", "")
        user_pw = request.POST.get("user_pw", "")
        birth_day = request.POST.get("birth_day", "")
        gender = request.POST.get("gender", "")
        email = request.POST.get("email", "")
        name = request.POST.get("name", "")
        age = request.POST.get("age", "")
        print('회원가입완료')
        print("아이디 : " + user_id + user_pw + birth_day + gender + email+name+age)
        return redirect("user:signup")
    return render(request, "user/signup.html")

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        print("request "+ str(request))
        print("body "+ str(request.body))
        userid = request.POST.get("userid", "")
        userpw = request.POST.get("userpw", "")
        user = authenticate(username=userid, password=userpw)
        print("userid = " + userid + " result = " + str(user))
        if user:
            print("로그인성공")
            login(request, user)
            
        else:
            print("로그인실패")
            return render(request, "user/login.html", status=401)
    return render(request, "user/login.html")

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("user:raylogin")



class UserLogin(APIView):
    @csrf_exempt 
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is None:
            print(Response(dict(msg="해당 ID의 사용자가 없습니다.")))
            return render(request, "user/login.html", status=401)
        if check_password(user_pw, user.user_pw):
            data = dict(msg="로그인 성공", user_id=user.user_id, birth_day=user.birth_day,
                                 gender=user.gender, email=user.email, name=user.name, age=user.age)
            # HttpResponse(status=200)
            print('로그인성공했습니다.')
            print(data['user_id'])
            return render(request, "user/index.html", data, status=200)
        else:
            Response(dict(msg="로그인 실패. 패스워드 불일치"))
            return render(request, "user/login.html", status=401)




class UserRegist(APIView):
    @csrf_exempt 
    def post(self, request):
        user_id = request.data.get("user_id", "")
        user_pw = request.data.get("user_pw", "")
        birth_day = request.data.get("birth_day", "")
        gender = request.data.get("gender", "")
        email = request.data.get("email", "")
        name = request.data.get("name", "")
        age = request.data.get("age", "")
        user_pw_crypted = make_password(user_pw)    # 암호화
        if LoginUser.objects.filter(user_id=user_id).exists():
            # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체에 담음
            user = LoginUser.objects.filter(user_id=user_id).first()
            data = dict(
                msg="이미 존재하는 아이디입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw
            )
            print('회원가입실패')
            print(data)
            return render(request, "user/signup.html", status=200)
        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_crypted, birth_day=birth_day, gender=gender, email=email, name=name, age=age)
        data = dict(
            user_id=user_id,
            user_pw=user_pw_crypted,
            birth_day=birth_day,
            gender=gender,
            email=email,
            name=name,
            age=age
        )
        print('회원가입성공')
        return render(request, "user/login.html", data ,status=200)

# 어플
class MobileLogin(APIView):
    def post(self, request):
        print("리퀘스트 로그" + str(request.body))
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        print("id = " + user_id + " pw = " + user_pw)

        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is None:
            print("해당 ID의 사용자가 없습니다.")
            return Response(dict(msg="해당 ID의 사용자가 없습니다.", code="500"))
        if check_password(user_pw, user.user_pw):
            print("로그인 성공!")
            return Response(dict(msg="로그인 성공", user_id=user.user_id, birth_day=user.birth_day,
                                 gender=user.gender, email=user.email, name=user.name, age=user.age, code="200"))
        else:
            print("실패")
            return Response(dict(msg="로그인 실패. 패스워드 불일치", code="400"))


class MobileRegist(APIView):
    def post(self, request):
        print("리퀘스트 로그" + str(request.body))
        serializer = LoginUserSerializer(request.data)

        if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
            # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체에 담음
            user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
            data = dict(
                msg="이미 존재하는 아이디입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw,
                code = "400"
            )
            return Response(data)
        user = serializer.create(request.data)
        return Response(data=LoginUserSerializer(user).data)



