from django.shortcuts import render, get_object_or_404, redirect
from .models import Slider, About, Comment, Media, Project, News, Team, Gallery, Testimonial, Partner, Event, Video, Agency
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    # Fetch data from the database
    sliders = Slider.objects.all()
    about = About.objects.first()  # Assuming there's only one About section
    projects = Project.objects.all()
    news = News.objects.all()
    team = Team.objects.all()
    testimonials = Testimonial.objects.all()
    partners = Partner.objects.all()
    events = Event.objects.all()
    video = Video.objects.all()

    # Context data to pass to the template
    context = {
        'sliders': sliders,
        'about': about,
        'projects': projects,
        'news': news,
        'team': team,
        'testimonials': testimonials,
        'partners': partners,
        'events': events,
        'videos': video
    }
    
    return render(request, 'src/home.html', context)


def about(request):
        # Fetch data from the database
  
    team = Team.objects.all()

 
    # Context data to pass to the template
    context = {

        'team': team
    }
    
    return render (request, 'src/about.html', context)


def contact(request):
    return render (request, 'src/contact.html')


def agency(request, pk):

    agency = Agency.objects.get(id=pk)

    context = {

        'agency': agency
    }

    return render(request, 'src/agency_details.html', context)





def news_list(request):
    # Fetch all news items
    news_list = News.objects.all().order_by('-date')  # Order by date (newest first)

    # Pagination
    paginator = Paginator(news_list, 4)  # Show 4 posts per page
    page = request.GET.get('page')  # Get the current page number from the URL

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page
        news = paginator.page(paginator.num_pages)

    context = {
        'news': news,
    }
    return render(request, 'src/news_list.html', context)



def news_details(request, pk):
    news_item = get_object_or_404(News, id=pk)
    comments = news_item.comments.all().order_by('-created_at')
    comment_count = news_item.comment_count()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item  # Associate the comment with the news item
            comment.save()  # Save the comment
            return redirect('news-details', pk=news_item.id)  # Redirect to the same page
    else:
        form = CommentForm()

    context = {
        'news_item': news_item,
        'comments': comments,
        'comment_count': comment_count,
        'form': form,
    }

    return render(request, 'src/news_details.html', context)





def gallery_list(request):
    # Fetch all gallery images
    gallery_list = Gallery.objects.all().order_by('-created_at')  # Order by newest first

    # Pagination
    paginator = Paginator(gallery_list, 8)  # Show 8 images per page
    page = request.GET.get('page')  # Get the current page number from the URL

    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        gallery = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page
        gallery = paginator.page(paginator.num_pages)

    context = {
        'gallery': gallery,
    }
    return render(request, 'src/gallery.html', context)




def media_list(request):
    # Fetch videos and audio separately
    video_list = Media.objects.filter(media_type='video').order_by('-created_at')
    audio_list = Media.objects.filter(media_type='audio').order_by('-created_at')

    # Pagination for videos
    video_paginator = Paginator(video_list, 4)  # Show 4 videos per page
    video_page = request.GET.get('video_page')
    try:
        videos = video_paginator.page(video_page)
    except PageNotAnInteger:
        videos = video_paginator.page(1)
    except EmptyPage:
        videos = video_paginator.page(video_paginator.num_pages)

    # Pagination for audio
    audio_paginator = Paginator(audio_list, 4)  # Show 4 audio files per page
    audio_page = request.GET.get('audio_page')
    try:
        audio = audio_paginator.page(audio_page)
    except PageNotAnInteger:
        audio = audio_paginator.page(1)
    except EmptyPage:
        audio = audio_paginator.page(audio_paginator.num_pages)

    context = {
        'videos': videos,
        'audio': audio,
    }
    return render(request, 'src/media.html', context)