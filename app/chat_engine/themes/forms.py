from django.forms import ModelForm
from . models import Theme

class ThemeForm(ModelForm):
	class Meta:
		model = Theme
		fields = '__all__'
		pass