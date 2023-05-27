from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def content(request):
    name='vinoth'
    loc='bangalore'
    
    return HttpResponse(f'NAME IS :{name},location of :{loc}')

def render_html(request):
    name='Doni'
    team='CSK'

    d={'na':name,'te':team}
    return render(request,'render_html.html',d)