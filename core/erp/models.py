from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    description = models.TextField(max_length=500, verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        #db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        #db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    category = models.ManyToManyField(Category, verbose_name='Categorías')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Tipo')
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    date_joined = models.DateField(verbose_name='Fecha de registro', auto_now=True)
    date_created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=True)
    date_updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50, verbose_name='Género')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        #db_table = 'empleado'
        ordering = ['id']