from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from .models import *

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']


class ExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['subject', 'question', 'mc1', 'mc2', 'mc3', 'mc4', 'mc5', 'correct']
