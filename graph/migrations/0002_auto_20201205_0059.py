# Generated by Django 3.1.4 on 2020-12-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='connection',
            field=models.ManyToManyField(blank=True, null=True, related_name='_node_connection_+', to='graph.Node'),
        ),
    ]
