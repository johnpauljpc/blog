from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

# Create your views here.

class Post_ListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'list.html'
    paginate_by = 1
    


def Post_DetailView(request, pk, year, month, day, slug):
    post = get_object_or_404(Post, status = 'published',
        id = pk, 
        slug = slug,
        publish__year = year,
        publish__month = month,
        publish__day = day
            
            )

    return render(request, 'detail.html', {'post':post})