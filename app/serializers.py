from rest_framework import serializers
from app.models import Task

# Serializers define the API representation.

class TaskSerializers(serializers.ModelSerializer):  
       
    class Meta:
        model = Task
        fields = ['title'] 
