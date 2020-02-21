from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from . forms import ThemeForm
from user.models import Profile
from . models import Theme


class ThemesList(ListView):	
	template_name = 'themes/themes.html'
	model = Theme

class ThemeCreate(UserPassesTestMixin,CreateView):
	template_name = 'themes/create.html'
	form_class = ThemeForm
	success_url = reverse_lazy('themes:themes_list') 
	raise_exception = True

	def test_func(self):
		return not self.request.user.is_anonymous and self.request.user.profile.is_teacher

class ThemeDelete(UserPassesTestMixin,DeleteView):
	template_name = 'themes/delete.html'
	model = Theme
	success_url = reverse_lazy('themes:themes_list')
	raise_exception = True

	def test_func(self):
		return not self.request.user.is_anonymous and self.request.user.profile.is_teacher

class ThemeUpdate(UserPassesTestMixin,UpdateView):
	template_name = 'themes/create.html'
	model = Theme
	fields = ['title','description']
	success_url = reverse_lazy('themes:themes_list')
	raise_exception = True

	def test_func(self):
		return not self.request.user.is_anonymous and self.request.user.profile.is_teacher