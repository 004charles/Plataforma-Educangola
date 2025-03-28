# Generated by Django 5.1.4 on 2024-12-27 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultoriaTCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')], default='pendente', max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultorias', to='biblioteca.usuariobiblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='Tese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('orientador', models.CharField(max_length=255)),
                ('ano_publicacao', models.PositiveIntegerField()),
                ('resumo', models.TextField()),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teses', to='biblioteca.biblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='EmprestimoTese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField(auto_now_add=True)),
                ('data_devolucao', models.DateField()),
                ('devolvido', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.usuariobiblioteca')),
                ('tese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.tese')),
            ],
        ),
    ]
