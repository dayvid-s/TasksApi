# serializers Serialization is the process of transforming data into a format that can
#be stored or transmitted and then reconstructed. It is used in all
#parts of application development, or when we are storing data in a database
#in memory or by converting them to files.

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todo
        fields= ['id', 'task', 'description']

