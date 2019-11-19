from django.shortcuts import get_object_or_404

from rest_framework.response import Response  #  JSON 응답 생성기
from rest_framework.decorators import api_view  # require_methods

# from rest_framework.permissions import IsAuthenticated  # login_required
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication  # login via JWT

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

# @api_view(['GET'])
# def todo_list(request):
#     serializer = TodoSerializer



@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        # serializer.data => { 'id': 1, 'user_id': 1, 'title': '밥먹기', 'completed': false }
        return Response(serializer.data)
    
    return Response(status=400, data=serializer.errors)
    
@api_view(['PATCH', 'DELETE'])
def update_delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'PATCH':
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400,)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)