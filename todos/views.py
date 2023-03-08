from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST']) # this is a decorator, and its for define the methods below
def task_list(request):
    if request.method == 'GET':
        tasks= Todo.objects.all()
        serializer = TodoSerializer(tasks, many = True) #creating a intance of the serializer,
                                            #tasks will be ready to be serialized to JSON  
        return JsonResponse({'Tasks': serializer.data})
    
    if request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # in this case we will get the data of the user, receveing from the request