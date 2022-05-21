# Generated by Django 3.2 on 2022-05-14 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prefered_unit', models.CharField(choices=[('g', 'gram'), ('kg', 'kilogram'), ('ml', 'mililitr'), ('l', 'litr')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='IntegrentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_visible', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='RecipeIntegrents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('g', 'gram'), ('kg', 'kilogram'), ('ml', 'mililitr'), ('l', 'litr')], max_length=2)),
                ('integrent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipe.integrent')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='integrents',
            field=models.ManyToManyField(through='recipe.RecipeIntegrents', to='recipe.Integrent'),
        ),
        migrations.AddField(
            model_name='integrent',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipe.integrenttype'),
        ),
    ]
