from django.views.decorators.cache import cache_page
from django.shortcuts import render
from messaging.models import Message

@cache_page(60)  # Cache for 60 seconds
def conversation_view(request, user_id):
    messages = Message.objects.filter(receiver_id=user_id) \
        .select_related('sender', 'receiver') \
        .prefetch_related('replies')
    return render(request, 'messaging/conversation.html', {'messages': messages})
