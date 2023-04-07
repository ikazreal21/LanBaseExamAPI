from django.db import models
from django.contrib.auth.models import User
from import_export import resources


class Questions(models.Model):
    subject = models.CharField(max_length=250)
    question = models.TextField()
    mc1 = models.CharField(max_length=255)
    mc2 = models.CharField(max_length=255)
    mc3 = models.CharField(max_length=255)
    mc4 = models.CharField(max_length=255)
    mc5 = models.CharField(max_length=255)
    correct = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.subject} || {self.correct}'


class QuestionsResources(resources.ModelResource):

    class Meta:
        model = Questions
        import_id_fields = ["question"]
        skip_unchanged = True
        use_bulk = True