# Generated by Django 4.2.7 on 2023-11-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client_id', models.CharField(max_length=100)),
                ('client_secret', models.CharField(max_length=100)),
                ('certificado_producao', models.FileField(blank=True, null=True, upload_to='efi/credentials/certificados/')),
                ('certificado_homologacao', models.FileField(blank=True, null=True, upload_to='efi/credentials/certificados/')),
                ('sandbox', models.BooleanField(default=True)),
            ],
        ),
    ]
