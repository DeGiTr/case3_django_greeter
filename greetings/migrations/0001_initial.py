from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VisitorName",
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
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
            ],
            options={
                "verbose_name": "Имя посетителя",
                "verbose_name_plural": "Имена посетителей",
                "ordering": ["-id"],
            },
        ),
    ]
