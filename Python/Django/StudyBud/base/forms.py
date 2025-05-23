from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']
        # Ou
        # fields = '__all__'
        # exclude = ['host', 'participants']
