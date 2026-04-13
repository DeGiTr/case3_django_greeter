from django.db import models


class VisitorName(models.Model):
    name = models.CharField("Имя", max_length=100)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Имя посетителя"
        verbose_name_plural = "Имена посетителей"

    def __str__(self) -> str:
        return self.name
