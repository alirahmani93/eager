from django.shortcuts import render
import json
# Create your views here.
from django.core.management.base import BaseCommand, CommandError
from .models import Like
from rabbit_mq.rabbit.counsumer import consumer
from rabbit_mq.rabbit.producer import producer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AbstractUser


class UserViewSet(ModelViewSet):
    queryset = AbstractUser.objects.all()
    serializer_class = None

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        respone = super(UserViewSet, self).destroy(request, *args, **kwargs)
        producer.produce(
            exchange="user",
            body={"user_id": user.id},
            routing_key="user.deleted"
        )
        return respone


class ConsumerUserDelete(BaseCommand):
    help = "Consumes user delete message from RabbitMQ"

    def _callback(self, channel, method, priority, body):
        payload = json.loads(body)
        user_id = payload.get("user_id")
        if user_id:
            likes = Like.objects.filter(user_id=user_id)
            likes.delete()

    def handle(self, *args, **options):
        consumer.consume(
            exchange="users",
            queue_name="user-delete",
            routing_key="user.deleted",
            callback=self._callback
        )
