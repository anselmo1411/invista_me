from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required
#cria paginas.

# pagina de investimento 
def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render (request,'investimentos/investimentos.html', context=dados)
#pagina de detalhes.
def detalhe(request,id_investimento):
    dados ={
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)

#formulario antomatico
@login_required
def criar(request):
    if request.method == 'POST':  #enviando dados.
        investimento_Form = InvestimentoForm(request.POST)
        if investimento_Form.is_valid():
            investimento_Form.save()
        return redirect('investimentos')
    else:
        investimento_Form= InvestimentoForm()
        formulario = {
            'formulario': investimento_Form
        }
        return render (request, 'investimentos/novo_investimento.html', context=formulario)

@login_required
def editar(request, id_investimento):
    investimento= Investimento.objects.get(pk=id_investimento)
    #novo investimento/1 ->GET
    if request.method == 'GET': #verficar tipo de requisição
        #Novo formulario já atualizado pela 'instancia.
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    # caso requisição seja POST novo formulário.
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect ('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})


    
