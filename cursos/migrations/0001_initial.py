# Generated by Django 5.1.4 on 2025-03-18 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instituicoes', '0005_blog_contacto_noticia_sobrenos_delete_inscricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='categorias/')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('duracao', models.CharField(max_length=100)),
                ('preco', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True)),
                ('nivel', models.CharField(choices=[('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')], max_length=100)),
                ('modalidade', models.CharField(choices=[('Presencial', 'Presencial'), ('Online', 'Online')], max_length=100)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens_cursos/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('destaque', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='cursos.categoria')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cursos', to='instituicoes.instituicao')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data_inscricao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], default='Pendente', max_length=50)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=10, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], max_length=10, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricoes', to='cursos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituicoes.instituicao')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilInstrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biografia', models.TextField()),
                ('titulo', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to='instrutores/')),
                ('cursos', models.IntegerField()),
                ('estudantes', models.IntegerField()),
                ('avaliacao', models.FloatField()),
                ('especializacoes', models.TextField()),
                ('contato', models.CharField(max_length=255)),
                ('instrutor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cursos.instrutor')),
            ],
        ),
    ]
