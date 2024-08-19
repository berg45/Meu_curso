from rest_framework import serializers
from apps.Core.models import Clientes


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state"]

    def validate_title(self, value):
       if len(value) < 5:
           raise serializers.ValidationError("O título deve ter pelo menos 5caracteres.")
       return value
