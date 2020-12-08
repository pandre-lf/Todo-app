from rest_framework import serializers
from .models import TodoTask


# Serializa a classe TodoTask
class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = '__all__'
