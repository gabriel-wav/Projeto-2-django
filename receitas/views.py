# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receita
from django.db.models import Q

def home(request):
    # Pega todas as receitas
    receitas = Receita.objects.all()
    
    # Envia o dicionário {'receitas': receitas} para o template
    return render(request, 'receitas/home.html', {'receitas': receitas})

def receita_detail(request, id):
    # Busca a receita pelo ID ou retorna um erro 404
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
    query = request.GET.get('q', '')
    resultados = []
    
    if query:
        # Busca por título, descrição ou ingredientes
        resultados = Receita.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) | 
            Q(ingredients__icontains=query)
        )
    
    return render(request, 'receitas/resultados.html', {
        'resultados': resultados,
        'query': query
    })