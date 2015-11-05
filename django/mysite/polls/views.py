from django.shortcuts import render

# Create your views here.


from .models import Poll

def PollView(request):
	context = {'year' : 'this is year'}
	return render(request,'polls/poll.html',context)
