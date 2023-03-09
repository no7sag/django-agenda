from django.forms import ModelForm, DateInput
from .models import ToDo

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        widgets = {
            'end_date': DateInput(attrs={'type': 'date'})
        }