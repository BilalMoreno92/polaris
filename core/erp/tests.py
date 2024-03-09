from config.wsgi import *

from core.erp.models import Type, Category, Employee

# Listar
# query = Type.objects.all()
# print(query)

# Inserción
#Type(name='Prueba', description='Tipo de prueba').save()
#Type(name='Prueba', description='Tipo de prueba').save()

# Clave no existe
#t = Type.objects.get(id=8)

# Edición
# try:
#     t = Type.objects.get(id=1)
#     t.name = 'Presidente'
#     t.save()
# except Exception as e:
#     print(e)

# Eliminación
# t = Type.objects.get(id=3)
# t.delete()

# print(t)

# obj = Type.objects.filter(name__contains='Pre')
# obj = Type.objects.filter(name__icontains='pre').query
# obj = Type.objects.filter(name__startswith='pre')
# obj = Type.objects.filter(name__endswith='a').query
# obj = Type.objects.filter(name__in=['Presidente', 'Accionista']).count()
# obj = Type.objects.filter(name__in=['Presidente', 'Accionista']).exclude(id = 1)

# print(obj)

for i in Type.objects.filter(name__in=['Presidente', 'Accionista']):
    print(i.name, i.description)