# cards/models.py

from django.db import models

NUM_BOXES = 3
BOXES = range(1, NUM_BOXES + 1)
TOPIC_CHOICES = (
    ('Phonetics', 'Phonetics'),
    ('Phonology', 'Phonology'),
    ('Morphology', 'Morphology'),
    ('Syntax', 'Syntax'),
    ('Semantics', 'Semantics'),
    ('Pragmatics', 'Pragmatics'),
)

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    topic = models.CharField(
        max_length=20, 
        choices=TOPIC_CHOICES,
        default=TOPIC_CHOICES[0][0],
    )
    date_created = models.DateTimeField(auto_now_add=True)
    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self
    def __str__(self):
        return self.question