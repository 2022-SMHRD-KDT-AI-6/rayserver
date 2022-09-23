from django.shortcuts import render
from board.models import Writing

# Create your views here.
def list(request):
    writing_list = Writing.objects.all()  # 객체들을 다 불러온다.
    writing_list = writing_list.order_by('-create_date')  # 만들어진 시간의 역으로 정렬한다.

    context = {'writing_list':writing_list,  # writing_list라는 키 안에 writing_list를 담는다.
               }
    return render(request, 'board/list.html', context)

def create(request):
    from django.shortcuts import redirect
    from .forms import WritingForm
    from django.utils import timezone  # 시간입력용
    if request.method == 'POST':  # 포스트로 요청이 들어온다면... 글을 올리는 기능.
        form = WritingForm(request.POST)  # 폼을 불러와 내용입력을 받는다.
        if form.is_valid():  # 폼에서 에러처리. 문제가 없으면 다음으로 진행.
            writing = form.save(commit=False)  # commit=False는 저장을 잠시 미루기 위함.(입력받는 값이 아닌, view에서 다른 값을 지정하기 위해)
            writing.mem_id = request.user  # 추가한 속성 author 적용
            writing.create_date = timezone.now()  #현재 작성일시 자동저장
            writing.save()
            return redirect('board:list')  #작성이 끝나면 목록화면으로 보낸다.
    else:  #포스트 요청이 아니라면.. form으로 넘겨 내용을 작성하게 한다.
        form = WritingForm()
    context = {'form': form}  # 폼에서 오류가 있으면 오류의 내용을 담아 create.html로 넘긴다.
    # 없으면 그냥 form 작성을 위한 객체를 넘긴다.
    return render(request, 'board/create.html', context)

from rest_framework import viewsets

from .models import Post1
from .models import Comment
from .serializers import PostSerializer
from .serializers import CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post1.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer