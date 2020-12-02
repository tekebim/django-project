from django import forms
from todo.models import Task

# Create the form class.
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'is_done']

    def edit_task(self):
        # send email using the self.cleaned_data dictionary
        pass
