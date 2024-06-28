# Generated by Django 4.2 on 2024-06-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0002_lesson"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="number",
            field=models.PositiveIntegerField(
                default=1, verbose_name="Порядковый номер урока"
            ),
            preserve_default=False,
        ),
    ]