from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .models import Event
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Event_form, Question_form
from .models import Event
from User.models import New
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from .models import Event, Question, Answer, New
from textblob import TextBlob
import csv
import reportlab
import io
import pdfkit
from reportlab.pdfgen import canvas

# Create your views here.


@login_required
def index(request, myid):

    newed = New.objects.get(username=request.user)
    print(newed)
    x = -1
    # for i in Event.objects.filter(id=myid):
    #     x = x + 1
    even = Event.objects.filter(id=myid)
    print(even)
    for i in even:
        events = i
    # even = Event.objects.all()[1]
    # print(even)
    creates = Question.objects.filter(event_related=events)
    # my_sentence = TextBlob("I am reading a Blog post on AnalyticsVidhya. I am loving it!")
    # print(my_sentence.tags)
    # print(my_sentence.noun_phrases)
    # print(my_sentence.sentiment)
    # print(my_sentence.words)
    # print(my_sentence.sentences)

    return render(request, 'Creators/submit.html', {"creates": creates})


def after(request):
    n = New.objects.all()[0]
    x = -1
    for i in Event.objects.filter(creator=n):
        temp = i.id
        x = x + 1

    print(x)
    even = Event.objects.filter(creator=n)[x]
    u = n.username
    q = Question.objects.filter(event_related=even)
    x = request.POST.get('numbergenerate'),
    k = x[0]
    k = int(k)

    print(temp)
    for i in range(k):
        concat = "Car" + str(i+1)
        print(q[i].question)
        print(request.POST.get(concat))
        p = Answer(answer=request.POST.get(concat),
                   answer_of_quest=q[i], user_admin=u)
        p.save()

        with open('Creators/static/Creators/Events/Event{}.csv'.format(temp), 'a', newline='') as f:

            writer = csv.writer(f)
            writer.writerow([q[i].question])
            writer.writerow([request.POST.get(concat)])
            writer.writerow(TextBlob(request.POST.get(concat)).sentiment)
            writer.writerow(TextBlob(request.POST.get(concat)).sentences)
            writer.writerow(TextBlob(request.POST.get(concat)).noun_phrases)

        # pdfkit.from_file('Creators/templates/submit.html', 'Output.pdf')

    # return HttpResponse('This is my HomePage')
    return redirect('index')
    # buffer = io.BytesIO()
    # p = canvas.Canvas(buffer)
    # p.drawString(100,100, 'Hello World.')
    #
    # p.showPage()
    # p.save()
    #
    # buffer.seek(0)
    # return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# Create your views here.
# def index(request):
#     return render(request, 'Creators/creators.html')
class q(ListView):
    model = Event


def Questions(request, prod_id):
    request.session['p_id'] = prod_id
    Events = Event.objects.filter(pk=prod_id)
    print(Events)
    if request.method == 'POST':
        form = Question_form(request.POST, request.FILES)
        if form.is_valid():
            us = request.user.new.username
            New_user = New.objects.filter(username=us)
            for i in Events:
                Event_at = i
            p = form.save(commit=False)
            p.event_related = Event_at
            print('hello')
            p.save()
            print('hello')
            return redirect('Question', prod_id)
        else:
            print(form.errors)
            return render(request, 'Creators/questions.html', {'form': Question_form})
    else:
        form = Question_form()
    return render(request, 'Creators/questions.html', {'form': Question_form})


def createform(request):
    if request.method == 'POST':
        form = Event_form(request.POST, request.FILES)
        if form.is_valid():
            us = request.user.new.username
            New_user = New.objects.filter(username=us)
            for i in New_user:
                News = i
            p = form.save(commit=False)
            p.creator = News
            print(p.creator)
            print('hello')
            p.save()
            print('hello')
            k = p.pk
            print(k)
            return redirect('Question', k)
        else:
            print(form.errors)
            return render(request, 'Creators/Creator_form.html', {'form': Event_form})
    else:
        form = Event_form()
    return render(request, 'Creators/Creator_form.html', {'form': Event_form})


# Create your views here.


# def togo(request):
#     return redirect('home', request.session.get('po'))

# def home(request):
#     return render(request, 'Creato.html')
@login_required
def home(request, *args, **kwargs):
    try:
        # print("kkk")
        print(request.GET.get('form'))
        # print(pk)
        # print(request['form'])
        # r1 = pk
        r1 = request.GET.get('form')
        request.session['po'] = r1
        name = SocialAccount.objects.get(
            user=request.user).extra_data['name']
        print(name)

        e = Event.objects.get(id=r1).csv_file
        # print(e)
        q = pd.read_csv(e)
        r = q["Full Name"].eq(name).any()
        print(r)
        # r = sessions['h']
        if not r:
            return redirect('login')
        else:
            return redirect('final', r1)
    except:
        return redirect('login')


# class home(LoginRequiredMixin, ListView):
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     print(self.kwargs['pk'])
#     #     return context
#     def __init__(self, **kwargs):
#         self.r = False

#     # def get_queryset(self, *args, **kwargs):
#     #     # try:
#     #     # print(self.request.user)
#     #     name = SocialAccount.objects.get(
#     #         user=self.request.user).extra_data['name']
#     #     print(name)
#     #     r1 = self.kwargs['pk']
#     #     e = Event.objects.get(id=r1).csv_file
#     #     # print(e)
#     #     q = pd.read_csv(e)
#     #     self.r = q["Full Name"].eq(name).any()

#         # self.request.session['h'] = r
#         # self.

#         # print(r)

#         # if not r:
#         #     return redirect('logout')
#         # print("Sorry")

#         # except:
#         #     self.r = False

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             name = SocialAccount.objects.get(
#                 user=self.request.user).extra_data['name']
#             print(name)
#             r1 = self.kwargs['pk']
#             e = Event.objects.get(id=r1).csv_file
#             # print(e)
#             q = pd.read_csv(e)
#             self.r = q["Full Name"].eq(name).any()
#             print(self.r)
#             # r = sessions['h']
#             if not self.r:
#                 return redirect('logout')
#             else:
#                 return redirect('final', r1)
#         except:
#             return redirect('logout')

#     # print(r)


def final(request, po):
    print(po)
    return render(request, 'Creators/creators.html')
