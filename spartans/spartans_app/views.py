from django.shortcuts import render

from .models import Empleado

# Create your views here.
def index(request):
    return render(request, "spartans_app/index.html")

def test(request):
    empleados = Empleado.objects.all()
    
    return render(request, 'spartans_app/test.html', {'empleados': empleados})
    