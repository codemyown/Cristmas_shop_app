from django.contrib import admin
from .models.contact import Contact
from .models.product import Product
from .models.blog import Blog


# Register your models here.


admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Blog)


