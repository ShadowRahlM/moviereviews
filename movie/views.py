from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from .models import Movie,Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def deletereview(request,review_id):
    movie = get_object_or_404(Review,pk=review_id,user=request.user)
    Review.delete()
    return redirect('detail',Review.movie_id)


@login_required
def updatereview(request,review_id_id):
    movie = get_object_or_404(Review,pk=review_id_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=Review)
        return render(request, 'updatereview.html',{'review': Review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST,instance=Review)
            form.save()
            return redirect('detail', Review.movie.id)
        except ValueError:
            return render(request,'updatereview.html',{'review': Review,'form':form,'error':'Bad data in form'})


@login_required
def createreview(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html',{'form':ReviewForm(), 'movie':movie})
    
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request,'createreview.html',{'form':ReviewForm(),'error':'bad datapassed in'})




def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html',{'movie':movie},{'reviews':reviews})




def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html',{'searchTerm':searchTerm,'movies':movies})



def about(request):
    return render(request,'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request,'signup.html',{'email':email})


