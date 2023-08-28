from django.contrib import admin
from .models import Product,TagLine,AboutUs,Image,ContactForm
# Register your models here.\


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Product)
admin.site.register(TagLine)
admin.site.register(AboutUs)
admin.site.register(Image)
admin.site.register(ContactForm, ContactFormAdmin)