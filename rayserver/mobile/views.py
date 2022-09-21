from django.shortcuts import render
from rest_framework.views import APIView
from member.models import Members
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response


# 어플
class MobileLogin(APIView):
    def post(self, request):
        print("리퀘스트 로그" + str(request.body))
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        print("id = " + user_id + " pw = " + user_pw)

        user = Members.objects.filter(user_id=user_id).first()
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




