from  luffapi import models
from  rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields="__all__"

