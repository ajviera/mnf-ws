# -*- coding: utf-8 -*-
from django.contrib import admin
from restapp.models import *

admin.site.register(Product)
admin.site.register(Favourite)
admin.site.register(Order)

# Para sacar 'Pestañas' de la ventana de admin
# admin.site.unregister(Group)