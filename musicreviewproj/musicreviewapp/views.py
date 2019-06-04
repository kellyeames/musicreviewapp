from django.shortcuts import render, get_object_or_404
from .models import GenreType, Album, Review
from .forms import AlbumForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'musicreviewapp/index.html')

def gettypes(request):
    type_list=GenreType.objects.all()
    return render(request, 'musicreviewapp/types.html' , {'type_list' : type_list})

def getalbums(request):
    albums_list=Album.objects.all()
    return render(request, 'musicreviewapp/albums.html', {'albums_list': albums_list})

def albumdetails(request, id):
    album=get_object_or_404(Album, pk=id)
    reviews=Review.objects.filter(album=id).count()
    context={
        'album' : album,
        'reviews' : reviews,
    }
    return render(request, 'musicreviewapp/albumdetails.html', context=context)

@login_required
def newAlbum(request):
    form=AlbumForm
    if request.method=='POST':
        form=AlbumForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AlbumForm()
    else:
        form=AlbumForm()
    return render(request, 'musicreviewapp/newalbum.html', {'form': form})

def loginmessage(request):
    return render(request, 'musicreviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'musicreviewapp/logoutmessage.html')

def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'musicreviewapp/newreview.html', {'form': form})
    