from django import forms
import requests
import json
import random

class fun_quiz(forms.Form):

# Define a function to retrieve quiz questions from the Open Trivia Database API
    category = 18 # Computer Science category
    difficulty = "easy"
    num_questions = 1
    url = f"https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    # print(response)
    data = json.loads(response.text)
    l=data['results'][0]
    q1=l['question']
    out=[q1]
    op=l['incorrect_answers']+[l['correct_answer']]
    o=[]
    random.shuffle(op)
    for i in op:
        o.append((i,i))
    
    out+=[l['correct_answer']]
    opt= forms.ChoiceField(choices=o,widget=forms.RadioSelect,required=False,label=False)
    print(l['correct_answer'])
        

   