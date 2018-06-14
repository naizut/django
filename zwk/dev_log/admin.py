from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
	list_display = ('title', 'publish', 'tag', 'category', 'body', 'resume')
	list_filter = ('publish', 'category')
	search_fields = ('title', 'body', 'tag', 'category', 'resume')
	date_hierarchy = 'publish'
	ordering = ['publish']
# Register your models here.

# admin.site.register(BugRecord)
admin.site.register(Tutorial, TutorialAdmin)
