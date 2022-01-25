from django.shortcuts import render, redirect, HttpResponse
from .models import wordle_answers, wordle_dayRanks, wordle_ranks, wordle_users
from django.utils import timezone
from datetime import datetime

# Create your views here.
# 화면 첫 진입 시에 사용할 view
def main(request):
    try:
        a = wordle_answers.objects.get(date=timezone.now())
        data = a
    except:
        data =''

    condata = wordle_ranks.objects.filter(date = datetime.now()).select_related('user').order_by('user_rank')
    return render(request, 'master_user/main.html', {'data': data, 'condata': condata})

def edit_answer(request):
    return render(request, 'master_user/edit.html')

# 상위 10명 가져와서 저장하는 view
# day_rank에서 10개 추출 -> rank에 10개 입력 -> day_rank 비우기
def get_top(request):
    #wordle_dayRanks(count=5, user_id=2, create_at=timezone.now()).save()
    # 제출한 시간이 최신 순서대로, 시간이 같다면 카운트가 적은 순서대로 탑 10
    a = wordle_dayRanks.objects.all().order_by('count','create_at')[:10]

    # 10개밖에 안되니까 반복문 돌려서 필요한 정보 wordl_ranks에 입력
    for n, i in enumerate(a):
        wordle_ranks(user_rank=n+1, date=i.create_at, user_id=i.user_id).save()

    # dayRanks 의 전체 데이터 삭제
    wordle_dayRanks.objects.all().delete()
    return redirect('/master/main')


# 오늘자 정답 입력시 동작할 view
def input_answer(request):
    a = request.GET.get('answer')
    try:
        m = wordle_answers(answer=a)
        m.date = timezone.now()
        m.save()
        return redirect('/master/main')
    except:
        answer = '등록에 실패했습니다.'

    return render(request, 'master_user/main.html', {'answer': answer})

# 더미 데이터 생성
# 나중에 필히 지울것!!!
def dummy(request):
    wordle_dayRanks(count=5, user_id=2, create_at=timezone.now()).save()
    wordle_dayRanks(count=2, user_id=1, create_at=timezone.now()).save()
    wordle_dayRanks(count=6, user_id=2, create_at=timezone.now()).save()
    wordle_dayRanks(count=4, user_id=1, create_at=timezone.now()).save()
    wordle_dayRanks(count=1, user_id=2, create_at=timezone.now()).save()
    wordle_dayRanks(count=3, user_id=1, create_at=timezone.now()).save()

    return HttpResponse('<p>성공</p>')