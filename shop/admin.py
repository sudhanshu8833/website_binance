from django.contrib import admin

# Register your models here.

from .models import User1,orders,positions,groups
admin.site.register(User1)
admin.site.register(orders)
admin.site.register(positions)
admin.site.register(groups)

