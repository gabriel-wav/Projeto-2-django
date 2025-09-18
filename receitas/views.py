# receitas/views.py

# from django.shortcuts import render, get_object_or_404
# from .models import Receita
# from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Receita
from .forms import ContatoForm 


def home(request):
    # Pega o parâmetro de categoria da URL (ex: /?category=doces)
    categoria_query = request.GET.get("category")

    # Começa com todas as receitas, ordenadas pelas mais recentes
    receitas = Receita.objects.all().order_by("-created_at")

    # Se uma categoria foi especificada na URL, filtra as receitas
    if categoria_query:
        receitas = receitas.filter(categoria=categoria_query)

    # Pega a lista de categorias do seu modelo para exibir os botões no template
    categorias = Receita.CATEGORIAS

    # Envia os dados para o template
    context = {
        "receitas": receitas,
        "categorias": categorias,
        "categoria_selecionada": categoria_query  # Adicione esta linha
    }

    return render(request, "receitas/home.html", context)


def receita_detail(request, id):
    # Busca a receita pelo ID ou retorna um erro 404
    receita = get_object_or_404(Receita, pk=id)
    return render(request, "receitas/receita_detail.html", {"receita": receita})


def pesquisar_receitas(request):
    query = request.GET.get("q", "")
    resultados = []

    if query:
        # Busca por título, descrição ou ingredientes
        resultados = Receita.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(ingredients__icontains=query)
        )

    return render(
        request,
        "receitas/pesquisar_receitas.html",
        {"resultados": resultados, "query": query},
    )

    # VIEW PARA A PÁGINA "SOBRE NÓS"


def sobre_nos(request):
    """
    Renderiza a página 'Sobre Nós'.
    """
    categorias = Receita.objects.values_list("categoria", flat=True).distinct()
    return render(request, "receitas/sobre_nos.html", {"categorias": categorias})


# # VIEW PARA A PÁGINA DE CONTATO (ainda depende de forms.py)
# def contato(request):
#     """
#     Lida com a exibição e o processamento do formulário de contato.
#     """
#     categorias = Receita.objects.values_list("categoria", flat=True).distinct()

#     if request.method == "POST":
#         # Se o formulário foi enviado, preenche o form com os dados
#         form = ContatoForm(request.POST)
#         if form.is_valid():
#             # Se os dados são válidos, extrai as informações
#             nome = form.cleaned_data["nome"]
#             email = form.cleaned_data["email"]
#             mensagem = form.cleaned_data["mensagem"]

#             # Lógica para enviar o email (lembre-se de configurar o email em settings.py)
#             send_mail(
#                 subject=f"Mensagem de Contato de {nome}",
#                 message=f"Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}",
#                 from_email=email,  # E-mail do remetente
#                 recipient_list=[
#                     "seu_email_de_destino@exemplo.com"
#                 ],  # Para quem você quer enviar
#                 fail_silently=False,
#             )
#             # Redireciona para uma página de sucesso
#             return redirect("sucesso")
#     else:
#         # Se for a primeira vez na página (GET), cria um formulário vazio
#         form = ContatoForm()

#     context = {
#         "form": form,
#         "categorias": categorias,
#     }
#     return render(request, "receitas/contato.html", context)


def contato(request):
    """
    Lida com a exibição e o processamento do formulário de contato.
    """
    categorias = Receita.objects.values_list("categoria", flat=True).distinct()

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            # ... (resto do seu código POST) ...
            return redirect("sucesso")
    else:
        # Se for a primeira vez na página (GET), cria um formulário vazio
        form = ContatoForm()

        # ---- ADICIONE AS DUAS LINHAS ABAIXO PARA DIAGNÓSTICO ----
        print("--- DEBUG FORM ---")
        print(form.as_p())
        # --------------------------------------------------------

    context = {
        "form": form,
        "categorias": categorias,
    }
    return render(request, "receitas/contato.html", context)


def sucesso(request):
    """
    Página de agradecimento após o envio do formulário.
    """
    categorias = Receita.objects.values_list("categoria", flat=True).distinct()
    return render(request, "receitas/sucesso.html", {"categorias": categorias})


def sobre(request):
    return render(request, 'receitas/sobre.html')

def contato(request):
    return render(request, 'receitas/contato.html')