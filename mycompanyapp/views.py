from django.shortcuts import render
from django.http import JsonResponse
from .models import Inquiry
def home(request):
    return render(request, 'home.html')

def inquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        inquiryObject = Inquiry.objects.create(name=name, email=email, contactNumber=contact, message=message)
        return JsonResponse({"message":"success"}, safe=False)
    else:
        return JsonResponse("Method Not allowed", safe=False)