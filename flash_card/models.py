from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class FlashCard(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
  question = models.TextField(verbose_name='سوال')
  answer = models.TextField(verbose_name='پاسخ')
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now_add=True)
  class Meta:
      verbose_name = ("فلش کارت")
      verbose_name_plural = ("فلش کارت‌ها")

  def __str__(self):
      return f"{self.question[0:10]}..."


  