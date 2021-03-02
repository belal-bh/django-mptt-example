from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Node(MPTTModel):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    connections = models.ManyToManyField('self', null=True, blank=True, related_name='connections')
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['username']

    def __str__(self):
        return f"{self.id}-@{self.username} -{self.name}"
    