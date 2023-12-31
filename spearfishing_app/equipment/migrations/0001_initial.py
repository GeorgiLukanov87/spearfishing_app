# Generated by Django 4.2.2 on 2023-06-29 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gun_model', models.CharField(choices=[('Cressi', 'Cressi'), ('Beuchat', 'Beuchat'), ('Omer', 'Omer'), ('Mares', 'Mares'), ('Salvimar', 'Salvimar'), ('Seac', 'Seac'), ('Epsealon', 'Epsealon'), ('Spetton', 'Spetton'), ('C4', 'C4')], max_length=20)),
                ('gun_material', models.CharField(choices=[('Wood', 'Wood'), ('Aluminium', 'Aluminium'), ('Poliplast', 'Poliplast'), ('Carbon Fiber', 'Carbon Fiber'), ('Other', 'Other')], max_length=20)),
                ('gun_length', models.CharField(choices=[('Lower than 65cm', 'Lower than 65cm'), ('65cm', '65cm'), ('70cm', '70cm'), ('72cm', '72cm'), ('75cm', '75cm'), ('80cm', '80cm'), ('82cm', '82cm'), ('85cm', '85cm'), ('90cm', '90cm'), ('95cm', '95cm'), ('100cm', '100cm'), ('110cm', '110cm'), ('115cm', '115cm'), ('120cm', '120cm'), ('125cm', '125cm'), ('Longer than 125cm', 'Longer than 125cm')], max_length=30)),
                ('gun_image', models.URLField(blank=True, null=True)),
                ('bands', models.CharField(choices=[('Less than 13mm', 'Less than 13mm'), ('13mm', '13mm'), ('13.5mm', '13.5mm'), ('14mm', '14mm'), ('14.5mm', '14.5mm'), ('16mm', '16mm'), ('18mm', '18mm'), ('20mm', '20mm'), ('20mm+', '20mm+')], max_length=30)),
                ('bands_brand', models.CharField(choices=[('SigalSub', 'SigalSub'), ('Cressi', 'Cressi'), ('Beuchat', 'Beuchat'), ('Epsealon', 'Epsealon'), ('Salvimar', 'Salvimar'), ('Dunlop', 'Dunlop'), ('Other', 'Other')], max_length=30)),
                ('bands_image', models.URLField(blank=True, null=True)),
                ('fins_model', models.CharField(choices=[('Cressi', 'Cressi'), ('Beuchat', 'Beuchat'), ('Omer', 'Omer'), ('Mares', 'Mares'), ('Salvimar', 'Salvimar'), ('Seac', 'Seac'), ('Epsealon', 'Epsealon'), ('Spetton', 'Spetton'), ('C4', 'C4')], max_length=20)),
                ('fins_material', models.CharField(choices=[('Plastic', 'Plastic'), ('Poli-Plastic', 'Poli-plastic'), ('Carbon', 'Carbon'), ('Other', 'Other')], max_length=20)),
                ('fins_image', models.URLField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, max_length=250, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
