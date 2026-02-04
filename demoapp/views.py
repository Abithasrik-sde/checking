from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Manager 👋 CI/CD is working!")