from django import forms
from main.models import Article

class ArticleForm(forms.ModelForm):
   # réutilise la classe article en enlevant la date de publication car elle est renseigné automatiquement lors de la création d'un nouvel article
   class Meta:
     model = Article
     exclude = ('publication_date',)