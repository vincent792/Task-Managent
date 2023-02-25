from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description','price', 'broker', 'deadline', 'paid', 'completed')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'broker': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Broker'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control' ,'type':'date'}),
            'paid': forms.CheckboxInput(attrs={'class': 'form-check-input form-check-centered'}),            
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input form-check-centered'}),
        }
 
