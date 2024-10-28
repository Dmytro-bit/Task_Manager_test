from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from users.models import User
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['post'], url_path='add-user')
    def add_user(self, request, pk=None):
        project = self.get_object()
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "Could not find user with this email"}, status=status.HTTP_404_NOT_FOUND)

        if project.users.count() >= 3:
            return Response({"detail": "Project already has 3 users"}, status=status.HTTP_400_BAD_REQUEST)

        project.users.add(user)
        project.save()
        return Response({"detail": "Success"}, status=status.HTTP_200_OK)


class TaskPagination(PageNumberPagination):
    page_size = 5


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

    @action(detail=False, methods=['get'], url_path='by-project')
    def by_project(self, request):
        project_id = request.data.get("project_id")
        email = request.data.get("email")

        try:
            project = Project.objects.get(id=project_id)
            user = User.objects.get(email=email)
        except (Project.DoesNotExist, User.DoesNotExist):
            return Response({"detail": "Project or User not found."}, status=status.HTTP_404_NOT_FOUND)

        if not project.users.filter(id=user.id).exists():
            return Response({"detail": "Denied"}, status=status.HTTP_403_FORBIDDEN)

        tasks = Task.objects.filter(project_id=project_id)
        page = self.paginate_queryset(tasks)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
