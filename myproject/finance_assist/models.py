from django.db import models



class ActionName(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class CategoryName(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Action(models.Model):
    action_name  = models.ForeignKey(ActionName, on_delete=models.CASCADE)
    category_name = models.ForeignKey(CategoryName, on_delete=models.CASCADE)
    action_count = models.IntegerField()
    action_date = models.DateTimeField('date action created')
    def __str__(self):
        return str(self.action_count)
