from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Programme, Category

# Create your views here.

def all_programmes(request):
    """ A view to show all programmes, including sorting and search queries """

    programmes = Programme.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            programmes = programmes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('programmes'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            programmes = programmes.filter(queries)

    context = {
        'programmes': programmes,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_detail(request, programme_id):
    """ A view to show individual programme details """

    programme = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': programme,
    }

    return render(request, 'programmes/programme_detail.html', context)