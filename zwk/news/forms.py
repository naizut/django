from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
	# commentator = forms.CharField(label='nickname', 
 #                    widget=forms.TextInput(attrs={'placeholder': '昵称'}))
	class Meta:
		model = Comment
		fields = ("commentator", "body",)
		widgets = {
            'commentator': forms.TextInput(attrs={'placeholder': '昵称'}),
            'body': forms.Textarea(
                attrs={'placeholder': '说说你的看法...'}),
        }