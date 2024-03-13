from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

#view for service_request
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'gas_utility/service_request.html', {'form': form})

#view for request_status
def request_status(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'gas_utility/request_status.html', {'service_requests': service_requests})
