from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskCreate(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskList(APIView):
    def get(self, request):
        todos = Task.objects.all()
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data)

class TaskDetail(APIView):
    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, id):
        todo = self.get_object(id)
        serializer = TaskSerializer(todo)
        return Response(serializer.data)

class TaskUpdate(APIView):
    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            raise Http404

    def put(self, request, id):
        todo = self.get_object(id)
        serializer = TaskSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDelete(APIView):
    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        todo = self.get_object(id)
        Task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)