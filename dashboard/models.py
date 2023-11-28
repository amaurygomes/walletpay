from django.db import models

class API(models.Model):
    name = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    certificado_producao = models.FileField(upload_to='efi/credentials/certificados/', blank=True, null=True)
    certificado_homologacao = models.FileField(upload_to='efi/credentials/certificados/', blank=True, null=True)
    sandbox = models.BooleanField(default=True)

    def __str__(self):
        return self.name
