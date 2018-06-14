from django.shortcuts import render

# Create your views here.
def games_pics(request):
	return render(request, 'games/pics.html')

def games_csgo(request):
	return render(request, 'games/csgo.html')

def games_fifa14(request):
	return render(request, 'games/fifa14.html')
# def games_eve(request):
# 	return render(request, 'games/eve.html')

# def games_fifa14(request):
# 	return render(request, 'games/fifa14.html')