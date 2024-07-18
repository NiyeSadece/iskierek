# Generated by Django 4.2.13 on 2024-07-13 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("iskierek_site", "0006_student_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="club",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="iskierek_site.club",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="extracurricular",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="iskierek_site.extracurricular",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="sport",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="iskierek_site.sport",
            ),
        ),
    ]
