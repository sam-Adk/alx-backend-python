from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)
from django.db.models.signals import pre_save
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Message already exists
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            # Save the old content in MessageHistory
            MessageHistory.objects.create(message=instance, old_content=old_message.content)
            # Mark the message as edited
            instance.edited = True
@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete all messages sent or received by this user
    instance.sent_messages.all().delete()
    instance.received_messages.all().delete()

    # Delete all notifications for this user
    instance.notification_set.all().delete()

    # MessageHistory related to messages will cascade automatically