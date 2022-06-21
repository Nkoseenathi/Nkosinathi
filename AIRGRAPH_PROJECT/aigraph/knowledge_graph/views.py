from django.shortcuts import render
from django.http import HttpResponse
from knowledge_graph import queries

t = queries.queries()

def home(request):
     t.open()
     return HttpResponse('<p>'+str(t.topUniversities())+'</p>')


