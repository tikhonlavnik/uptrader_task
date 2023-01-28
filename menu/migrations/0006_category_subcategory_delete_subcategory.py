# Generated by Django 4.1.5 on 2023-01-26 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='menu.category'),
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
