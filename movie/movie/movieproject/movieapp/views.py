from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movies
from .form import MoviesForm
# Create your views here.

def hello(request):
    movie=Movies.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year = request.POST.get('year')
        dec = request.POST.get('dec')
        img=request.FILES['img']
        movie=Movies(name=name,year=year,dec=dec,img=img)
        movie.save()


    return render(request,'add.html')


def update(request,id):
    movie=Movies.objects.get(id=id)
    form=MoviesForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method =='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')