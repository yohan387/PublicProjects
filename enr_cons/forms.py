from django.forms import ModelForm
from .models import Participant

class FormParticipant(ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'