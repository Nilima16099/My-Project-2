from django import forms
from todo.models import Todo,Contact
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields={"title","name","email","mobile","description"}


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","email","mobile","message"}