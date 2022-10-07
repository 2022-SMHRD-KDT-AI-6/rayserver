from contextlib import redirect_stderr
from django.shortcuts import render
from predict.models import ImgSave
from django.http import JsonResponse
import psycopg2
from rest_framework.views import APIView
from rest_framework.response import Response    
# Create your views here.
from member.models import Members
from django.views import View
from datetime import datetime

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
        return JsonResponse({"results":results},status=200)


def chart_bar3(request):
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
        cursor.execute("SELECT exam_result FROM t_exam")
        # scorescount = cursor.fetchall().count()
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
        manavg = int(num2/cnt2)
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
        womanavg = int(num3/cnt3)
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
        sixavg = int(num4/cnt4)
        print('60대평균')
        print(sixavg)
        
        # 유저점수
        mem_id = request.session.get("m_id")
        print(mem_id)
        mem_score = ImgSave.objects.filter(mem_id=mem_id).order_by('-mem_seq')[0]
        print(mem_score)
        print(results)

        # 60대이상 치매의심 남자여자 비율 구하기
        cursor.execute("SELECT m.mem_id, m.mem_gender, e.exam_result, (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1) as age  FROM t_member as m join t_exam as e on m.mem_id = e.mem_id where (to_char(now(),'YYYY')::int-substring(m.mem_birth::varchar,1,4)::int+1)>=60")
        sixmw = cursor.fetchall()
        num5=0
        cnt5=0
        cntm=0
        cntw=0
        for i in sixmw:
            if i[2] == "":
                pass
            elif float(i[2]) < 20:
                cnt5 +=1
                num5 += float(i[2])
                if i[1] == 'w':
                    cntw +=1
                    
                elif i[1] == 'm':
                    cntm += 1
                    results.append({
                    })
        results.append({
            "cntm":cntm,
            "cntw":cntw
                })
        print('남자',cntm)
        print('여자',cntw)
        gender_list = ['Male', 'Female']
        gender_number = [cntm, cntw]
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
            'cntm':cntm,
            'cntw':cntw,
            'gender_list':gender_list,
            'gender_number':gender_number
            }
    return render(request, "chart/chart_example.html", context)