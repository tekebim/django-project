from django import forms
from todo.models import Task

# Create the form class.
class AddTaskForm(forms.ModelForm):
    content = forms.CharField(label=False, required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'What do you need to do ?', 'class': 'form-control'}))
    # is_done = forms.BooleanField(initial=False)

    class Meta:
        model = Task
        fields = ['content']

# Create the form class.
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'is_done']
        # fields = '__all__'
        # exclude = ['created_date']
