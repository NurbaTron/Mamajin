from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=15)

    def register(self):
        self.save

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExisits(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False    

    def __str__(self):
        return self.first_name
