# receitas/forms.py
from django import forms

class ContatoForm(forms.Form):
    # Classe CSS para estilização com TailwindCSS
    form_class = "w-full px-3 py-2 text-gray-700 bg-gray-200 rounded-lg focus:outline-none focus:bg-white focus:ring-2 focus:ring-orange-500"

    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class': form_class, 'placeholder': 'Seu nome completo'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': form_class, 'placeholder': 'seuemail@exemplo.com'})
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': form_class, 'rows': 4, 'placeholder': 'Deixe sua mensagem aqui...'})
    )