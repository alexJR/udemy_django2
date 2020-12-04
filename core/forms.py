from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea()) #Vai ser um campo que tera várias linhas

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}\n'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2', #Aplicação que envio o email, ou pode colocar o assunto.
            body=conteudo, # Corpo do email
            from_email='alex@hotmail.com', # para quem será enviado o email
            to=['alex@hotmail.com',],# Esse atributo deve estar em uma lista, pois pode ser enviado para mais de um e-mail
            headers={'Reply-To': email} # Caso for respondido, quem receberá o email. Nesse exemplo, o prórpio cliente que o enviou
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = {'nome', 'preco', 'estoque', 'imagem'}