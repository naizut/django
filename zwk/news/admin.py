from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'resume', 'publish')
	list_filter = ('publish',)
	search_fields = ('title', 'resume')
	date_hierarchy = 'publish'
	ordering = ['publish']
# Register your models here.

admin.site.register(News, NewsAdmin)
