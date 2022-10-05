from django.db.models import Max, Min, Avg
from django.shortcuts import render
from rest_framework.views import APIView
from member.models import Members
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from datetime import datetime
from predict.models import ImgSave
from keras.models import load_model
import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from .models import GameScore, GameScore2

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

class MobileShowMember(APIView):
    def post(self, request):
        print("로그 : " +str(request.body))
        mem_id = request.data.get('mem_id',"")
        user = Members.objects.filter(mem_id=mem_id).first()
        data = dict(
            mem_id=user.mem_id,
            mem_name=user.mem_name,
            mem_birth = user.mem_birth,
            mem_gender = user.mem_gender,
            mem_joindate =user.mem_joindate,
            mem_type = user.mem_type
            )
        return Response(data)


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
            return Response(dict(msg="아이디 중복", code="400"))
        else:
            Members.objects.create(
                mem_id=mem_id, mem_pw=mem_pw_crypted,  mem_name=mem_name, mem_birth=mem_birth, mem_gender=mem_gender, mem_type=mem_type,
                mem_joindate=datetime.now())
            context['message'] = mem_name + "님 회원가입 되었습니다."
            return Response(dict(msg="회원가입성공", code="200"))



from matplotlib import pyplot as plt 
# 업로드 링크
UPLOAD_DIR = 'media/'

def Dataization(img_path):
    image_h = 28
    image_w = 28
    img = cv2.imread(img_path)
    # k = np.array([[1,1,1],[1,1,1],[1,1,1]]) * (1/9)
    # 미디언 블러 처리
    # blur = cv2.filter2D(img, -1, k)
    
    # Edge Dectect Canny
    # canny = cv2.Canny(blur, 30, 100)
    # canny = cv2.Canny(merged, 30, 100)
    # 회색조 처리
    # img1 = cv2.imread(img_path, canny)
    # img = can
    # 임계값 처리
    ret, thresh = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
    img = thresh
    # 흑백 반전
    inverted_image = cv2.bitwise_not(img)
    img = inverted_image
    # 사이즈 변환 512 * 512
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    #정규화
    img = cv2.normalize(img, None, alpha=0,beta=230, norm_type=cv2.NORM_MINMAX)
    return (img/256)

class ImageScore(APIView):
    def post(self, request):
        print("로그 : " + str(request.body))
        mem_id = request.data.get('mem_id', "")
        user_id = Members.objects.get(pk=mem_id)
        print(user_id)
        test = ImgSave()
        test.exam_img =  request.FILES["exam_img"]
        test.mem = user_id
        test.save()

        if 'exam_img' in request.FILES:
            # 파라미터 처리
            file = request.FILES['exam_img']
            file_name = file.name  # 첨부파일 이름
            print(file_name)
            fp = open("%s%s" % (UPLOAD_DIR, file_name), 'wb')
            # 파일을 1바이트씩 조금씩 읽어서 저장
            for chunk in file.chunks():
                fp.write(chunk)
                print('a')
            fp.close()  # 파일 닫기
            # 이미지 불러오기
            # img = cv2.imread("%s%s" % (UPLOAD_DIR, file_name), cv2.IMREAD_COLOR)
            # 블러 처리를 위한 마스크 생성
            print("s"+request.FILES["exam_img"].name)
            print(file)
            categories = ["36.0","35.5","35.0","34.5","34.0","33.5","33.0","32.5","32.0","31.5","31.0","30.5","30.0",
                "29.5","29.0","28.5","28.0","27.5","27.0","26.5","26.0","25.5","25.0","24.5","24.0",
                "23.5","23.0","22.5","22.0","21.5","21.0","20.5","20.0","19.5","19.0","18.5",
                "18.0","17.5","17.0","16.5","16.0","15.5","15.0","14.5","14.0","13.5","13.0",
                "12.5","12.0","11.5","11.0","10.5","10.0","9.5","9.0","8.5","8.0","7.5","7.0",
                "6.5","6.0","5.5","5.0","4.5","4.0","3.5","3.0","2.5","2.0","1.5","1.0","0.5",]
            src = []
            name = []
            test2 = []
            image_dir = UPLOAD_DIR
            # for file in os.listdir(image_dir):     
            #     print('a')
            src.append(image_dir + file_name)
            name.append(file)
            test2.append(Dataization(image_dir + file_name))
            test2 = np.array(test2)
            model = load_model('ray_canny_1004.h5')
            # 오류 해결
            y_prob = model.predict(test2, verbose=0) 
            predict = y_prob.argmax(axis=-1)
            raypredict = categories[predict[0]]
            print("예측 : "+ raypredict)
            test.exam_result = raypredict
            print(raypredict)
        else:
            file_name = '-'
        scoreSave = ImgSave.objects.filter(mem_id=mem_id).order_by('-mem_seq')[0]
        scoreSave.exam_result = raypredict
        scoreSave.save()
        return Response(dict(msg="이미지저장완료", code="200",score=raypredict))
        
class ScoreData(APIView):
    def post(self, request):
        print("로그:"+str(request.body))
        mem_id = request.data.get('mem_id', "")
        class_object = ImgSave.objects.filter(mem_id=mem_id).order_by('-mem_seq')[0]
        return Response(dict(msg="이미지저장완료", code="200",imgurl=class_object.exam_img.url, score=class_object.exam_result, date=class_object.exam_date))

class GameSave(APIView):
    def post(self, request):
        print("로그 : " + str(request.body))
        mem_id = request.data.get('mem_id', "")
        user_id = Members.objects.get(pk=mem_id)
        score1 = request.data.get('game_score1', 0)
        score2 = request.data.get('game_score2', 0)
        score3 = request.data.get('game_score3', 0)
        score4 = request.data.get('game_score4', 0)
        obj = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score1').aggregate(game_score1=Max('game_score1'))
        obj2 = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score2').aggregate(game_score2=Max('game_score2'))
        obj3 = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score3').aggregate(game_score3=Max('game_score3'))
        obj4 = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score4').aggregate(game_score4=Max('game_score4'))
        max1 = obj['game_score1']
        max2 = obj2['game_score2']
        max3 = obj3['game_score3']
        max4 = obj4['game_score4']
        if max1 == None or max2==None or max3==None or max4==None:
            test = GameScore2()
            test.game_score1 = score1
            test.game_score2 = score2
            test.game_score3 = score3
            test.game_score4 = score4
            test.mem = user_id
            test.save()
        else:
            if int(max1) <= int(score1) or int(max2) <= int(score2) or int(max3) <= int(score3) or int(max4) <= int(score4):
                test = GameScore2()
                test.game_score1 = score1
                test.game_score2 = score2
                test.game_score3 = score3
                test.game_score4 = score4
                test.mem = user_id
                test.save()
            else:
                return Response(dict(msg="게임점수저장실패", code="400"))
        return Response(dict(msg="게임점수저장성공", code="200"))


class GameScoreShow(APIView):
    def post(self, request):
        mem_id = request.data.get('mem_id', "")
        obj = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score1').aggregate(game_score1=Max('game_score1'))
        obj2 = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score2').aggregate(game_score2=Max('game_score2'))
        obj3 = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score3').aggregate(game_score3=Max('game_score3'))
        obj4 = GameScore2.objects.filter(mem_id=mem_id).order_by('-game_score4').aggregate(game_score4=Max('game_score4'))
        max1 = obj['game_score1']
        max2 = obj2['game_score2']
        max3 = obj3['game_score3']
        max4 = obj4['game_score4']
        print(max1)
        print(max2)
        print(max3)
        print(max4)
        data= dict(
            max1=max1,
            max2=max2,
            max3=max3,
            max4=max4
        )
        return Response(data)