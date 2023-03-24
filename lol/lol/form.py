from django import forms

class user(forms.Form):
    n1 = forms.CharField(required=False,label='num1')
    o = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
    ]

    opt= forms.ChoiceField(choices=o,label='opt',widget=forms.Select,required=False)
    n2 = forms.CharField(label='num2',required=False)
    
