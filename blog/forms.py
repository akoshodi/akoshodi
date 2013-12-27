from django import forms
from models import Blog_Post, Comment

class Blog_PostForm(forms.ModelForm):
    class Meta:
    	model = Blog_Post
    	fields = ('title', 'body', 'pub_date')

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('name', 'body')

