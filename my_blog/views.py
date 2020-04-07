from django.urls import reverse
from django.views import generic

from my_blog.forms import BlogForm
from my_blog.models import Blog


class BlogList(generic.ListView):
    model = Blog
    template_name = 'index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title_selected'] = Blog.objects.filter(title__startswith='H')
        return context


class CreateArticle(generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('index')


class EditArticle(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('index')
