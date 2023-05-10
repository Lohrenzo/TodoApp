from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def send_message(sender, receiver, body):
        # Sender Message Function
        sender_message = Message(
            user = sender,
            sender = sender,
            receiver = receiver,
            body = body,
            is_read = True
        )
        sender_message.save()

        # Receiver Message Function
        receiver_message = Message(
            user = receiver,
            sender = sender,
            receiver = sender,
            body = body,
            is_read = True
        )
        receiver_message.save()

        return sender_message

    def get_message(user):
        users = []
        messages = Message.objects.filter(user = user).values("receiver").annotate(last = Max("date")).order_by("-last")

        for message in messages:
            users.append(
                {
                    "user": User.objects.get(pk = message["receiver"]),
                    "last": message["last"],
                    "unread": Message.objects.filter(user = user, receiver_id = message["receiver"], is_read = False).count()
                }
            )
        return users