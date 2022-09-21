from django.shortcuts import render
from rest_framework.views import APIView
from member.models import Members
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from datetime import datetime

# 어플
class MobileLogin(APIView):
    def post(self, request):
        print("리퀘스트 로그" + str(request.body))
        mem_id = request.data.get('mem_id', "")
        mem_pw = request.data.get('mem_pw', "")
        print("id = " + mem_id + " pw = " + mem_pw)

        user = Members.objects.filter(mem_id=mem_id).first()
        if user is None:
            print("해당 ID의 사용자가 없습니다.")
            return Response(dict(msg="해당 ID의 사용자가 없습니다.", code="500"))
        if check_password(mem_pw, user.mem_pw):
            print("로그인 성공!")
            return Response(dict(msg="로그인 성공", mem_id=user.mem_id, code="200"))
        else:
            print("실패")
            return Response(dict(msg="로그인 실패. 패스워드 불일치", code="400"))


class MobileRegist(APIView):
    def post(self, request):
        print("로그 : " + str(request.body))
        context = {}
        mem_id = request.data.get('mem_id', "")
        mem_pw = request.data.get('mem_pw', "")
        mem_name = request.data.get('mem_name', "")
        mem_birth = request.data.get('mem_birth', "")
        mem_gender = request.data.get('mem_gender', "")
        mem_type = request.data.get('mem_type', "")

        mem_pw_crypted = make_password(mem_pw)    # 암호화
        # 회원가입 중복체크
        rs = Members.objects.filter(mem_id=mem_id)
        if rs.exists():
            context['message'] = mem_id + "가 중복됩니다."
            return Response(dict(msg="아이디 중복", mem_id=rs.mem_id, code="400"))
        else:
            Members.objects.create(
                mem_id=mem_id, mem_pw=mem_pw_crypted,  mem_name=mem_name, mem_birth=mem_birth, mem_gender=mem_gender, mem_type=mem_type,
                mem_joindate=datetime.now())
            context['message'] = mem_name + "님 회원가입 되었습니다."
            return Response(dict(msg="회원가입성공", mem_id=rs.mem_id, code="200"))



