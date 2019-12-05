from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo
from .models import Our_images

from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    all_movies = MovieInfo.objects.all()
    return render(request,"moviereview/home.html",{'Movies':all_movies})

def AddMovie(request):
    all_movies = MovieInfo.objects.all()
    return render(request,"moviereview/AddMovies.html",{'Movies':all_movies})

def rohit(request):
    all_movies = MovieInfo.objects.all()
    return render(request, "moviereview/index.html", {'Movies': all_movies})

def search(request):
    q=request.GET.get('q')
    if q:
        name = MovieInfo.objects.filter(Q(movie_name__icontains=q))
        if name:
            return render(request,"moviereview/home.html",{'sr': name,'query': q})
        else:
            return render(request,"moviereview/home.html",{'r':['result not found']})
    else:
        return HttpResponse('/atleast put your data/')
    return render(request,"moviereview/home.html")


def shadi(request):
    all_url = Our_images.objects.all()
    return render(request, "moviereview/shadi.html", {'My_url': all_url})


def add_movie_form_submission(request):
    print("hello form is submitted")
    movie_name=request.POST["movie_name"]
    movie_type = request.POST["movie_type"]
    movie_review = request.POST["movie_review"]
    movie_release_date = request.POST["movie_release_date"]
    movie_detail = request.POST["movie_detail"]
    # pic=request.POST.get('image')

    pic=request.FILES['image']
    print(pic.name)
    print(pic.size)
    fs=FileSystemStorage()
    fs.save(pic.name,pic)

    movie_info=MovieInfo(movie_name=movie_name,movie_type=movie_type,movie_review=movie_review,
                         movie_release_date=movie_release_date,movie_detail=movie_detail,image=pic)
    movie_info.save()
    all_movies = MovieInfo.objects.all()
    return render(request,"moviereview/index.html",{'Movies':all_movies})