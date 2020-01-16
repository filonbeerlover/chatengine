from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import ThemeForm
from user.models import Profile
from . models import Theme



class ThemesList(ListView):	
	template_name = 'themes/themes.html'
	model = Theme


class ThemeCreate(CreateView):
	template_name = 'themes/create.html'
	form_class = ThemeForm
	success_url = reverse_lazy('themes:themes_list') 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		teacher_profiles = Profile.objects.filter(is_teacher=True).values('user')
		teachers_list = list()
		for teacher_profile in teacher_profiles:
			teachers_list.append(teacher_profile.get('user'))
		teacher_users = User.objects.filter(pk__in=teachers_list)
		context['author']=teacher_users
		return context

class ThemeDelete(DeleteView):
	template_name = 'themes/delete.html'
	model = Theme
	success_url = reverse_lazy('themes:themes_list')

class ThemeUpdate(UpdateView):
	template_name = 'themes/create.html'
	model = Theme
	fields = ['title','description']
	success_url = reverse_lazy('themes:themes_list')
	
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	theme = get_object_or_404(Theme,pk = context['id'])
	# 	context['object'] = theme
	# 	return context

# class ThemeDelete(View):
# 	template_name = 'themes/delete.html'
# 	def get(self,request,id):
# 		theme = Theme.objects.get(pk__iexact=id)
# 		return render(request,'themes/delete.html',context={'theme':theme})

# 	def post(self,request,id):
# 		theme = Theme.objects.get(pk__iexact=id)
# 		theme.delete()
# 		return redirect(reverse_lazy('themes:themes_list'))