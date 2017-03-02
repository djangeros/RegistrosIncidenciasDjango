#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode, force_unicode
from django import forms

class Incidencia(models.Model):
	fecharepo = models.DateField(auto_now_add=True, verbose_name='Fecha Reporte:')
	docrepo  = models.CharField(max_length=60, verbose_name='Documento Reporte:', blank=True)
	Regrepo = models.CharField(max_length=6, verbose_name='Registro Usuario Reporta:')
	descripcion = models.TextField(max_length=1000, verbose_name='Descripción Reporte:')
	uuoorepo = models.CharField(max_length=10, verbose_name='UUOO Reporte:')
	direccion = models.CharField(max_length=200, verbose_name='Dirección UUOO Reporte:')
	imagenini = models.ImageField(upload_to='reportes1', verbose_name='Registro Fotográfico Inicial:')
	solucionpla = models.TextField(max_length=1000, verbose_name='Solucion Planteada:', blank=True)
	flg_solucion = models.CharField(max_length=1, default=0)
	flg_cierre = models.CharField(max_length=1, default=0)

	def __unicode__(self):
		return str(self.pk)
		
class Solucion(models.Model):
    incidencia = models.ForeignKey(Incidencia, verbose_name='N° Incidencia:')
    uuoosol = models.CharField(max_length=10, verbose_name='UUOO Emite Requerimiento:')
    fechasol = models.DateField(auto_now_add=True, verbose_name='Fecha Asignada de Atención Reporte:')
    fechaeje = models.DateField(auto_now_add=False, verbose_name='Fecha Asignada de solucion Reporte:')
    uuooati = models.CharField(max_length=10, verbose_name='UUOO Area Usuaria que Atiende:')
    regsup = models.CharField(max_length=10, verbose_name='Supervisor OSA que Atiende:')
    tipo_ate = models.CharField(max_length=50, verbose_name='Tipo de Atención:')
    reguosa = models.CharField(max_length=6, verbose_name='Registro Usuario OSA que Atiende:')

    def __unicode__(self):
        return str(self.pk)

class Cierre(models.Model):
	solucion = models.ForeignKey(Incidencia, verbose_name='N° Incidencia:')
	fechaejec = models.DateField(auto_now_add=True, verbose_name='Fecha Ejecutada de Atención:')
	comentario = models.TextField(max_length=350, verbose_name='Solución Atendida:')
	imagenfin = models.ImageField(upload_to='reportes2', verbose_name='Registro Fotográfico Final:', blank=True)
	
	def __unicode__(self):
		return str(self.pk)
