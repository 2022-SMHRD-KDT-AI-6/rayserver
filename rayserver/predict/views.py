
from .models import Post, Test
from django.shortcuts import render, redirect
from datetime import datetime
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

def imgtest(request):
    if request.method == "POST":
        test = Test()
        test.exam_img =  request.FILES["exam_img"]
        test.exam_date = datetime.now()
        test.exam_result = request.POST["exam_result"]
        test.mem_id = request.POST["mem_id"]
        test.save()
        print('123')
        return render(request, 'predict/predict.html')
    return render(request, 'predict/imgtest.html')
    # return redirect("user:raylogin" + str(blog.id))
    # return redirect("detail/"+str(blog.id))
