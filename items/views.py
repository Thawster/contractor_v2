from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import PageForm
from django.http import HttpResponseRedirect
from items.models import Page

def get_name(request):
    if request.method == 'POST':

        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific item page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class PageCreateView(CreateView):
    model = Page

    def get(self, request):
        form = PageForm()
        context = {'form': form,}
        return render(request, "new-item.html", context)

    def post(self, request):
        if request.method == "POST":
            form = PageForm(request.POST)
            if form.is_valid():
                item = form.save()

                txt_message = item.title+" has been successfully created"

                return render(request, 'page.html', {'page': item})
            else:

                errors = "Item was not created" 
                error_page('page-error', errors)
        else:
            form = PageForm()

        context = {'form': form}

        return render(request, 'item/page.html', context)