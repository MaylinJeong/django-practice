from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime


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
    importance = models.IntegerField(choices=Importance.choices, default=Importance.NORMAL)
    create_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def attached_file_path(self, filename):
        dirname = datetime.datetime.now().strftime(str('uploads/%Y/%m/%d'))
        path = dirname + '/q_{0}/{1}'.format(self.id, filename)
        return path

    attached_file = models.FileField(upload_to=attached_file_path, blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
