from rest_framework import serializers

from .models import Make, Model, Review


class ReviewSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Review
		fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
	##review = ReviewSerializer(many=True)

	class Meta:
		model = Model
		fields = '__all__'

class MakeSerializer(serializers.ModelSerializer):
	model = ModelSerializer(many=True)

	class Meta:
		model = Make
		fields = '__all__'