from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        designation = request.data.get('designation')
        famille = request.data.get('famille')
        origine = request.data.get('origine')
        quantite = request.data.get('quantite')

        if not designation or not famille or not origine or not quantite:
            return Response({'error': 'Tous les champs doivent être remplis.'}, status=status.HTTP_400_BAD_REQUEST)

        # Vérifie que la famille est l'une des options valides
        valid_families = dict(Article.FAMILLE_CHOICES).keys()
        if famille not in valid_families:
            return Response({'error': 'Famille non valide. Options disponibles : MI, MB, MM, EM.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            quantite = int(quantite)
            if quantite <= 0: 
                return Response({'error': 'La quantité doit être un nombre entier positif.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'La quantité doit être un nombre entier.'}, status=status.HTTP_400_BAD_REQUEST)

        articles = []
        for _ in range(quantite):
            article = Article(
                designation=designation,
                famille=famille,
                origine=origine,
                quantite=1, 
            )
            articles.append(article)

        Article.objects.bulk_create(articles)

        created_articles = ArticleSerializer(articles, many=True).data

        return Response({'message': f'{quantite} articles créés', 'articles': created_articles}, status=status.HTTP_201_CREATED)
