from .models import devlogComments
from django import forms

class CommentForm(forms.ModelForm):
	# commentator = forms.CharField(label='nickname', 
 #                    widget=forms.TextInput(attrs={'placeholder': '昵称'}))
	class Meta:
		model = devlogComments
		fields = ("commentator", "body",)
		widgets = {
            'commentator': forms.TextInput(attrs={'placeholder': 'Name'}),
            'body': forms.Textarea(
                attrs={'placeholder': 'Make comments...'}),
        }