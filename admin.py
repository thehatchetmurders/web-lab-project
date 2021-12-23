# admin
# admin1234
from django.contrib import admin
from .models import Comments, Messages, Consult, Doctors, Department, Blogs
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Comments)
admin.site.register(Messages)
admin.site.register(Consult)
# admin.site.register(Account)
# admin.site.register(Doctors)
# admin.site.register(Department)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_show', 'slug', 'email','surname', 'specialization']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src = '{}' width = '60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Picture"

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_show', 'article']

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src = '{}' width = '60' />".format(obj.photo.url))
        return "None"

    image_show.__name__ = "Picture"