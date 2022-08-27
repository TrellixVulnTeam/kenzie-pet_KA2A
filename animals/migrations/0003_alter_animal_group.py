# Generated by Django 4.1 on 2022-08-11 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0003_alter_group_name_alter_group_scientific_name"),
        ("animals", "0002_animal_traits_alter_animal_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="animals",
                to="groups.group",
            ),
        ),
    ]
