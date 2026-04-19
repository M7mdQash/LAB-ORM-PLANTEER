from django.shortcuts import render
app_name = "plants"

#TODO: make the details view be here
# Create your views here.
def create_view(request):
    return render(request, 'plants/create.html')

def update_view(request):
    return render(request, 'plants/edit.html')