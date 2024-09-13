from django.contrib.auth import login
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from users.models import CustomUser


class LoginView(TemplateView):
    template_name = 'login.html'


class MakeUserLoginView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data['email']
        password = data['password']

        user = CustomUser.objects.get(email=email)
        print("пользователь", user)

        correct = user.check_password(password)
        print("коррект равен", correct)

        if correct == True:
            login(request, user)
            return render(request, "login.html", context={'logged_in': True})
        else:
            return render(request, "login.html", context={'logged_in': False})





class MakeUserRegistrationView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data["password1"]
        password2 = data["password2"]

        if password1 == password2:
            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            user = CustomUser.objects.create_user(
                email=email, password=password1,
                first_name=first_name, last_name=last_name
            )
            login(request, user)
            return render(request, "index.html")
        else:
            pass


class UserRegistrationView(TemplateView):
    template_name = 'register.html'
