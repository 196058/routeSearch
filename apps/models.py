from msvcrt import CRT_ASSEMBLY_VERSION

from django.db import models


class Admin(models.Model):
    user_name = models.CharField(max_length=192, blank=True, null=True)
    pass_word = models.CharField(max_length=192, blank=True, null=True)
    mail = models.CharField(max_length=192, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Field(models.Model):
    paddy = models.ForeignKey('Paddy', models.DO_NOTHING, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field'


class Inquiry(models.Model):
    inquiry_no = models.AutoField(primary_key=True)
    inquiry_id = models.CharField(max_length=192, blank=True, null=True)
    title = models.CharField(max_length=192, blank=True, null=True)
    contents = models.CharField(max_length=192, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inquiry'


class Mecainfo(models.Model):
    meca_id = models.AutoField(primary_key=True)
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id', blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    full_length = models.IntegerField(blank=True, null=True)
    full_width = models.IntegerField(blank=True, null=True)
    plant = models.IntegerField(blank=True, null=True)

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
    user_name = models.CharField(max_length=192, blank=True, null=True)
    pass_word = models.CharField(max_length=192, blank=True, null=True)
    mail = models.CharField(max_length=192, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'



