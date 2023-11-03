from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def create(request):
     
    # 1.
    # POST방식이면: form을 통해 데이터가 들어왔다는 얘기. 전에 배운 create/ (사용자가 제출한 데이터를 저장하는 기능) 역할
    if request.method == 'POST':
        # 어제 봤던 POST라는 딕셔너리를 넣어주는 것, 사용자가 입력한 데이터를 넣어서 ArticleForm 클래스를 활용해 html코드를 만들어서 form에 할당
        # request.POST = 사용자가 입력한 데이터
        form = ArticleForm(request.POST)

        # 사용자가 넣은 입력값은 request.POST 값이 유효한지 여부를 점검. 
        # 사용자가 올바르지 않은 데이터를 입력할 시 이를 걸러줌.
        # 저장한 정보는 article에 저장 >> 저장된 article의 id값을 이용해 그리 이동가능.(오늘은 안 함)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
        
        # 사용자가 넣은 입력값이 유효하지 않은 경우
        else:
            context = {
                # 여기서 form은 앞서 할당한 form. => 사용자가 입력해둔 데이터를 가져온 것이므로, 쓰던 내용 남아있음.
                'form': form,
            }
            return render(request, 'create.html', context)

    # 2.
    # GET방식이면: 전에 배운 new/ (빈 인풋 도화지를 제공하는 기능) 역할
    else:
        form = ArticleForm()

        context = {
            'form': form
        }

    return render(request, 'create.html', context)