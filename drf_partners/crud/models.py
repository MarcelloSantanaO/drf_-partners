from django.db import models
from datetime import datetime

from django.db.models.fields import CharField

class Partner(models.Model):
    cnpj = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    partnership_status = models.CharField(max_length=20, default="Not Initiated")
    uf = models.CharField(max_length=2, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    cnpj_status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Partner: Nome: {self.name} /CNPJ: {self.cnpj} /Create at: {self.created_at}'