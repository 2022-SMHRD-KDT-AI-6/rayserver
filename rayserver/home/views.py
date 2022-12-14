from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from requests import session
from predict.models import ImgSave
import json
from django.http import HttpResponse, JsonResponse
from django.views import View
import psycopg2
from django.contrib.auth.hashers import make_password, check_password
from .models import PlaceInfo
from member.models import Members
from datetime import datetime

# Create your views here.

def index(request):
    context = {}
    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/index3.html', context)



def home_view(request):
    context = {}
    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/index2.html', context)

def introcom_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/pages/samples/뉴로젠.html', context)

def introrey_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/pages/samples/프로젝트소개.html', context)

def introteam_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'home/pages/samples/기억할레이.html', context)

def imgresult_view(request):
    context = {}
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
    return render(request, 'predict/all.html', context)

@csrf_exempt
def change_view(request):
    if request.method == "GET":
        mem_id = request.session.get('m_id','')
        user = Members.objects.filter(mem_id = mem_id).all()
        context = {'user': user}
        # request.session = {
        # 'user_info' : user
        #     }
        return render(request, 'home/pages/samples/change.html', context)

    elif request.method == "POST":
        context = {}
        mem_id = request.POST["mem_id"]
        mem_pw = request.POST["mem_pw"]
        mem_pw2 = request.POST["mem_pw2"]
        mem_name = request.POST["mem_name"]
        mem_pw_crypted = make_password(mem_pw)    # 암호화
    
        # 비밀번호 확인하기
        if mem_pw != mem_pw2:
            context = {}
            context['message'] = "비밀번호 재확인 하십시오"
            return render(request, 'home/pages/samples/change.html', context)
        Members.objects.filter(mem_id = mem_id).update(mem_pw=mem_pw_crypted,mem_name=mem_name
        )
        context['message'] = mem_name + "님 회원가입 수정 되었습니다."
        return redirect('/',context)





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
        # return HTTPResponse(avg)
        return JsonResponse({"results":results},status=200)


def chart_view(request):
    dbCon = psycopg2.connect(dbname="raydb", user="root", password="1234")
    cursor = dbCon.cursor()
    labels = []
    data = []
    with dbCon:
        # 연습
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where m.mem_gender = 'w'")
        queryset = cursor.fetchall()
        for person in queryset:
            labels.append(person[0])
            data.append(person[2])

        # 전체 평균구하기
        cursor.execute("SELECT exam_result, mem_seq FROM t_exam")
        # scorescount = cursor.fetchall().count()
        scores = cursor.fetchall()
        results = []
        num = 0
        cnt = 0
        for i in scores:
            if i[0] != "":
                cnt += 1
                num += float(i[0])
                results.append({
                "examseq":i[1],
                "score":i[0]
                })
            else:
                print('a')
        if num != 0:
            avg = int(num/cnt)
        else:
            avg = 0
        print(avg)
        
        # 남자 중에서 전체 평균구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where m.mem_gender = 'm'")
        menscores = cursor.fetchall()
        num2=0
        cnt2=0
        for i in menscores:
            if i[2] == "":
                pass
            else:
                cnt2 +=1
                num2 += float(i[2])
                results.append({
                "menscore":i[2]
            })
        if num2 != 0:
            manavg = int(num2/cnt2)
        else:
            manavg = 0
        print('남자평균')
        print(manavg)

        # 여자 중에서 전체 평균구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where m.mem_gender = 'w'")
        womenscores = cursor.fetchall()
        num3=0
        cnt3=0
        for i in womenscores:
            if i[2] == "":
                pass
            else:
                cnt3 +=1
                num3 += float(i[2])
                results.append({
                "womanscore":i[2]
            })
        if num3 != 0:
            womanavg = int(num3/cnt3)
        else:
            womanavg = 0
        print('여자평균')
        print(womanavg)




        # 60대 이상중에서 전체 평균구하기
        cursor.execute("SELECT m.mem_id, m.mem_joindate, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)>=60")
        sixscore = cursor.fetchall()
        num4=0
        cnt4=0
        for i in sixscore:
            if i[2] == "":
                pass
            else:
                cnt4 +=1
                num4 += float(i[2])
                results.append({
                "sixscore":i[2]
            })
        if num4 !=0:
            sixavg = int(num4/cnt4)
        else:
            sixavg = 0

        print('60대평균')
        print(sixavg)
        
        # 유저점수
        mem_score=0
        mem_id = request.session.get("m_id","")
        print(mem_id)
        if mem_id != "":

            mem_score = ImgSave.objects.filter(mem_id=mem_id).order_by('-mem_seq').first()
        #print(mem_score)
        #print(results)

        # 전체 치매 남녀 비율 구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id")
        allmw = cursor.fetchall()
        cntmall = 0
        cntwall = 0
        for i in allmw:
            if i[2] == "":
                pass
            elif float(i[2])<20:
                if i[1] == 'w':
                    cntwall +=1
                elif i[1] == 'm':
                    cntmall +=1
        results.append({
            "cntmall":cntmall,
            "cntwall":cntwall
        })
        # 20대 치매 남녀 비율 구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)>=20 and (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)<30;")
        twomw = cursor.fetchall()
        cntmtwo = 0
        cntwtwo = 0
        for i in twomw:
            if i[2] == "":
                pass
            elif float(i[2])<20:
                if i[1] == 'w':
                    cntwtwo +=1
                elif i[1] == 'm':
                    cntmtwo +=1
        # 30대 치매 남녀 비율 구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)>=30 and (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)<40;")
        threemw = cursor.fetchall()
        cntmthree = 0
        cntwthree = 0
        for i in threemw:
            if i[2] == "":
                pass
            elif float(i[2])<20:
                if i[1] == 'w':
                    cntwthree +=1
                elif i[1] == 'm':
                    cntmthree +=1
        # 40대 치매 남녀 비율 구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)>=40 and (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)<50;")
        twomw = cursor.fetchall()
        cntmfour = 0
        cntwfour = 0
        for i in twomw:
            if i[2] == "":
                pass
            elif float(i[2])<20:
                if i[1] == 'w':
                    cntwfour +=1
                elif i[1] == 'm':
                    cntmfour +=1

        # 60대이상 치매의심 남자여자 비율 구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)>=60")
        sixmw = cursor.fetchall()
        num5=0
        cnt5=0
        cntm60=0
        cntw60=0
        for i in sixmw:
            if i[2] == "":
                pass
            elif float(i[2]) < 20:
                cnt5 +=1
                num5 += float(i[2])
                if i[1] == 'w':
                    cntw60 +=1
                    
                elif i[1] == 'm':
                    cntm60 += 1
                    results.append({
                    })
        results.append({
            "cntm60":cntm60,
            "cntw":cntw60
                })
        print('남자',cntm60)
        print('여자',cntw60)
        gender_list = ['Male', 'Female']
        gender_number = [cntm60, cntw60]
        # 치매환자 비율 한번에 보기
        gender_allm = [cntmall,cntm60,cntmtwo,cntmthree,cntmfour]
        gender_allw = [cntwall,cntw60,cntwtwo,cntwthree,cntwfour]

           
    
        context = {
            'labels' : labels,
            'data' : data,
            'results' : results,
            # 전체에서 볼수 있는데이터
            'scores' : scores,
            'menscores' :menscores,
            'womanscore' :womenscores,
            'sixscore' :sixscore,
            # 평균들, 전체평균,남자평균,여자평균,60대평균
            'avg' : avg,
            'manavg': manavg,
            'womanavg':womanavg,
            'sixavg':sixavg,
            # 유저에서 볼수 있는 데이터
            # 현재유저데이터
            'mem_score':mem_score,
            # 60대이상이고 남녀 비율체크데이터
            'cntm60':cntm60,
            'cntw60':cntw60,
            'gender_list':gender_list,
            'gender_number':gender_number,
            'gender_allm':gender_allm,
            'gender_allw':gender_allw,
            'm_id':request.session.get('m_id', ''),
            'm_name':request.session.get('m_name', '')
            }
            # m_id 세션변수 값이 없다면 '' 을 넣어라
    return render(request, "home/index.html", context)

import csv
def csvToModel(request):
    path = "./material/csv/csvplace2.CSV"
    file = open(path)
    reader = csv.reader(file)
    print('----', reader)
    list = []
    for row in reader:
        list.append(PlaceInfo(category=row[0],name=row[1],address=row[2],tel=row[3]))
    PlaceInfo.objects.bulk_create(list)
    return HttpResponse('create model ~~')

from django.core.paginator import Paginator
def place_view(request):
    boards = PlaceInfo.objects.all()
    # boards 페이징 처리
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(boards, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'home/search.html', {'page_obj':page_obj})

from django.shortcuts import render
from django.db.models import Q

# filter 함수의 Q함수: OR조건으로 데이터를 조회하기 위해 사용하는 함수
# objects.filter() 는 특정 조건에 해당하면 객체 출력 .get('kw') 은 kw만 반환
# __icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사. 사용법 "필드명"__icontains = 조건값

def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        products = PlaceInfo.objects.all().filter(
            Q(name__icontains=query) | #이름 검색
            Q(description__icontains=query) #설명 검색
        )
    return render(request, 'home/search2.html', {'query':query, 'products':products})

