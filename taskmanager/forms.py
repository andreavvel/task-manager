from django import forms
from .models import Category, Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'category']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
