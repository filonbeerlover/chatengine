from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
	title = models.CharField(max_length=250, blank=False,null=False,verbose_name='Наименование')
	description = models.TextField(blank=True,verbose_name='Описание')
	author = models.ForeignKey(User,verbose_name="Автор",on_delete=models.PROTECT)
	pub_date = models.DateTimeField(auto_now_add=True,verbose_name="Дата публикации")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Тема конференции'
		verbose_name_plural = 'Темы конференции'
		ordering = ['-pub_date','author']