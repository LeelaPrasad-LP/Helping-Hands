from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

from .models import Problem
def student(request):
    return render(request,'student/index.html')

def profileView(request):
    context={
        'model':Problem
    }
    return render(request,'student/profile.html',context)

from django.views.generic import TemplateView
class Contactus(TemplateView):
    template_name = "student/contact.html"

class ProblemsView(ListView):
    model=Problem
    template_name='student/yourproblems.html'
    context_object_name='problems'

class ProblemCreate(CreateView):
    model           = Problem
    fields          = ['Author','Title','description','Organisation','Location']
    template_name   ='student/createProblem.html'
    success_url     =reverse_lazy('loginhome')
class Problemdetailview(DetailView):
    model=Problem
    template_name='student/detailprob.html'
    context_object_name='prob'

def upvote(request, pk):
    prob = Problem.objects.get(pk=pk)
    prob.upvotes += 1
    prob.save()
    return redirect('problems')

class ProblemEdit(UpdateView):
    template_name='student/edit_problem.html'
    model=Problem
    context_object_name='editprob'
    fields=['Title','description','Organisation','Location']
    success_url=reverse_lazy('problems')
class deleteArticle(DeleteView):
    template_name='stuent/delete.html'
    model=Problem
    context_object_name='art'
    success_url=reverse_lazy('loginhome')

#VIEWS FOR DONOR

def donor(request):
    return render(request,'donor/index.html')
def dprofileView(request):
    context={
        'model':Problem
    }
    return render(request,'donor/profile.html',context)

class dProbView(ListView):
    model=Problem
    template_name='donor/problemsView.html'
    context_object_name='problems'
class dProblemdetailview(DetailView):
    model=Problem
    template_name='donor/detailprob.html'
    context_object_name='prob'
class dContactus(TemplateView):
    template_name = "donor/contact.html"