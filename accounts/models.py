from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Usuário customizado do blog.

    Herda de ``AbstractUser`` os campos: ``username`` (nome de usuário),
    ``first_name`` (nome), ``last_name`` (sobrenome), ``email``,
    ``password`` (senha) e ``last_login`` (último login).
    """

    age = models.PositiveIntegerField('idade', null=True, blank=True)
    city = models.CharField('cidade', max_length=100, blank=True)
    profile_photo = models.ImageField(
        'foto de perfil', upload_to='profiles/', null=True, blank=True
    )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return self.username
