from django.db import models
from django.utils.translation import gettext_lazy as _

# modèle de la classe article qui sera enregistré en bdd avec les différents champs titre, contenu, date de publication
class Article(models.Model):
    title = models.fields.CharField(_('title'), max_length=100)
    content = models.fields.CharField(_('content'), max_length=1000)
    publication_date = models.fields.DateTimeField(_('publication date'), auto_now_add=True)