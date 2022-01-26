from django.shortcuts import render, HttpResponse
# config 에서 settings 받아오기
from config import settings

# python
from datetime import datetime
# models
from master_user.models import WordleRanks

# Create your views here.
def upload(request):

    return


def download(request):
    rank_data = WordleRanks.objects.filter(date=datetime.now()).select_related('user').order_by('user_rank')

    with open('top10.txt', 'w', encoding='utf-8') as txtfile:
        for i in rank_data:
            data = f'{i.user_rank}등 {i.user.user_name}\n'
            txtfile.write(data)

    with open(str(settings.BASE_DIR) + '/top10.txt', 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % 'top10.txt'

        return response