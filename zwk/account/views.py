import functools
import warnings
from django.contrib import auth

from .forms import AuthenticationForm, RegistrationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, deprecate_current_app
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash, authenticate, login
)
from django.utils.deprecation import (
    RemovedInDjango20Warning, RemovedInDjango21Warning,
)

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=user_form.cleaned_data['username'],
            password=user_form.cleaned_data['password'])
            auth.login(request, user) 
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/dev_log/')
        else:
            return HttpResponse('注册失败,请检查输入格式.')
    else:
        user_form = RegistrationForm()
        return render(request, 'account/register.html', {'form': user_form, 'next': redirect_to})

@deprecate_current_app
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=False):
    warnings.warn(
        'The login() view is superseded by the class-based LoginView().',
        RemovedInDjango21Warning, stacklevel=2
    )
    return LoginView.as_view(
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        form_class=authentication_form,
        extra_context=extra_context,
        redirect_authenticated_user=redirect_authenticated_user,
    )(request)