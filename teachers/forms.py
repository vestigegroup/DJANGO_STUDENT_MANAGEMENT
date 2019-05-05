from django import forms


class AddTeacherForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'teacher name'
    }))
    teacher_pin = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'enter unique id'
    }))
    designation = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    joined = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'yyyy-mm-dd'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))