from django.shortcuts import render
from .models import Tutorial
from django.db.models.aggregates import Count
from .forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



def splitQueryset(dict):
		tmp = []
		for m in dict:
			for n in m:
				tmp.append(n)
		tmp = list(set(tmp))
		return tmp

@csrf_exempt
@require_POST
def searchTitles(request):
	titles_search = Tutorial.objects.values_list('title')
	titles_search = splitQueryset(titles_search)
	target=[]
	titles=[]
	context = request.POST.get('header-search')
	if context:
		#return HttpResponse('OK')
		for title in titles_search:
			if context in title:
				target.append(title)
	for x in target:
		titles.append(Tutorial.objects.get(title=x))
	print(target)
	if not titles:
		titles = ['没有找到文章，请尝试其他关键字']
	return render(request, 'coding/titles.html',{'titles':titles})

@csrf_exempt
def devlogList(request, coding_language=None, coding_category=None, coding_labels=None, coding_sort=None):

	titles = Tutorial.objects.all()
	titles_search = Tutorial.objects.values_list('title')
	titles_search = splitQueryset(titles_search)

	labels=[]
	labels_wrap=[]
	labels_tuple = Tutorial.objects.values_list('tag')
	for label in labels_tuple:
		for x in label:
			labels_wrap.append(x)
			for m in x.split(','):
				labels.append(m)
	labels = list(set(labels))
	categories = Tutorial.objects.values_list('category')
	categories = splitQueryset(categories)
	languages = Tutorial.objects.values_list('language')
	languages = splitQueryset(languages)
	sorts = ('Newest','Oldest','MostViews','MostCommented')
	if coding_language:
		for language in languages:
			if coding_language in language:
				titles = Tutorial.objects.filter(language=coding_language)

	if coding_category:
		for category in categories:
			if coding_category in category:
				titles = Tutorial.objects.filter(category=coding_category)

	if coding_labels:
		for m in labels_wrap:
			if coding_labels in m:
				titles = Tutorial.objects.filter(tag=m)

	if coding_sort == 'Newest':
		titles = Tutorial.objects.all().order_by('-publish')
	if coding_sort == 'Oldest':
		titles = Tutorial.objects.all().order_by('publish')
	if coding_sort == 'MostCommented':
		titles = Tutorial.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')
	# if context:
	# 	for title in titles_search:
	# 		if context in title:
	# 			return render(request, 'coding/titles.html', {'titles':titles_search})

	# comments = Tutorial.objects.values_list
	paginator = Paginator(titles, 5)
	page = request.GET.get('page')
	try:
		current_page = paginator.page(page)
		titles = current_page.object_list
	except PageNotAnInteger:
		current_page = paginator.page(1)
		titles = current_page.object_list
	except EmptyPage:
		current_page = paginator.page(paginator.num_pages)
		titles = current_page.object_list

	return render(request, 'coding/titles.html', {'titles':titles, 'page':current_page, 'labels':labels, 'categories':categories, 'languages':languages, 'sorts':sorts})

def devlogContent(request, coding_id):
	diaries = Tutorial.objects.get(id=coding_id)
	coding_categories = Tutorial.objects.filter(id=coding_id).values('category')
	coding_category = list(coding_categories[0].values())[0]

	def convertPage(page):
		if len(page):
			page = list(page)[0]
		else:
			page = "已经为该类别的最后一篇文章"
		return page
	prePage = Tutorial.objects.filter(category=coding_category, id__gt=coding_id).order_by('-id')
	nextPage = Tutorial.objects.filter(category=coding_category, id__lt=coding_id).order_by('id')
	prePage = convertPage(prePage)
	nextPage = convertPage(nextPage)

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.diaries = diaries
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request, 'coding/content.html', {'diaries':diaries, 'comment_form':comment_form, 'prePage':prePage, 'nextPage':nextPage})

@csrf_exempt
def devlogListBySort(request, coding_sort):
	sorts = ('Newest','Oldest','Most-Views','Most-Commented')
	titles = Tutorial.objects.all()


	return render(request, 'coding/titles.html',{'titles':titles, 'sorts':sorts})

# def codingLikes(request):
# 	coding_id = request.POST.get('id')
# 	action = request.POST.get('action')
# 	if coding_id and action:
# 		try:
# 			coding = Tutorial.objects.get(id=coding_id)
# 			if action=='like':
# 				coding.users_like.add(request.user)
# 				return HttpResponse('1')
# 			else:
# 				coding.users_like.remove(request.user)
# 				return HttpResponse('2')
# 		except:
# 			return HttpResponse('failed')