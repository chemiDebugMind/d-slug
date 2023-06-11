from django.views.generic import ListView, DetailView


from .models import Articles


class ArticleListView(ListView):
    model = Articles
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article_detail.html"


