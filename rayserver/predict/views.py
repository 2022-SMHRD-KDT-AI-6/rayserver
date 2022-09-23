
from .models import ImgSave, Post, Test, Test2, Test3
from django.shortcuts import render, redirect
from datetime import datetime
from member.models import Members

# from keras.models import model_from_json
from PIL import Image
import numpy as np

# Create your views here.
def home(request):
    return render(request, 'predict/home.html')

def predict(request):
    return render(request, 'predict/predict.html')


def result(request):
    import numpy as np
    import pickle

    sc = pickle.load(open('sc.pkl', 'rb'))
    model = pickle.load(open('classifier.pkl', 'rb'))

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    input_features = np.array([val1,val2,val3,val4,val5,val6,val7,val8])
    pred = model.predict(sc.transform(input_features.reshape(1,-1)))
    result1 = pred
    if pred==[1]:
        result1 = "당뇨병 같은데, 의사선생님께 문의하세요"
    else:
        result1 = "건강하신거 같은데 의사선생님께 확인 하세요"
    return render(request, 'predict/result.html', {"result_pred":result1})    

def postcreate2(request):
    if request.method == "POST":
        print(111, request.POST)
        print(222, request.FILES)
        
        title = request.POST["title"]
        text = request.POST["text"]
        image =  request.FILES["image"]
        # image = request.POST["image"]

        upload = Post.objects.create(title,text,image)
        upload.image = image
        upload.save()
        return redirect("/")

def practice(request):
    return render(request, 'predict/practice.html')




def detail(request):
    return render(request, 'predict/detail.html')




def postcreate(request):
    blog = Post()
    blog.title = request.POST["title"]
    blog.text = request.POST["text"]
    blog.image =  request.FILES["image"]
    blog.save()
    # return redirect("user:raylogin" + str(blog.id))
    return redirect("detail/"+str(blog.id))


        #       {% if not 'm_id' in request.session %}
        #       <a href="/member/register">[회원가입]</a><br>
        #       <a href="/member/login">[로그인]</a>
        #   {% else %}
        #       {{ m_name }} 님 어서오세요.


# 업로드 링크
UPLOAD_DIR = 'media/'

def imgtest(request):
    if request.method == "POST":
        mem_id = request.session['m_id']
        user_id = Members.objects.get(pk=mem_id)
        test = ImgSave()
        test.exam_img =  request.FILES["exam_img"]
        test.exam_result = '1'


        if 'exam_img' in request.FILES:
            # 파라미터 처리
            file = request.FILES['exam_img']
            file_name = file.name  # 첨부파일 이름
            print(file_name)

            fp = open("%s%s" % (UPLOAD_DIR, file_name), 'wb')
            # 파일을 1바이트씩 조금씩 읽어서 저장
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()  # 파일 닫기

            # ---추가-- 어차피 개 어려운거 실행이라도 해보는게 의의-------
            # model.json 파일 열기
            json_file = open('catdog_model.json')
            loaded_model_json = json_file.read()
            json_file.close()

            # json 파일로부터 model 로드하기
            loaded_model = model_from_json(loaded_model_json)
            # json model에 가중치 값 로드하기
            loaded_model.load_weights("model.h5")
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

            # 예측해서 50% 이면 cat, 아니면 dog
            if y_predict >= 0.5:
                print("cat",y_predict)
            else:
                print("dog",y_predict)


        else:
            file_name = '-'
        # return render(request, "predict/predict.html", {'file_name': file_name})
        test.mem = user_id
        test.save()
        return render(request, 'predict/predict.html')
    return render(request, 'predict/imgtest.html')
