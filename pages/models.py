from django.db import models
from django.utils.timezone import now

# Create your models here.
class Login(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  password2 = models.CharField(max_length=50)
  

class PrintOrder(models.Model):
    PRINTING_TYPE_CHOICES = [
        ('color', 'ألوان'),
        ('black', 'أبيض وأسود'),
    ]
    
    PAPER_SIZE_CHOICES = [
        ('A4', 'A4'),
        ('A3', 'A3'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'كاش'),
        ('vod-cash', 'محفظة إلكترونية'),
    ]

    printing_type = models.CharField(max_length=10, choices=PRINTING_TYPE_CHOICES,null=True,blank=True, verbose_name="نوع الطباعة")
    paper_size = models.CharField(max_length=10, choices=PAPER_SIZE_CHOICES,null=True,blank=True, verbose_name="حجم الورق")
    paper_number = models.PositiveIntegerField(verbose_name="عدد الورق")
    copy_number = models.PositiveIntegerField(verbose_name="عدد النسخ")
    paper_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الورقة")
    other = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="مبالغ إضافية")
    pay = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES,null=True,blank=True, verbose_name="طريقة الدفع")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإجمالي")

    created_at = models.DateTimeField(default=now)




class Payments(models.Model):
  cash_out = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
  notes = models.TextField(null=True, blank=True)
  created_at2 = models.DateTimeField(default=now)
  
class Come_in(models.Model):
  cash_in = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
  notes = models.TextField(null=True, blank=True)
  created_at3 = models.DateTimeField(default=now)  
  