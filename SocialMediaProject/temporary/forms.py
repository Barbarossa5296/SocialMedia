from django import forms
from .models import Forum


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"
