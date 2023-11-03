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
     
    # 모든 경우의 수 
    # 1. GET: form을 만들어서 html문서를 사용자에게 리턴 (# 1~4번)
    # 2-1. POST invalid data: 검증에 성공한 데이터 부분만 살려서 form을 만들어서 html문서를 사용자에게 리턴 (# 5~9번)
    # 2-2. POST valid data: DB에 데이터 저장 후 index페이지로 redirect (# 10~끝번)

    # 5. POST요청 (데이터가 잘못들어온 경우)
    # 10. POST요청 (데이터가 잘 들어온 경우)
    # POST방식이면: form을 통해 데이터가 들어왔다는 얘기. 전에 배운 create/ (사용자가 제출한 데이터를 저장하는 기능) 역할
    if request.method == 'POST':
        # 6. 사용자가 입력한 정보(invalid)를 담아서 form 생성
        # 11. 사용자가 입력한 정보(valid)를 담아서 form 생성
        # 어제 봤던 POST라는 딕셔너리를 넣어주는 것, 사용자가 입력한 데이터를 넣어서 ArticleForm 클래스를 활용해 html코드를 만들어서 form에 할당
        # request.POST = 사용자가 입력한 데이터
        form = ArticleForm(request.POST)

        # 7. form을 검증(실패)
        # 12. form을 검증(성공)
        # 사용자가 넣은 입력값은 request.POST 값이 유효한지 여부를 점검. 
        # 사용자가 올바르지 않은 데이터를 입력할 시 이를 걸러줌.
        # 저장한 정보는 article에 저장 >> 저장된 article의 id값을 이용해 그리 이동가능.(오늘은 안 함)
        if form.is_valid():
            # 13. form을 저장 (DB에 반영)
            article = form.save()
            # 14. index페이지로 redirect
            return redirect('articles:index')
        
        # 사용자가 넣은 입력값이 유효하지 않은 경우
        # else:
            # form = ArticleForm()

            # context = {
            #     # 여기서 form은 앞서 할당한 form. => 사용자가 입력해둔 데이터를 가져온 것이므로, 쓰던 내용 남아있음.
            #     'form': form,
            # }
            # return render(request, 'create.html', context)
            # pass

    # 1. GET 요청
    # GET방식이면: 전에 배운 new/ (빈 인풋 도화지를 제공하는 기능) 역할
    else:
        # 2. 비어있는 form을 만들어서
        form = ArticleForm()

    # 3. context dict에 담고
    # 8. 검증에 실패한 form을 contex dict에 담고
    context = {
        'form': form
    }

    # 4. create.html을 랜더링
    # 9. create.html을 랜더링
    return render(request, 'create.html', context)


def delete(request, id):
    # Article이라는 클래스 테이블의 id 컬럼이 여기서의 파란글씨 id
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')


def update(request, id):

    article = Article.objects.get(id=id)

    # 제출버튼 누른 후
    if request.method == 'POST':
        # (첫째 인자: (data=) 생략. 새롭게 입력한 데이터 / 둘째인자: 과거의 데이터) 순서로 2개의 인자를 적어야 함
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        
    # update 버튼 누른 후
    else:
        # 빈 종이 만들기
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'update.html', context)