from django.urls import path, include
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets

from mi_aplicacion.models import Escuela, Maestro, Alumno

# Serializers define the API representation.
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "codename",
            "content_type",
        ]


class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        required=False
    )
    permission_details = PermissionSerializer(
        source="permissions",
        many=True,
        read_only=True
    )


    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "permissions",
            "permission_details",
        ]


    def create(self, validated_data):
        permissions = validated_data.pop("permissions", [])
        group = Group.objects.create(**validated_data)
        if permissions:
            group.permissions.set(permissions)
        return group


    def update(self, instance, validated_data):
        permissions = validated_data.pop("permissions", None)
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        if permissions is not None:
            instance.permissions.set(permissions)
        return instance




class UserSerializer(serializers.ModelSerializer):
    # Recibe IDs de grupos al crear/editar el usuario
    groups = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all(),
        required=False
    )
    group_details = GroupSerializer(
        source="groups",
        many=True,
        read_only=True
    )
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "groups",
            "group_details",
        ]


    def create(self, validated_data):
        groups = validated_data.pop("groups", [])
        password = validated_data.pop("password")


        user = User.objects.create(**validated_data)
        user.set_password(password)  # importante para hashear la contraseña
        user.save()


        if groups:
            user.groups.set(groups)


        return user


    def update(self, instance, validated_data):
        groups = validated_data.pop("groups", None)
        password = validated_data.pop("password", None)


        for attr, value in validated_data.items():
            setattr(instance, attr, value)


        if password:
            instance.set_password(password)


        instance.save()


        if groups is not None:
            instance.groups.set(groups)


        return instance


class EscuelaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escuela
        fields = "__all__"

class MaestroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maestro
        fields = "__all__"

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"

    def validate(self, attrs):
        escuela = attrs.get("escuela")
        maestro = attrs.get("maestro")

        if self.instance:
            escuela = escuela or self.instance.escuela
            maestro = maestro or self.instance.maestro

        if escuela and maestro and maestro.escuela_id != escuela.id:
            raise serializers.ValidationError({
                "maestro": "El maestro debe pertenecer a la misma escuela que el alumno."
            })


        return attrs

