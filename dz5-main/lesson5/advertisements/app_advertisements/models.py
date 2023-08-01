from django.db import models

# Create your models here.

class Advertisement(models.Model):
    class Meta:
        db_table = "advertisements"
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг",help_text="укажите true, если торг уместен")
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    def __str__(self):
        return f"<{self.__class__.__name__}(id={self.id}, title={self.title}, price={self.price})>"

    #  >>> from app_advertisements.models import *
    #  >>> print(Advertisement.objects.get(id=1))
