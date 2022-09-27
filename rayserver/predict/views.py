from fileinput import filename
from .models import ImgSave, Post, Test, Test2, Test3
from django.shortcuts import render, redirect
from datetime import datetime
from member.models import Members
from predict.models import ImgSave

import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
from matplotlib import pyplot as plt 

# from keras.models import model_from_json
from PIL import Image
import numpy as np

# Create your views here.
def home(request):
    return render(request, 'predict/home.html')

def predict(request):
    return render(request, 'predict/predict.html')

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
class ProductDetailView(DetailView):
    template_name = "predict/product_detail.html"
    queryset = ImgSave.objects.all().order_by('-mem_seq')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Data = 장바구니데이타(self.request)
        # cartItems = Data['cartItems']
        # context['cartItems'] = cartItems
        print(context)
        return context
def scoredata(request):
    query_set = ImgSave.objects.first()
    obj= ImgSave.objects.filter(id=1).order_by('-id')[0]
    obj2=ImgSave.objects.filter(id=2)
# {{class_object.exam_img.url}}
# Create your views here.
def scoredata2(request):
    class_object = ImgSave.objects.filter(mem_id="111").order_by('-mem_seq')[0]
    return render(request, 'predict/recent.html', {'class_object': class_object})   

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


# 업로드 링크
UPLOAD_DIR = 'media/'




categories = ["36.0","35.5","35.0","34.5","34.0","33.5","33.0","32.5","32.0","31.5","31.0","30.5","30.0",
                "29.5","29.0","28.5","28.0","27.5","27.0","26.5","26.0","25.5","25.0","24.5","24.0",
                "23.5","23.0","22.5","22.0","21.5","21.0","20.5","20.0","19.5","19.0","18.5",
                "18.0","17.5","17.0","16.5","16.0","15.5","15.0","14.5","14.0","13.5","13.0",
                "12.5","12.0","11.5","11.0","10.5","10.0","9.5","9.0","8.5","8.0","7.5","7.0",
                "6.5","6.0","5.5","5.0","4.5","4.0","3.5","3.0","2.5","2.0","1.5","1.0","0.5"]


def Dataization(img_path):
    image_h = 224
    image_w = 224
    img = cv2.imread(img_path)
    k = np.array([[1,1,1],[1,1,1],[1,1,1]]) * (1/9)
    # 미디언 블러 처리
    blur = cv2.filter2D(img, -1, k)
    
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


def imgtest(request):
    print(request)
    print(request.POST.dict())
    if request.method == "POST":
        mem_id = request.session['m_id']
        user_id = Members.objects.get(pk=mem_id)
        imgsave = ImgSave()
        imgsave.exam_img =  request.FILES["exam_img"]
        imgsave.mem = user_id
        imgsave.save()
        if 'exam_img' in request.FILES:
            # 파라미터 처리
            file = request.FILES['exam_img']
            file_name = file.name  # 첨부파일 이름
            print(file_name)
            src = []
            name = []
            test = []
            # 이미지 불러오기
            image_dir = UPLOAD_DIR
            src.append(image_dir + file_name)
            name.append(file)
            test.append(Dataization(image_dir + file_name))
            test = np.array(test)
            model = load_model('model.h5')

            y_prob = model.predict(test, verbose=0) 
            predict = y_prob.argmax(axis=-1)
            raypredict = categories[predict[0]]

            print("예측 : "+ raypredict)
            imgsave.exam_result = raypredict
        else:
            file_name = '-'
        board = ImgSave.objects.filter(mem_id=mem_id).order_by('-mem_seq')[0]
        board.exam_result = raypredict
        board.save()
        return render(request, 'predict/predict.html')
    return render(request, 'predict/imgtest.html')
