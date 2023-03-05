from .models import Message, Testimony
from django import forms


class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            "aria-label ": "Sizing example input",
            "aria-describedby": "inputGroup-sizing-sm",

        }

    )
    )

    location = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            "aria-label ": "Sizing example input",
            "aria-describedby": "inputGroup-sizing-sm",

        }
    ))

    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'textarea',
            'class': 'form-control',
            "id": "floatingTextarea2",
            "style": "height: 100px",

        }
    ))

    class Meta:
        model = Message
        fields = '__all__'


class TestimonyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
        }
    ))

    tel = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'id': 'exampleFormControlInput1',
        }
    ))

    testimony = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'id': 'exampleFormControlTextarea1',
            'rows': '5',
            "style": "height: 100px",
        }
    ))

    class Meta:
        model = Testimony
        fields = '__all__'
