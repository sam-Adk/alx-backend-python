from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted.")
    return redirect('home')
