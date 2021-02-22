from django import forms
from .models import Thought
from django.utils import timezone

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'thought']
        pub_date = timezone.now()
    # title_text = forms.CharField(max_length=200)
    # thought_text = forms.CharField(max_length=1000)
    # pub_date = forms.DateTimeField()

    # def __str__(self):
    #     return self.thought_text