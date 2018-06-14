from django.shortcuts import render
from .forms import ChatForm
from .models import Chat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# # Create your views here.
# @login_required(login_url='/account/login')
def chat_board(request):
	messages_box = Chat.objects.all()
	paginator = Paginator(messages_box, 5)
	page = request.GET.get('page')
	try:
		current_page = paginator.page(page)
		messages = current_page.object_list
	except PageNotAnInteger:
		current_page = paginator.page(1)
		messages = current_page.object_list
	except EmptyPage:
		current_page = paginator.page(paginator.num_pages)
		messages = current_page.object_list
	if request.method == 'POST':
		chat_board = ChatForm(data=request.POST)
		if chat_board.is_valid():
			new_chat = chat_board.save(commit=False)
			new_chat.save()
	else:
		chat_board = ChatForm()
	return render(request, 'chat/chat_board.html', {'messages':messages, 'chat_board':chat_board, 'page':current_page})