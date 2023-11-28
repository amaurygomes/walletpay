from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cria um usuário comum'

    def handle(self, *args, **options):
        nome_de_usuario = 'usuario_comum'
        senha = 'senha'

        if not User.objects.filter(username=nome_de_usuario).exists():
            User.objects.create_user(nome_de_usuario, password=senha)
            self.stdout.write(self.style.SUCCESS('Usuário comum criado com sucesso!'))
        else:
            self.stdout.write(self.style.WARNING('O usuário comum já existe!'))
