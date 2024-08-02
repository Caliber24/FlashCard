from django.db import models

# Create your models here.

class FlashCard(models.Model):
  question = models.TextField(verbose_name='سوال')
  answer = models.TextField(verbose_name='پاسخ')
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now_add=True)
  class Meta:
      verbose_name = ("فلش کارت")
      verbose_name_plural = ("فلش کارت‌ها")

  def __str__(self):
      return f"{self.question[0:10]}..."


  