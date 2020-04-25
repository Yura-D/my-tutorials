from djongo import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        if self.name:
            return self.name


class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    link = models.TextField()
    comment = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to=Category,
                                 on_delete=models.CASCADE)
    
    def __str__(self):
        if self.name:
            return self.name
