from django.db import models
#from .models import Nicho  # Importando o modelo Nicho para a chave estrangeira
# Create your models here.

class Nicho(models.Model):
    id_nicho = models.BigAutoField(primary_key=True)
    numero_nicho = models.PositiveIntegerField()
    local = models.CharField(max_length=100, null=True)
    observacao = models.TextField(null=True)

    class Meta:
        db_table = 'nicho'

    def __str__(self):
        return f'Nicho {self.numero_nicho}'  # Personalizando a representação do objeto

###############################################
class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    nome_do_livro = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, null=True)  # Permitindo valores nulos
    quantidade_exemplar = models.IntegerField()
    saldo_exemplar = models.IntegerField()
    id_nicho = models.ForeignKey(Nicho, on_delete=models.CASCADE)
    observacao_livro = models.TextField(null=True)  # Permitindo valores nulos

    class Meta:
        db_table = 'livro'

    def __str__(self):
        return self.nome_do_livro  # Definindo a representação como o nome do livro