# -*- coding: utf-8 -*-
from django.contrib import admin
from src.models import *

admin.site.register( Note )
admin.site.register( Tag )

# Para sacar 'Pestañas' de la ventana de admin
# admin.site.unregister(Group)