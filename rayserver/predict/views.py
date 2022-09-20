from django.shortcuts import render

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