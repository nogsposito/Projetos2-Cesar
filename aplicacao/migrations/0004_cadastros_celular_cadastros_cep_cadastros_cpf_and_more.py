# Generated by Django 5.1.1 on 2024-10-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_remove_cadastros_comentarios_remove_cadastros_idade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastros',
            name='celular',
            field=models.IntegerField(default='Celular não informado'),
        ),
        migrations.AddField(
            model_name='cadastros',
            name='cep',
            field=models.IntegerField(default='CEP não informado'),
        ),
        migrations.AddField(
            model_name='cadastros',
            name='cpf',
            field=models.IntegerField(default='CPF não informado'),
        ),
        migrations.AddField(
            model_name='cadastros',
            name='idade',
            field=models.IntegerField(default='Idade não informada'),
        ),
        migrations.AddField(
            model_name='cadastros',
            name='numero',
            field=models.IntegerField(default='Número não informado'),
        ),
    ]