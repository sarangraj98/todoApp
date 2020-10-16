from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=50,
    widget = forms.TextInput(attrs={'placeholder':'Enter todo e.g. Wash my car','type':'text'})
    )
