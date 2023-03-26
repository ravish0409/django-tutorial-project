from django import forms

class fun_quiz(forms.Form):
    q1 = "1. What color is your Bugatti?"
    o = [
        ('1', 'a. kala'),
        ('2', 'b. nila'),
        ('3', 'c. pila'),
        ('4', 'd. abhi to nhi hh'),
    ]

    opt= forms.ChoiceField(choices=o,widget=forms.RadioSelect,required=False,label=False)
