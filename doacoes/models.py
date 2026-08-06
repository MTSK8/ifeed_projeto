from django.db import models # type: ignore  # noqa: I001


class Doacao(models.Model):
    STATUS_CHOICES = [  # noqa: RUF012
        ('disponivel', 'Disponível'),
        ('reservada', 'Reservada'),
        ('coletada', 'Coletada'),
        ('entregue', 'Entregue'),
    ]

    nome_alimento = models.CharField(max_length=150)
    quantidade = models.CharField(max_length=50)
    data_validade = models.DateField()
    foto = models.ImageField(upload_to='doacoes_fotos/', blank=True, null=True)
    tipo_armazenamento = models.CharField(max_length=150, blank=True, null=True)
    horario_retirada = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_alimento} - Status: {self.status}"