from contextlib import redirect_stderr
from django.shortcuts import render
from predict.models import ImgSave
from django.http import JsonResponse
# Create your views here.
def chart_bar(request):
    imgdata = ImgSave.all().filter(mem_id='1')
    return render(request, "home/piechart.html", {
        'chartdata':imgdata
    })

def chart_bar2(request):
    import psycopg2
    dbCon = psycopg2.connect('localhost', 'root', '1234', 'raydb')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute("SELECT yyyymm, sales_amt, sales_predict FROM sales_predict")
        rsSales = cursor.fetchall()

    return render(request, "chart_bar2.html", {
        'title' : '판매 예측',
        'dtitle1' : '실적',
        'dtitle2' : '예측',
        'rsSales' : rsSales
    })
import psycopg2



from rest_framework.views import APIView
from rest_framework.response import Response    



class ResultAPIView(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request): 
        data = request.session.get('result')
        return Response(data)

def result_detail(request):

    context = {}
    return render(request, 'chart/chart_example.html', context )

def chartShow(request):
    num=0
    cnt=0
    object = ImgSave.objects.all()
    for i in object:
            if i.exam_result=="":
                i.exam_result=0
            num +=float(i.exam_result)
            cnt +=1
    avg = int(num/cnt)
    print(avg)
    context = {'avg' : avg}
    return render(request,'chart/chart_example.html', context)
    
from member.models import Members
from django.views import View
class ChartView(View):
    def get(self, request):
        results = []
        object = ImgSave.objects.all()
        num = 0
        cnt = 0
        for i in object:
            if i.exam_result=="":
                i.exam_result=0
            num +=float(i.exam_result)
            cnt +=1
            results.append({
                "score":i.exam_result
            })
        print(num)
        print(cnt)
        avg = num/cnt
        print(avg)
        mem_id = self.request.session.get("m_id")
        
        object2 = Members.objects.filter(mem_gender='m')
        
        
        cnt2=0
        for i in object2:
            print(i.mem_id)
            cnt2+=1
        print('남자수')
        print(cnt2)

        # object4 = object.union(object2)
        # print(object4)
        return JsonResponse({"results":results},status=200)



def chart_bar3(request):
    dbCon = psycopg2.connect(dbname="raydb", user="root", password="1234")
    cursor = dbCon.cursor()
    with dbCon:
        # 전체 평균구하기
        cursor.execute("SELECT exam_result FROM t_exam")
        scores = cursor.fetchall()
        results = []
        num = 0
        cnt = 0
        for i in scores:
            if i[0] == "":
                pass
            else:
                cnt += 1
                num += float(i[0])
                results.append({
                "score":i[0]
            })
        avg = int(num/cnt)
        
        # 남자 중에서 전체 평균구하기
        cursor.execute("SELECT mem_id FROM t_member")
        mem_id = cursor.fetchall()
        context = {
            'avg' : avg,
            'scores' : scores,
            'mem_id': mem_id
            }
    return render(request, "chart/chart_example.html", context)