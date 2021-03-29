from .models import Task
from .serializer import TaskSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.http.response import HttpResponse
from django.core.mail import send_mail
from . import tasks
from django.shortcuts import get_object_or_404


class TaskList(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        query = Task.objects.all()
        if not self.request.is_admin:
            return query.filter(owner=self.request.user)
        return query


def index(request):
    msg = tasks.send_task_mail.delay('sadrakhamoshi7@gmail.com')
    return HttpResponse(msg)
