from django.db import models

# Create your models here.
class mision(models.Model):
    CO='COD'
    CP='CP'
    SO='EL'
    RES='RES'
    PRO='LI'
    LID='AS'
    CHOICES = [
        (CO, 'clasificado'),
        (CP, 'capturar'),
        (SO, 'eliminar'),
        (RES, 'rescatar'),
        (PRO, 'proteger'),
        (LID, 'liderar'),
    ]
    misiones= models.CharField(
        max_length=3,
        choices=CHOICES,
        default=CO,
    )

    nombreClave  = models.CharField(
        max_length=100,
        unique=True,
    )
    fecha=models.DateField()
    fechaActivada=models.DateField(auto_now=True)
    lugar=models.CharField(
         max_length=100,

    )



    def __str__(self):
        return '{}'.format(self.misiones)
    
    def save(self):
        self.misiones= self.misiones
        self.nombreClave = self.nombreClave
        super(mision, self).save()
    
    class Meta:
        verbose_name_plural = "misiones"