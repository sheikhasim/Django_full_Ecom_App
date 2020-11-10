# Generated by Django 3.1 on 2020-11-04 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0011_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('code', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image_id', models.IntegerField(blank=True, default=0, null=True)),
                ('qunatity', models.IntegerField(blank=True, default=1, null=True)),
                ('price', models.FloatField(default=0)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.size')),
            ],
        ),
    ]
