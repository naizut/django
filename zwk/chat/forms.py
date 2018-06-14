from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
	# commentator = forms.CharField(label='nickname', 
 #                    widget=forms.TextInput(attrs={'placeholder': '昵称'}))
	class Meta:
		model = Chat
		fields = ("chatter", "body",)
		widgets = {
            'chatter': forms.TextInput(attrs={'placeholder': '昵称'}),
            'body': forms.Textarea(
                attrs={'placeholder': '对博主说些什么吧'}),
        }