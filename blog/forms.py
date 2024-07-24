from django.forms import ModelForm
from django import forms
from blog.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # def save(self, commit=True):
    #     instance = super(BlogForm, self).save(commit=False)
    #     instance.title = self.cleaned_data['title']
    #     instance.description = self.cleaned_data['description']
    #     instance.image = self.cleaned_data['image']
    #     if commit:
    #         instance.save()
    #         return instance
