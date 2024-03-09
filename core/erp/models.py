from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoría')
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to='product/{}'.format(category), null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    surname = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    birthday = models.DateField(verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=50, verbose_name='Género')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    sell_date = models.DateField(verbose_name='Fecha de venta')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='IVA')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return self.client
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['sell_date']

class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Venta')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    amount = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')

    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de venta'
        ordering = ['id']



# class Type(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
#     description = models.TextField(max_length=500, verbose_name='Descripción', null=True, blank=True)

#     def __str__(self):
#         return '({}) {}'.format(self.id, self.name)
    
#     class Meta:
#         verbose_name = 'Tipo'
#         verbose_name_plural = 'Tipos'
#         #db_table = 'tipo'
#         ordering = ['id']

# class Category(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre')
#     description = models.TextField(max_length=500, verbose_name='Descripción', null=True, blank=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Categoría'
#         verbose_name_plural = 'Categorías'
#         #db_table = 'categoria'
#         ordering = ['id']

# class Employee(models.Model):
#     category = models.ManyToManyField(Category, verbose_name='Categorías')
#     type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Tipo')
#     names = models.CharField(max_length=150, verbose_name='Nombres')
#     dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
#     date_joined = models.DateField(verbose_name='Fecha de registro', auto_now=True)
#     date_created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=True)
#     date_updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now_add=True)
#     age = models.PositiveIntegerField(default=0)
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     state = models.BooleanField(default=True)
#     #gender = models.CharField(max_length=50, verbose_name='Género')
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
#     cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

#     def __str__(self):
#         return self.names
    
#     class Meta:
#         verbose_name = 'Empleado'
#         verbose_name_plural = 'Empleados'
#         #db_table = 'empleado'
#         ordering = ['id']