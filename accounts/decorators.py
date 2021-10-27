from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def verified(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if request.user.verified:
             return function(request, *args, **kwargs)
        else:
            messages.error(request, "Your account hasn't been verified")
            return redirect("accounts:verify")

  return wrap