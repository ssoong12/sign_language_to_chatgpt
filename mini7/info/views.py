from django.shortcuts import render
from .models import Picture
from .forms import PictureForm

def picture_view(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            picture = form.cleaned_data['picture']
    else:
        form = PictureForm()
        picture = Picture.objects.first()  # display the first picture by default
    return render(request, 'info/picture.html', {'form': form, 'picture': picture})

from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import get_storage_class
import os

def image_desc_list(request):
    image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'info/images')
    desc_dir = os.path.join(settings.STATICFILES_DIRS[0], 'info/desc')

    image_files = sorted(os.listdir(image_dir))

    image_desc_list = []

    for image_file in image_files:
        point = image_file.find('.')
        name = image_file[:point]

        # image_path = os.path.join(image_dir, image_file)
        desc_path = os.path.join(desc_dir, f'{name}.txt')
        
        with open(desc_path, 'r', encoding='utf-8') as f:
            desc_text = f.read()
        
        if desc_text == "":
            desc_text = "PLACEHOLDER"

        image_desc_list.append({
            'name': name,
            'image': 'info/images/' + image_file,
            'desc': desc_text
        })

    # return JsonResponse(image_desc_list, safe=False)
    return render(request, 'info/image_desc_list.html', {'image_desc_list': image_desc_list})