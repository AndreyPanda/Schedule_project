# Generated by Django 4.1.5 on 2023-05-24 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialization",
            name="visit_duration",
            field=models.IntegerField(default=30),
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_name", models.CharField(max_length=255)),
                ("first_name", models.CharField(max_length=255)),
                ("fathers_name", models.CharField(max_length=255)),
                ("photo", models.ImageField(null=True, upload_to="photos/%Y/%m/%d/")),
                ("education", models.TextField(max_length=2000)),
                ("description", models.TextField(max_length=5000)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("working_start_time", models.DateTimeField(null=True)),
                ("working_finish_time", models.DateTimeField(null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "specialization",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="doctors_specialization",
                        to="main.specialization",
                    ),
                ),
            ],
        ),
    ]
