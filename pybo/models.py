from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Question(models.Model):
    class Category(models.TextChoices):
        QUESTION_PRODUCT = 'PRODUCT', _('question_product')
        QUESTION_DELIVERY = 'DELIVERY', _('question_delievery')
        QUESTION_REFUND = 'REFUND', _('question_refund')

    class Importance(models.IntegerChoices):
        EMERGENCY = 1
        HIGH = 2
        NORMAL = 3
        LOW = 4
        TRIVIAL = 5

    subject = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(choices=Category.choices, max_length=10)
    importance = models.IntegerField(choices=Importance.choices)
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
