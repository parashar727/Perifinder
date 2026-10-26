from django.db import models
from django.db.models import ForeignKey

class Item(models.Model):

    brand = models.CharField(max_length=100)

    name = models.CharField(max_length=200)

    # ITEM_CATEGORIES = [
    #     ("KB", "Keyboard"),
    #     ("MS", "Mouse"),
    #     ("CL", "Controller"),
    # ]
    # category = models.CharField(max_length=3, choices=ITEM_CATEGORIES, default="MS")

    description = models.TextField()

    CONNECT_CATEGORIES = [
        ("24", "Wired + 2.4 GHz"),
        ("WD", "Wired"),
        ("TR", "Tri-Mode (Wired + 2.4 GHz + Bluetooth)"),
    ]
    connectivity = models.CharField(max_length=3,choices=CONNECT_CATEGORIES, default="WD")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Keyboard(Item):
    LAYOUTS = [
        ("80%", "80%"),
        ("100%", "100%"),
        ("75%", "75%"),
        ("60%", "60%"),
    ]
    layout = models.CharField(max_length=5, choices=LAYOUTS, default="80%")

    SWITCH_CATEGORIES = [
        ("LN", "Linear"),
        ("CL", "Clicky"),
        ("MG", "Magnetic"),
        ("TC", "Tactile"),
    ]

    switch_type = models.CharField(max_length=3, choices=SWITCH_CATEGORIES, default="LN")

    switch_name = models.CharField(max_length=100, blank=True)

    plate_material = models.CharField(max_length=100, blank=True)

    TECH_CATEGORIES = [
        ("HE", "Hall-effect"),
        ("MC", "Mechanical"),
    ]
    technology = models.CharField(max_length=3, choices=TECH_CATEGORIES, default="MC")

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    url = models.URLField()



class Listing(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=7, decimal_places=2)

    url = models.URLField(max_length=400)

    stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['price', 'id']

        constraints = [
            models.UniqueConstraint(fields=['vendor', 'url'], name='unique_vendor_listing_url'),
        ]