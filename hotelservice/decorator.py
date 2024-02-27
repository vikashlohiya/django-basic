from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def custom_permission_decorator(permission_codename,return_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.has_perm(permission_codename):
                return view_func(request, *args, **kwargs)
            else:
                if return_url:
                    # Redirect to the specified URL
                    return redirect(return_url)
                else:
                    # If no redirect URL is provided, redirect to a default route
                    return redirect(return_url)
        return wrapper
    return decorator