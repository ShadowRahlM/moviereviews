from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import Movie,Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def deletereview(request,review_id):
    movie = get_object_or_404(Movie,pk=review_id,user=request.user)
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    return redirect('detail', review.movie.id)


@login_required
def updatereview(request,review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        try:
            form = ReviewForm(request.POST,instance=review)
            if form.is_valid():
                form.save()
                return redirect('detail', review.movie.id)
        except ValueError:
            return render(request,'updatereview.html',{'review': review,'form':form,'error':'Bad data in form'})
    return render(request, 'updatereview.html',{'review': review,'form':form})


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
            return render(request,'createreview.html',{'form':ReviewForm(),'error':'Bad data passed in form'})




def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html', {'movie': movie, 'reviews': reviews})




def home(request):
    search_term = request.GET.get('searchMovie')
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html',{'searchTerm':search_term,'movies':movies})



def about(request):
    return render(request,'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request,'signup.html',{'email':email})


