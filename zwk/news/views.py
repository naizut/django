from django.shortcuts import render
from .models import News, Comment
from .forms import CommentForm
from django.db.models.aggregates import Count

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/account/login/')
def news_list(request):
	news = News.objects.all()
	num_comments = Comment.objects.values_list('article').annotate(dd=Count('created'))
	return render(request, 'news/news_list.html', {'news':news})

def news_content(request, news_id):
	message = News.objects.get(id=news_id)

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.article = message
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request, 'news/news_content.html', {'message':message, 'comment_form':comment_form})

@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def newsLikes(request):
	news_id = request.POST.get('id')
	action = request.POST.get('action')
	if news_id and action:
		try:
			news = News.objects.get(id=news_id)
			if action=='like':
				news.users_like.add(request.user)
				return HttpResponse('1')
			else:
				news.users_like.remove(request.user)
				return HttpResponse('2')
		except:
			return HttpResponse('failed')


