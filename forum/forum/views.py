from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings

from posts.models import Post
from .forms import LoginForm, RegisterForm
from posts.forms import PostForm


class HomeView(View):

	def dispatch(self, request):
		User = request.user
		form = PostForm(request.POST or None)
		
		if request.user.is_authenticated:
			if form.is_valid():
				print(form.cleaned_data)
				body = form.cleaned_data.get("body")
				user = User

				new_post = Post(body=body, user=user)
				new_post.save()

				return redirect("/")

		post_list = Post.objects.all().order_by('-datetime')

		context = {
	        "form": form,
	        "post_list": post_list
	    }

		return render(request, "home_page.html", context)


class LoginView(View):

	def dispatch(self, request):
		form = LoginForm(request.POST or None)
		context = {
	        "form": form
	    }
		
		if form.is_valid():
			print(form.cleaned_data)
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("/")
			else:
				print("Error")

		return render(request, "login_page.html", context)


class RegisterView(View):
	
	def dispatch(self, request):
		User = get_user_model()
		form = RegisterForm(request.POST or None)
		context = {
		    "form": form
		}

		if form.is_valid():
		    username  = form.cleaned_data.get("username")
		    # email  = form.cleaned_data.get("email")
		    password  = form.cleaned_data.get("password")
		    new_user  = User.objects.create_user(username=username, password=password)

		    if new_user is not None:
		    	login(request, new_user)
		    	return redirect("/")
		    else:
		    	print("Error")


		return render(request, "register_page.html", context)