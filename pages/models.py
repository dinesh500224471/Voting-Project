from django.db import models

# Model representing a Question
class Question(models.Model):
    # Field for the question text
    question_text = models.CharField(max_length=200)
    # Field for the date the question was published
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


# Model representing a Choice for a Question
class Choice(models.Model):
    # A ForeignKey links each Choice to its corresponding Question.
    # on_delete=models.CASCADE means that if a Question is deleted, all its related Choices will be deleted as well.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Field for the choice text
    choice_text = models.CharField(max_length=200)
    # Field for the number of votes for this choice, with a default value of 0
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
