from django.db import models
from django.core.exceptions import ValidationError

HOMBRE = 2
MUJER = 1
NEUTRO = 0
SEXO = [
    (NEUTRO, "Prefiero no decir"),
    (HOMBRE, "Hombre"),
    (MUJER, "Mujer"),
]

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=20)

    def __str__(self):
        cadena = f"( {self.id} ) {self.siglas}"
        return cadena

class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT, null=False)
    sexo = models.IntegerField(choices=SEXO, default=NEUTRO, null=False)
    fecha_nacimiento = models.DateField(null=False)

    def __str__(self):
        cadena = f"( {self.id} ) {self.nombre} de la escuela {self.escuela.siglas}"
        return cadena

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT, null=False)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, null=False)
    sexo = models.IntegerField(choices=SEXO, default=NEUTRO, null=False)
    fecha_nacimiento = models.DateField(null=False)

    def clean(self):
        if self.maestro_id and self.escuela_id:
            if self.maestro.escuela_id != self.escuela_id:
                raise ValidationError(
                    {"maestro": "El maestro debe pertenecer a la misma escuela que el alumno."}
                )


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


