from django.shortcuts import render
from .forms import ThingForm

def home(request):
    #new
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = ThingForm()
        # Create a new instance of ThingForm for GET requests or invalid form submissions
    return render(request, 'home.html', {'form': form})
