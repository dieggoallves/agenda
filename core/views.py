from django.shortcuts import render
from core.models import Evento

# Create your views here.

#'''Direciona para a agenda ao não especificar no link da pagina'''
#def index(request):
#    return redirect('/agenda/')

'''Busca o usuario da sessão e retorna todos os registros desse agente'''
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)