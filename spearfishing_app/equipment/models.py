from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Equipment(models.Model):
    GUN_CHOICES = (
        ('Cressi', 'Cressi'),
        ('Beuchat', 'Beuchat'),
        ('Omer', 'Omer'),
        ('Mares', 'Mares'),
        ('Salvimar', 'Salvimar'),
        ('Seac', 'Seac'),
        ('Epsealon', 'Epsealon'),
        ('Spetton', 'Spetton'),
        ('C4', 'C4'),
    )

    GUN_MATERIAL_CHOICES = (
        ('Wood', 'Wood'),
        ('Aluminium', 'Aluminium'),
        ('Poliplast', 'Poliplast'),
        ('Carbon Fiber', 'Carbon Fiber'),
        ('Other', 'Other'),
    )

    GUN_LENGTH_CHOICES = (
        ('Lower than 65cm', 'Lower than 65cm'),
        ('65cm', '65cm'),
        ('70cm', '70cm'),
        ('72cm', '72cm'),
        ('75cm', '75cm'),
        ('80cm', '80cm'),
        ('82cm', '82cm'),
        ('85cm', '85cm'),
        ('90cm', '90cm'),
        ('95cm', '95cm'),
        ('100cm', '100cm'),
        ('110cm', '110cm'),
        ('115cm', '115cm'),
        ('120cm', '120cm'),
        ('125cm', '125cm'),
        ('Longer than 125cm', 'Longer than 125cm'),
    )

    BANDS_CHOICES = (
        ('Less than 13mm', 'Less than 13mm'),
        ('13mm', '13mm'),
        ('13.5mm', '13.5mm'),
        ('14mm', '14mm'),
        ('14.5mm', '14.5mm'),
        ('16mm', '16mm'),
        ('18mm', '18mm'),
        ('20mm', '20mm'),
        ('20mm+', '20mm+'),
    )

    BANDS_BRAND_CHOICES = (
        ('SigalSub', 'SigalSub'),
        ('Cressi', 'Cressi'),
        ('Beuchat', 'Beuchat'),
        ('Epsealon', 'Epsealon'),
        ('Salvimar', 'Salvimar'),
        ('Dunlop', 'Dunlop'),
        ('Other', 'Other'),
    )

    FINS_BRAND_CHOICES = (
        ('Cressi', 'Cressi'),
        ('Beuchat', 'Beuchat'),
        ('Omer', 'Omer'),
        ('Mares', 'Mares'),
        ('Salvimar', 'Salvimar'),
        ('Seac', 'Seac'),
        ('Epsealon', 'Epsealon'),
        ('Spetton', 'Spetton'),
        ('C4', 'C4'),
    )

    FINS_MATERIAL_CHOICES = (
        ('Plastic', 'Plastic'),
        ('Poli-Plastic', 'Poli-plastic'),
        ('Carbon', 'Carbon'),
        ('Other', 'Other'),
    )

    gun_model = models.CharField(
        max_length=20,
        choices=GUN_CHOICES,
    )

    gun_material = models.CharField(
        max_length=20,
        choices=GUN_MATERIAL_CHOICES,
    )

    gun_length = models.CharField(
        max_length=30,
        choices=GUN_LENGTH_CHOICES,
    )

    gun_image = models.URLField(
        null=True,
        blank=True,
    )

    bands = models.CharField(
        max_length=30,
        choices=BANDS_CHOICES,
    )

    bands_brand = models.CharField(
        max_length=30,
        choices=BANDS_BRAND_CHOICES,
    )

    bands_image = models.URLField(
        null=True,
        blank=True,
    )

    fins_model = models.CharField(
        max_length=20,
        choices=FINS_BRAND_CHOICES,
    )

    fins_material = models.CharField(
        max_length=20,
        choices=FINS_MATERIAL_CHOICES,
    )

    fins_image = models.URLField(
        null=True,
        blank=True,
    )

    additional_info = models.TextField(
        max_length=250,
        null=True,
        blank=True,
    )

    owner = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
