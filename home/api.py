from rest_framework.viewsets import ModelViewSet

from .serializers import MakeSerializer, ModelSerializer, ReviewSerializer
from .models import Make, Model, Review

class MakeViewSet(ModelViewSet):
	queryset = Make.objects.all()
	serializer_class = MakeSerializer

class ModelViewSet(ModelViewSet):
	queryset = Model.objects.all()
	serializer_class = ModelSerializer

class ReviewViewSet(ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer