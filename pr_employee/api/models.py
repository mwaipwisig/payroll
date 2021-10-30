from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Company(models.Model):
    class Meta:
        db_table = 'tb_companies'

    name = models.CharField(max_length=100, unique=True)
    ceo = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    company_slogan = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    last_update_date = models.DateField(auto_now=True)
    last_update_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = str(self.name).upper()
        return super(Company, self).save()


class Office(models.Model):
    ch_mikoa = (
        ('Dodoma', 'Dodoma'),
        ('Arusha', 'Arusha'),
        ('Kilimanjaro', 'Kilimanjaro'),
        ('Tanga', 'Tanga'),
        ('Morogoro', 'Morogoro'),
        ('Pwani', 'Pwani'),
        ('Dar es Salaam', 'Dar es Salaam'),
        ('Lindi', 'Lindi'),
        ('Mtwara', 'Mtwara'),
        ('Ruvuma', 'Ruvuma'),
        ('Iringa', 'Iringa'),
        ('Mbeya', 'Mbeya'),
        ('Songwe', 'Songwe'),
        ('Singida', 'Singida'),
        ('Tabora', 'Tabora'),
        ('Rukwa', 'Rukwa'),
        ('Kigoma', 'Kigoma'),
        ('Shinyanga', 'Shinyanga'),
        ('Kagera', 'Kagera'),
        ('Mwanza', 'Mwanza'),
        ('Mara', 'Mara'),
        ('Manyara', 'Manyara'),
        ('Njombe', 'Njombe'),
        ('Katavi', 'Katavi'),
        ('Simiyu', 'Simiyu'),
        ('Geita', 'Geita'),
        ('Unguja Kaskazini', 'Unguja Kaskazini'),
        ('Unguja Kusini', 'Unguja Kusini'),
        ('Unguja Mjini Magharibi', 'Unguja Mjini Magharibi'),
        ('Pemba Kaskazini', 'Pemba Kaskazini'),
        ('Pemba Kusini', 'Pemba Kusini')
    )

    class Meta:
        db_table = 'tb_office'
        unique_together = ['company', 'name', 'region', 'location']
        ordering = ['-id']

    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    pay_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(auto_now=True)
    last_update_time = models.DateField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=ch_mikoa)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.company.name} '


class Department(models.Model):
    d_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Employee(models.Model):
    class Meta:
        db_table = 'tb_employee'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100, blank=True, null=True)
    l_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos/employee', blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='user_office', null=True, blank=True)
    companies = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='user_branches')
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    last_update_date = models.DateField(auto_now=True)
    last_update_time = models.DateField(auto_now=True)

    def name(self):
        return f'{self.user.get_full_name()} - {self.user.username}'

    def __str__(self):
        return self.user.username
