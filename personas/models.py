from django.db import models

# Create your models here.
class persona(models.Model):
    SAL='salvar'
    ALI='aliado'
    PAT='patrocinador'
    ENE='enemigo'
    COM='compañero'  
    CHOICES = [
        (SAL, 'salvar'),
        (ALI, 'aliado'),
        (PAT, 'patrocinador'),
        (ENE, 'enemigo'),
        (COM, 'compañero'),
        
    ]
    relacion= models.CharField(
        max_length=14,
        choices=CHOICES,
        default=SAL,
    )
    nombre = models.CharField(
        max_length=100,
    )
   
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.relacion= self.relacion
        self.nombre = self.nombre.upper()
        super(persona, self).save()
    
    class Meta:
        verbose_name_plural = "personas"