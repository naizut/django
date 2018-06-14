from django.contrib import admin
from .models import Chat

class ChatAdmin(admin.ModelAdmin):
	list_display = ('chatter', 'body', 'created')
	list_filter = ('created',)
	search_fields = ('chatter', 'body')
	date_hierarchy = 'created'
	ordering = ['created']
# Register your models here.

admin.site.register(Chat, ChatAdmin)
