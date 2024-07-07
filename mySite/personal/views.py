from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def about(request):
    return render(request, 'personal/about.html')

def additional1(request):
    return render(request, 'personal/additional1.html')

def additional2(request):
    return render(request, 'personal/additional2.html')


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'personal/index.html', context)

def poll_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'personal/poll_detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'personal/poll_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_detail', args=(question.id,)))

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'personal/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'personal/register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Invalid login details')
    return render(request, 'personal/login.html')

from django.contrib.auth.decorators import login_required

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'personal/poll_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_detail', args=(question.id,)))
