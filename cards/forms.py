# cards/forms.py

from django import forms

class GPTCreateForm(forms.Form):
    TOPIC_CHOICES = (
        ('Phonetics', 'Phonetics'),
        ('Phonology', 'Phonology'),
        ('Morphology', 'Morphology'),
        ('Syntax', 'Syntax'),
        ('Semantics', 'Semantics'),
        ('Pragmatics', 'Pragmatics'),
    )
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    number_of_cards = forms.IntegerField(min_value=0)


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)