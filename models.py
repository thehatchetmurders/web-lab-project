from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'

class Doctors(models.Model):
    name = models.CharField(max_length = 100)
    department = models.ForeignKey('Department', related_name = 'doctors', on_delete=models.CASCADE)
    slug = models.CharField(max_length = 100, db_index=True, unique=True, default='Cardiology')
    surname = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to='doctors/%Y/%m/%d', blank=True)
    email = models.CharField(max_length=100, default='test@mail.ru')
    specialization = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Doctors'
        verbose_name = 'Doctor'

    def get_absolute_url(self):
        return reverse('testapp:doctor_list_by_category', args=[self.slug])

class Department(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100, unique = True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Departments'
        verbose_name = 'Department'

    def get_absolute_url(self):
        return reverse('testapp:doctor_list_by_category', args=[self.slug])

# class Account(models.Model):
#     client_ID = models.ForeignKey('Consult',
#     on_delete=models.CASCADE,)
#     full_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     ph_num = models.CharField(max_length = 100)
#     password = models.CharField(max_length = 100)
#     def __str__(self):
#         return self.full_name
#     class Meta:
#         verbose_name_plural = 'Accounts'
#         verbose_name = 'Account'


class Messages(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length = 300)
    message = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Message'


class Consult(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    comment = models.CharField(max_length = 300)
    dep_ID = models.ForeignKey('Department',
    on_delete=models.CASCADE,)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Consults'
        verbose_name = 'Consult'

class Blogs(models.Model):
    title = models.CharField(max_length = 500)
    photo = models.ImageField(upload_to='doctors/%Y/%m/%d', blank=True)
    article = models.TextField()
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

