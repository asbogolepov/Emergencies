from django.shortcuts import render, redirect
from emergencies.forms import EmergencyForm, EmergencyImageForm
from emergencies.models import Emergency, EmergencyImage
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def emergencies(request):
    name = "Anton"
    current_day = "08.06.2017"
    form = EmergencyForm(request.POST or None)
    emergency_images = EmergencyImage.objects.filter(is_active=True, is_main=True)

    if request.method == "POST" and form.is_valid():
        form1 = EmergencyImageForm(request.POST, request.FILES)
        form1.save()

        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
        return redirect('emergencies')
    else:
        form1 = EmergencyImageForm()

    return render(request, 'emergencies/home.html', locals())


# def emergency(request, emergency_id):
#     emergency = Emergency.objects.get(id=emergency_id)
#     return render(request, 'emergencies/emergency.html')

# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'emergencies/emergency.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'emergencies/emergency.html')


def model_form_upload(request):
    if request.method == 'POST':
        form1 = EmergencyImageForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('emergencies')
    else:
        form1 = EmergencyImageForm()
    return render(request, 'emergencies/home.html', {
        'form1': form1
    })

