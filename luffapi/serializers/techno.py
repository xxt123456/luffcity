from  luffapi import models
from  rest_framework import serializers

class TechnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Article
        fields="__all__"