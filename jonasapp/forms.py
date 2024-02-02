from django import forms
from .models import Post
from .models import Report


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title', 'description', 'image', 'user','pet']
       
       widgets = {
           'title' : forms.TextInput(attrs={
               'class':'bg-white border-gray-100 border-2 p-2 w-64 placeholder-gray-400 rounded',
               'placeholder': 'Enter your topic'
       }),
           'description': forms.Textarea(attrs={
               'class': 'bg-white border-gray-100 border-2 h-32 p-2 w-full placeholder-gray-400', 
               'placeholder': 'Provide Location & description'       
       }),
          'user': forms.Select(attrs={
               'class': 'bg-white border-gray-50 border-2 p-2 w-64 placeholder-gray-400',
       }),
          'pet': forms.Select(attrs={
               'class': 'bg-white border-gray-50 border-2 p-2 w-64 py-2.5 shadow placeholder-gray-400',
       }),
          'image': forms.FileInput(attrs={
               'class': 'file-input-accent bg-white border-white border-2 p-2 w-64 py-2.5',
       })
       }
    
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['location', 'description', 'image', 'post']
        
        widgets = {
            'location': forms.TextInput(attrs={
                'class':'bg-white border-gray-50 border-2 p-2 w-64 placeholder-gray-400 rounded',
                'placeholder': 'Enter your location'
        }),
           'description': forms.Textarea(attrs={
               'class': 'bg-white border-gray-50 border-2 h-32 p-2 w-full placeholder-gray-400', 
               'placeholder': 'Description'  
        }),
           'post': forms.Select(attrs={
               'class': 'bg-white border-gray-50 border-2 p-2 w-64 placeholder-gray-400',     
       }),
           'image': forms.FileInput(attrs={
               'class': 'file-input-accent bg-white border-white border-2 p-2 w-64 py-2.5',
       })
        }
       


        