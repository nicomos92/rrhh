from django.db import models

# Create your models here.
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length=60,blank= False,null= False)
    nombre = models.CharField(max_length=60,blank= False,null= False)
    legajo = models.CharField(max_length=30,blank= False,null= False)
    dni = models.CharField(max_length=30,blank= False)
    fechaNacimiento = models.DateField()
    fechaIngreso = models.DateField()
    cuit = models.IntegerField()
    telefono = models.IntegerField()
    email = models.CharField(max_length=60)
    sector = models.CharField(max_length=60,blank=True,default='')
    area = models.CharField(max_length=60,blank=True,default='')
    categoria = models.CharField(max_length=60,blank=True,default='')
    lugarDeTrabajo = models.CharField(max_length=60,blank=True,default='')
    regimen = models.CharField(max_length=10,blank=True,default='')


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    def __str__(self):
        return self.nombre +"  " +self.apellido

class Novedades(models.Model):
    id = models.AutoField(primary_key=True,null= False)
    fecha = models.DateTimeField(auto_now_add=True)
    select_tipoNovedad = (
        ('Cert','Cert'),
        ('Vacaciones','Vacaciones'),
        ('Licencia','Licencia'),
        ('Otro','Otro'),
    )
    tipoNovedad = models.CharField(max_length=30, choices=select_tipoNovedad)
    descripcion = models.TextField()
    tipodeacto = models.CharField(max_length=100)
    numero = models.IntegerField()
    adjunto = models.FileField()
    empleadoId = models.ForeignKey(Empleado,null=False,blank=False,on_delete=models.CASCADE)

class Familia(models.Model):
    id = models.AutoField   (primary_key=True)
    dni = models.IntegerField(default=0)
    apellido = models.CharField(max_length=60,null=False, blank=False)
    nombre = models.CharField(max_length=60,null=False, blank=False)
    fechaNacimiento = models.DateField()
    vinculo = models.CharField(max_length=20)
    empledoID =models.ForeignKey(Empleado,null=True,blank=False,on_delete=models.CASCADE)



