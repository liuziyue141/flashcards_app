# cards/models.py

from django.db import models

NUM_BOXES = 3
#BOXES = range(1, NUM_BOXES + 1)
BOX_CHOICES = [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
]

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
    box = models.CharField(
        max_length=10,
        choices=BOX_CHOICES,
        default=BOX_CHOICES[0][0],
    )
    topic = models.CharField(
        max_length=20, 
        choices=TOPIC_CHOICES,
        default=TOPIC_CHOICES[0][0],
    )
    date_created = models.DateTimeField(auto_now_add=True)
    def move(self, solved):
        if solved:
            if self.box == 'Hard':
                new_box = 'Medium'
            elif self.box == 'Medium':
                new_box = 'Easy'
            else:  # 'Easy' remains the same
                new_box = 'Easy'
        else:  # If not solved, everything goes to 'Hard'
            new_box = 'Hard'
        self.box = new_box
        self.save()

        return self
    def __str__(self):
        return self.question