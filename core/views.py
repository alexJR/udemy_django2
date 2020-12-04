from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto
from django.shortcuts import redirect

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            #TRANTANDO A MENSAGEM
            messages.success(request, "E-mail enviado com sucesso!")
        else:
            messages.error(request, "Erro ao enviar o e-mail")
    context = {
        'form': form
    }

    return render(request, 'contato.html', context)


def produto(request):
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        if(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()
                #prod = form.save(commit=False)
                #posso mostrar os valores carregados
                #print(f'Produto: {prod.nome}')
                #print(f'Preço: {prod.preco}')
                #print(f'Estoque: {prod.estoque}')

                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salva o produto!')

        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')