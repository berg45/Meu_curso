import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from app.models import Usuario, Empresa, Publicacao

class Command(BaseCommand):
    help = 'Importa dados de arquivos CSV para as tabelas do banco de dados'

    def handle(self, *args, **kwargs):
        # Caminho para os arquivos CSV
        caminho_usuarios = os.path.join(settings.BASE_DIR, 'usuario.csv')
        caminho_empresas = os.path.join(settings.BASE_DIR, 'empresa.csv')
        caminho_publicacoes = os.path.join(settings.BASE_DIR, 'publicacao.csv')

        # Importar dados de usuarios.csv
        self.stdout.write(self.style.NOTICE('Importando dados de usuarios.csv...'))
        with open(caminho_usuarios, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Usuario.objects.create(
                    name=row['nome'],
                    email=row['email'],
                    nickname=row['nickname'],
                    senha=row['senha'],
                    foto=row['foto'],  # Certifique-se de que as fotos estão acessíveis
                )
        self.stdout.write(self.style.SUCCESS('Dados de usuários importados com sucesso!'))

        # Importar dados de empresa.csv
        self.stdout.write(self.style.NOTICE('Importando dados de empresa.csv...'))
        with open(caminho_empresas, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Empresa.objects.create(
                    nome=row['nome'],
                    logo=row['logo'],  # Certifique-se de que os logos estão acessíveis
                )
        self.stdout.write(self.style.SUCCESS('Dados de empresas importados com sucesso!'))

        # Importar dados de publicacao.csv
        self.stdout.write(self.style.NOTICE('Importando dados de publicacao.csv...'))
        with open(caminho_publicacoes, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    empresa = Empresa.objects.get(id_empresa=row['empresa_id'])
                    Publicacao.objects.create(
                        foto=row['foto'],
                        titulo_prato=row['titulo_prato'],
                        local=row['local'],
                        cidade=row['cidade'],
                        empresa=empresa,  # Relacionando a empresa
                    )
                except Empresa.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Empresa com id {row["empresa_id"]} não existe. Pulando...'))
                    continue
        self.stdout.write(self.style.SUCCESS('Dados de publicações importados com sucesso!'))
