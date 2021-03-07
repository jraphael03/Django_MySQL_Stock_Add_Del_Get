from django.db import models

# CREATING DATABASE MODEL    # CREATED A TABLE UNDER THE NAME quotes_stock
class Stock(models.Model):
    ticker = models.CharField( max_length=10 )          # VALUE NAME, TYPE OF VALUE

    def __str__(self):
        return self.ticker
