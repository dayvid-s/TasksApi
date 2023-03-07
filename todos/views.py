from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer


def task_list(request):
    #get all the tasks
    #serialize all the tasks
    #return the tasks in json format
    tasks= Todo.objects.all()
    serializer = TodoSerializer(tasks, many = True) #creating a intance of the serializer,
                                        #tasks will be ready to be serialized to JSON  
    return JsonResponse(serializer.data, safe= False)