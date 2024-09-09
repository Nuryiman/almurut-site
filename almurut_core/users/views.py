from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from users.models import CustomUser


class LoginView(TemplateView):
    template_name = 'login.html'


class MakeUserRegistrationView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data["passsword1"]
        password2 = data["passsword2"]

        if password1 == password2:
            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            user = CustomUser.objects.create_user(
                email=email, password=password1,
                first_name=first_name, last_name=last_name
            )
            return render(request, "index.html")
        else:
            pass


class UserRegistrationView(TemplateView):
    template_name = 'register.html'
