from django.shortcuts import redirect, render
from .models import Member
from .serializer import MemberSerializer
from django.http import JsonResponse

def index(request):
    mem=Member.objects.all()
    # serializer = MemberSerializer(mem, many = True)
    # json_data = serializer.data  
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    # data = {'firstname': x, 'lastname': y, 'country': z}
    # serializer = MemberSerializer(data = data )
    # if serializer.is_valid():
    mem.save()
    return {JsonResponse(mem),redirect("/")}
    # else:
    #    return JsonResponse(serializer.errors ,safe= False)
        
def delete(request,id):
    mem=Member.objects.get(id=id)
    # serializer = MemberSerializer(mem)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")