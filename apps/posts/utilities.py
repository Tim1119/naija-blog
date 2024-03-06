from posts.models import Article
from django.db.models import Max
import random


def get_random3():
    max_id = Article.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        random_list = []
        pk = random.randint(1, max_id)
        for i in range(6):
            random_list.append(i)
        article = Article.objects.filter(id__in=random_list).first()
        if article:
            return article
