from django.shortcuts import render_to_response
from blog.models import Blog_Post #, Comment
from django.http import HttpResponse
# from forms import Blog_PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone

# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import  Context
# from django.views.generic.base import TemplateView

# Create your views here.
def blog_posts(request):
	return render_to_response('blog_posts.html', {'blog_posts': Blog_Post.objects.all()})

def blog_post(request, blog_post_id=1):
	return render_to_response('blog_post.html', {'blog_post': Blog_Post.objects.get(id=blog_post_id)})

def create(request):
	if request.POST:
		form = Blog_PostForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/blog')
	else:
		form = Blog_PostForm()

	args = {}
	args.update(csrf(request))

	args['form'] = 	form
	return render_to_response("create_blog_post.html", args)


def add_comment(request, article_id):
	a = Article.objects.get(id=article_id)

	if request.method == 'POST':
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.article = a
			c.save()

			return HttpResponseRedirect('/articles/get/%s' % article_id)

	else:
		f = CommentForm()

	args = {}
	args.update(csrf(request))

	args['article'] = a
	args['form'] = f

	return render_to_response('add_comment.html', args)

