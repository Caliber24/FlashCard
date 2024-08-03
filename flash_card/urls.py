from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.CreateFlashCardView.as_view(), name='create_flash_card'),
    path('update/<id>', views.UpdateFlashCardView.as_view(),name='update_flash_card'),
    path('delete/<id>',views.DeleteFlashCardView.as_view(), name='delete_flash_card'),
    path('list/<user_id>',views.ListFlashCardView.as_view(), name='list_flash_card'),
]

