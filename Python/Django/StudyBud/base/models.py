from django.db import models


class Room(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    # Salva o valor toda vez quem voce salva ele
    updated = models.DateTimeField(auto_now=True)
    # Salva ele uma vez que foi instanciado e não irá mudar
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
