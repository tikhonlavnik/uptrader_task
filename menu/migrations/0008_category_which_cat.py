# Generated by Django 4.1.5 on 2023-01-28 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_category_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='which_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='which_menu_cat', to='menu.menu'),
        ),
    ]
