from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question, Thought
from .forms import ThoughtForm

#View of latest few Questions
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
            """
            Return the last five published questions (not including those set to be
            published in the future).
            """
            return Question.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


#View of a Question's text
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


#View of a Question's results
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#Handles voting for a particular Question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
           'question': question,
           'error_message': "You didn't select a choice.", 
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

class ThoughtListView(generic.ListView):
    template_name = "polls/thought_list.html"
    context_object_name = 'thought_list'

    def get_queryset(self):
        return Thought.objects.order_by('-pub_date')[:]

#Handles thought submission
def thoughts(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:thought_list'))
    else:
        form = ThoughtForm()
    return render(request, 
                    'polls/thoughts.html',
                    {'form' : form})
