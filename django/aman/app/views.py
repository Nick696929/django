from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"base.html")
def list(request):
    return HttpResponse("jdbjsdkbvjdubgvuighudfhvbiehriguhdkjdvh9erhiovhshvkjlhxuhakjbduf9ihvkjhdviojhfohjflkdvhioahjvklh")
def main(request):
    return render(request,'index.html')