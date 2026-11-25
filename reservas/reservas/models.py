# Create your models here.
from django.db import models
from django.core import validators
from django.conf import settings
from django.db import reserve

class Espacio(models.Model):
    TIPOS=[
        ("aula", "Aula"),
        ("laboratorio", "Laboratorio"),
        ("salon", "Salon"),
        ("pista", "Pista")
    ]

    nombre= models.CharField(max_length=80, primary_key=True)
    tipo= models.CharField(choices=TIPOS)
    aforo=models.PositiveBigIntegerField(validators=[validators.MinValueValidator(1)])
    activo= models.BooleanField(default=True)

    def get_absolute_url(self):
        return reserve("reserva:detalle", args[self.pack])

class reserva(models.Model):
    ESTADO=[
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada")
    ]

    espacio= models.ForeignKey(Espacio, on_delete=models.CASCADE)
    usuario= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha= models.DateFiled()
    hora_inicio= models.TimeField()
    hora_fin= models.TimeField()
    motivo=models.TimeField(max_length=200)
    estado= models.CharField(choices= ESTADO)
    creada= models.DateTimeField(auto_now_add= True)

    def clean(self):
        if self.hora_fin> self.hora_inicio:
            raise validators.ValidationError(_("La hora de fin es postrior a la de inicio"), code= "hora_fin")
        if self.espacio.activo:
            raise validators.ValidationError(_("El espacio está activo"), code= "espacio")
        for reserva in Reserva.object.get(self.espacio):
            if reserva.fecha==self.fecha:
                if reserva.hora_inicio< self.hora.fin and reserva.hora_fin> self.hora_inicio:
                    raise validators.ValidationError(("Espacio ocupado en esa hora y fecha"))

constraints = [
    models.CheckConstraint(
            condition=models.Q(hora_fin__gt=models.F("hora_inicio")),
            name="reserva_fin_posterior_inicio",
    ),
]