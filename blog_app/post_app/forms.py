from django import forms

from .models import Comments

class CreateCommentForm(forms.ModelForm):
    
    content = forms.CharField(widget=forms.Textarea(attrs={"id":"content", "placeholder":"Enter comment"}))

    class Meta:
        model = Comments
        fields = ["content"]