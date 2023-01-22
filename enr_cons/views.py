
from django.shortcuts import render,redirect
from .models import Participant
from .forms import FormParticipant

def enreg(request):
    form = FormParticipant()
    if request.method == 'POST':
        form = FormParticipant(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('consultation/')
            except:
                pass
    context = {'form':form}    
    return render(request, 'enreg.html', context)


def consult(request):
    Participants = Participant.objects.all()
    context = {"LesParticipant":Participants}
    return render(request, 'consult.html', context)
 