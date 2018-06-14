from django.views.generic.base import TemplateView
from news.models import News, Comment
from chat.models import Chat
from dev_log.models import Tutorial

class HomePageView(TemplateView):
	template_name = 'home.html'

	

	def get_context_data(self, **kwargs):
		def splitQueryset(dict):
			tmp = []
			for m in dict:
				for n in m:
					tmp.append(n)
			tmp = list(set(tmp))
			return tmp
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['latest_news'] = News.objects.first()
		context['latest_message'] = Chat.objects.all()
		context['latest_article'] = Tutorial.objects.first()
		context['titles'] = splitQueryset(Tutorial.objects.values_list('title').order_by('publish'))
		return context