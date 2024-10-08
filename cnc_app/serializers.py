from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'designation', 'famille', 'origine', 'quantite', 'emplacement', 'etat', 'code_article']
