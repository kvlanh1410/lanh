from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
# Create your views here.
from .form import NameForm

# def band_listing(request):
#     """A view of all bands."""
#     bands = models.Band.objects.all()
#     return render(request, 'polls/band_listing.html', {'bands': bands})
#     # return HttpResponse("Hello, world. You're at the polls index.")
# def band_detail(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def band_search(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def get_name(request):
    if request.method == 'POST':
        form=NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('Thanks')
    else:
        form=NameForm()
    return render(request, 'polls/name.html', {'form': form})
# def home_view(request):
#     print(request.GET)
#     return render(request, "polls/form.html")
