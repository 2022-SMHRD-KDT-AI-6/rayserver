from django.shortcuts import render
from board.models import Writing
from django.views.decorators.csrf import csrf_protect
# from keras.models import model_from_json
from PIL import Image
import numpy as np

# Create your views here.
# Create your views here.
def main(request):
    return render(request, 'fileup/upform1.html')
def main2(request):
    return render(request, "fileup/upform2.html")

# 업로드 링크
UPLOAD_DIR = '/rayserver/media/'


# @csrf_protect
def upload_success(request):
# request.FILES : enctype으로 전소오디어 온 파일 파라미터 객체
# .name 등의 파일의 정보를 받을 수 있다.
    if 'file1' in request.FILES:
# 파라미터 처리
        file = request.FILES['file1']
        file_name = file.name  # 첨부파일 이름

# 파일 오픈 - wb모드(binary)
        fp = open("%s%s" % (UPLOAD_DIR, file_name), 'wb')

# 파일을 1바이트씩 조금씩 읽어서 저장
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()  # 파일 닫기
    else:
        file_name = '-'
    return render(request, "fileup/success.html", {'file_name': file_name})



@csrf_protect
def upload_success2(request):
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file.name
        
        fp = open("%s%s" % (UPLOAD_DIR, file_name), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

        # ---추가-- 어차피 개 어려운거 실행이라도 해보는게 의의-------
        # model.json 파일 열기
        json_file = open('/home/kosmo_03/PycharmProjects/myapps/fileup/static/catdog_model.json')
        loaded_model_json = json_file.read()
        json_file.close()

        # json 파일로부터 model 로드하기
        loaded_model = model_from_json(loaded_model_json)
        # json model에 가중치 값 로드하기
        loaded_model.load_weights("/home/kosmo_03/PycharmProjects/myapps/fileup/static/model.h5")
        loaded_model.compile(loss='binary_crossentopy', optimizer='adam', metrics=['accuracy'])
        # 가중치와 모델을 로드 완료
        image = Image.open("%s%s"%(UPLOAD_DIR,file_name))
        width = 64
        height = 64
        image = image.resize((width,height))

        # 이미지를 벡터화
        image = np.array(image)
        x_test = [image]
        x_test = np.array(x_test)
        x_test = x_test /255
        y_predict = loaded_model.predict(x_test)
        category = ""

    # 예측해서 50% 이면 cat, 아니면 dog
        if y_predict >= 0.5:
            category = "cat"
            print("cat",y_predict)
        else:
            category = "dag"
            print("dog",y_predict)

    # --------------- 추가 완료 -----------------------------
    else:
        file_name = '-'
    return render(request, "fileup/success2.html", {'file_name': file_name, 'y_predict':y_predict, 'category':category})