from django.db import models

# Create your models here.

class Receita(models.Model):
    CATEGORIAS = [
        ('doces', 'Doces'),
        ('salgados', 'Salgados'),
        ('bebidas', 'Bebidas'),
        ('sobremesas', 'Sobremesas'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='salgados')
    image = models.ImageField(upload_to="receitas/img", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ["-created_at"]