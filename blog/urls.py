from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'blog.views.blog_posts' ),
	url(r'^post/(?P<blog_post_id>\d+)/$', 'blog.views.blog_post'),
	#url(r'^add_comment/(?P<blog_post_id>\d+)/$', 'blog.views.add_comment'),

	# url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
	# url(r'^create/$', 'article.views.create'),
	# url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),


)