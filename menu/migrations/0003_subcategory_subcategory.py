# Generated by Django 4.1.5 on 2023-01-26 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_category_menu_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_2', to='menu.subcategory'),
            preserve_default=False,
        ),
    ]
