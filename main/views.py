from django.shortcuts import render
from django.shortcuts import redirect  
from django.utils.translation import gettext_lazy as _
from main.models import Article
from main.forms import ArticleForm
from django.http import JsonResponse
from multilang_site.chatbot_service import get_gpt_response

# les vues des différentes pages de l'application qui permettent d'enregistrer en bdd et également de les récupérer pour ensuite les afficher
def article_list(request):
   # récupère tous les articles
   articles = Article.objects.all()
   return render(request,
           'main/article_list.html',
           {'articles': articles})

def article_detail(request, id):
   # récupère un article spécifique
   article = Article.objects.get(id=id)
   return render(request,
           'main/article_detail.html',
           {'article': article})

def article_create(request):
    if request.method == 'POST':
        # utilise le formulaire d'article pour enregistrer en bdd
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article-detail', article.id)

    else:
        form = ArticleForm()

    return render(request,
            'main/article_create.html',
            {'form': form})

def article_update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-detail', article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request,
                'main/article_update.html',
                {'form': form})

def article_delete(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':

        article.delete()

        return redirect('article-list')

    return render(request,
                    'main/article_delete.html',
                    {'article': article})

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        bot_response = get_gpt_response(user_message)
        return JsonResponse({'response': bot_response})
    return render(request, 'main/chatbot.html')