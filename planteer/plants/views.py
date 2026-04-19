from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant
from .forms import PlantForm


app_name = "plants"

#TODO: make the details view be here
# Create your views here.
def all_plants_view(request):
    plants = Plant.objects.all()
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    
    if category:
        plants = plants.filter(category=category)
    if is_edible in ('true', 'false'):
        plants = plants.filter(is_edible=(is_edible == 'true'))
        
    return render(request, 'plants/plants-all.html', {
        'plants': plants,
        'categories': Plant.Category.choices,
        'selected_category': category,
        'selected_edible': is_edible,
    })

def plant_detail_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related = Plant.objects.filter(category=plant.category).exclude(id=plant.id)
    return render(request, 'plants/plant-detail.html', {'plant': plant, 'related': related})

#============= searching =============
def search_view(request):
    query = request.GET.get('q')
    plants = Plant.objects.filter(name__icontains=query) if query else Plant.objects.none()
    return render(request, 'plants/search.html', {'plants': plants, 'query': query})


# ==== crud stuff ======
def create_view(request):
    form = PlantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('plants:all_plants_view')
    return render(request, 'plants/create.html', {'form': form})

def update_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    form = PlantForm(request.POST or None, request.FILES or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('plants:plant_detail_view', plant_id=plant.id)
    return render(request, 'plants/edit.html', {'form': form, 'plant': plant})

def delete_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:all_plants_view')
    return redirect('plants:plant_detail_view', plant_id=plant_id)
