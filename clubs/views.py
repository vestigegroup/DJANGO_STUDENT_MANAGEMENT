from django.shortcuts import render
from clubs.models import Club, Activity


def clubshome(request):
    topclubs = Club.objects.all()[:4]
    allclubs = Club.objects.all()
    activities = Activity.objects.order_by('-date')
    context = {
        'topclubs': topclubs,
        'allclubs': allclubs,
        'activities': activities,
    }
    return render(request, 'clubs/clubshome.html', context)


def clubs_history(request):
    clubs = Activity.objects.order_by('-date')
    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs/history.html', context)

