from rest_framework import serializers
from .models import Account
from .controller import VerifyAccount



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, attrs):
        print(attrs)
        reply = VerifyAccount(attrs)
        if reply == "ERROR CSRF": raise serializers.ValidationError("ERROR CSRF")
        elif reply == "CONSUL INVALID": raise serializers.ValidationError("CONSUL INVALIDO")
        elif reply == "CAS INVALID": raise serializers.ValidationError("CAS INVALIDO")
        elif reply == "MONTHS INVALID": raise serializers.ValidationError("MES INVALIDO")
        elif reply == "STATUS INVALID": raise serializers.ValidationError("ESTADO INVALIDO")
        elif reply == "TYPE_ACOT INVALID": raise serializers.ValidationError("TIPO DE CUENTA INVALIDA")
        elif reply == "INCORRECT PASSWORD": raise serializers.ValidationError("CONTRASEÑA INCORRECTA")
        elif reply == "NOT IVR": raise serializers.ValidationError("IVR NO ENCONTRADO")
        elif reply == "NOT READY": raise serializers.ValidationError("LA CUENTA NO ESTA LISTA")
        elif reply == "READY": return super().validate(attrs)
        else: raise serializers.ValidationError("ERROR NO IDENTIFICADO")