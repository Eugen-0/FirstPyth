from django.shortcuts import render

# Create your views here.
from.models import Article

def index (request):
    articles = Article.objects.all()
    return render(request,'index.html', {'articles': artticles})