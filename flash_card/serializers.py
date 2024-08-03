from rest_framework.serializers import ModelSerializer
from .models import FlashCard
class CreateFlashCard(ModelSerializer):
  class Meta:
    model = FlashCard
    fields=('__all__')
    

class UpdateFlashCard(ModelSerializer):
  class Meta:
    model = FlashCard
    fields=('question','answer')
    
    
class ListFlashCard(ModelSerializer):
  class Meta:
    model = FlashCard
    fields=('__all__')
    