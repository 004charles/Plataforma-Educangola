# Generated by Django 5.1.4 on 2024-12-27 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaBiblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('site', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='bibliotecas/logos/')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.categoriabiblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('editora', models.CharField(max_length=100)),
                ('ano_publicacao', models.PositiveIntegerField()),
                ('isbn', models.CharField(blank=True, max_length=13, unique=True)),
                ('disponivel', models.BooleanField(default=True)),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='biblioteca.biblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioBiblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='biblioteca.biblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField(auto_now_add=True)),
                ('data_devolucao', models.DateField()),
                ('devolvido', models.BooleanField(default=False)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.usuariobiblioteca')),
            ],
        ),
    ]