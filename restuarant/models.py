from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False)

    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    MENU_CHOICES = (
        ("Appetisers", "Appetisers"),
        ("Salads", "Salads"),
        ("Starters", "Starters"),
        ("Main_Dishes", "Main_Dishes"),
    )
    title = models.CharField(max_length=50, choices=MENU_CHOICES)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
