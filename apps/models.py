from msvcrt import CRT_ASSEMBLY_VERSION

from django.db import models


class Field(models.Model):
    paddy = models.ForeignKey('Paddy', models.DO_NOTHING, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field'


class Mecainfo(models.Model):
    meca_id = models.AutoField(primary_key=True)
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    full_length = models.IntegerField(blank=True, null=True)
    full_width = models.IntegerField(blank=True, null=True)
    jousu = models.IntegerField(blank=True, null=True)
    joukan = models.IntegerField(blank=True, null=True)
    kabuma = models.IntegerField(blank=True, null=True)
    adjusting = models.IntegerField(blank=True, null=True)
    workingspeed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mecainfo'


class Paddy(models.Model):
    paddy_id = models.AutoField(primary_key=True)
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paddy'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=192)
    user_name = models.CharField(max_length=192, blank=True, null=True)
    pass_word = models.CharField(max_length=192, blank=True, null=True)
    mail = models.CharField(max_length=192, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


