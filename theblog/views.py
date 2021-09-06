from django.views.generic import ListView,DetailView
from theblog.models import Post
# def home(request):
# 	return render(request, 'home.html',{})



# Create your views here.


class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model=Post
	template_name = 'article_detail.html'