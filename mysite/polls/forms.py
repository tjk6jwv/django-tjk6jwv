from django import forms
from .models import Thought
from django.utils import timezone

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'thought']
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'thought': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
			}
    # title_text = forms.CharField(max_length=200)
    # thought_text = forms.CharField(max_length=1000)
    # pub_date = forms.DateTimeField()

    # def __str__(self):
    #     return self.thought_text