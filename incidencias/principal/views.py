# -*- coding: utf-8 -*-
from principal.models import Incidencia, Solucion, Cierre
from principal.forms import IncidenciaForm, SolucionForm, ContactoForm, CierreForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Añadir al inicio
from django.contrib.auth.hashers import make_password

# Modificar al inicio
from .forms import (EditarContrasenaForm)
# Añadir al final
@login_required
def editar_contrasena(request):
    if request.method == 'POST':
        form = EditarContrasenaForm(request.POST)
        if form.is_valid():
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
        return HttpResponseRedirect('/inicio')
    else:
        form = EditarContrasenaForm()
    return render_to_response('editar_contrasena.html', {'form': form}, context_instance=RequestContext(request))

def sobre(request):
    html = "<html><body>Registro de incidencias</body></html>"
    return HttpResponse(html)

def inicio(request):
    incidencias = Incidencia.objects.all().order_by('-id')
    return render_to_response('inicio.html',{'incidencias':incidencias}, context_instance=RequestContext(request))

def search(request):
    info = Incidencia.objects.count()
    code = Incidencia.objects.latest('id')
    query = request.GET.get('q', '')

    if query:
        incidencias = Incidencia.objects.filter(Q(fecharepo__icontains=query) | Q(descripcion__icontains=query) | Q(uuoorepo__icontains=query) | Q(Regrepo__icontains=query))
    else:
        incidencias = []
    return render_to_response("inicio.html", {"incidencias": incidencias,
        "query": query,
        "code": code,
        'info':info
    }, context_instance=RequestContext(request))

def reportes(request):
    incidencias = Incidencia.objects.all()
    #asignadas = int(Saldo1.objects.values('saldo_gal').last()["saldo_gal"]) - dscto1r
    info = Incidencia.objects.count()
    asig1 = Incidencia.objects.filter(flg_solucion='1').count()
    cie = Incidencia.objects.filter(flg_cierre='1').count()
    return render_to_response('reportes.html',{'incidencias':incidencias,'info':info,'asig1':asig1,'cie':cie}, context_instance=RequestContext(request))

def reportes1(request):
    incidencias = Incidencia.objects.all()
    #asignadas = int(Saldo1.objects.values('saldo_gal').last()["saldo_gal"]) - dscto1r
    info = Incidencia.objects.count()
    asig1 = Solucion.objects.count()
    cie = Cierre.objects.count()
    return render_to_response('reportes1.html',{'incidencias':incidencias,'info':info,'asig1':asig1,'cie':cie}, context_instance=RequestContext(request))

def reportes2(request):
    info1 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='6N0200').count()
    info1s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='6N0200').count()
    info2 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='6N0300').count()
    info2s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='6N0300').count()
    info3 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='6N0600').count()
    info3s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='6N0600').count()
    info4 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='6N0400').count()
    info4s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='6N0400').count()
    info5 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='6N0500').count()
    info5s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='6N0500').count()
    info6 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='6N0000').count()
    info6s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='6N0000').count()
    info7 = Incidencia.objects.filter(flg_solucion='1',uuoorepo='801000').count()
    info7s = Incidencia.objects.filter(flg_cierre='1',uuoorepo='801000').count()
    return render_to_response('reportes2.html',{'info1':info1,'info1s':info1s,'info2':info2,'info2s':info2s,'info3':info3,'info3s':info3s,'info4':info4,'info4s':info4s,'info5':info5,'info5s':info5s,'info6':info6,'info6s':info6s,'info7':info7,'info7s':info7s}, context_instance=RequestContext(request))

def reportes3(request):
    info1 = Solucion.objects.filter(reguosa='ro28',uuoosol='6N0200').count()
    info1s = Solucion.objects.filter(reguosa='1810',uuoosol='6N0200').count()
    info2 = Solucion.objects.filter(reguosa='ro28',uuoosol='6N0300').count()
    info2s = Solucion.objects.filter(reguosa='1810',uuoosol='6N0300').count()
    info3 = Solucion.objects.filter(reguosa='ro28',uuoosol='6N0600').count()
    info3s = Solucion.objects.filter(reguosa='1810',uuoosol='6N0600').count()
    info4 = Solucion.objects.filter(reguosa='ro28',uuoosol='6N0400').count()
    info4s = Solucion.objects.filter(reguosa='1810',uuoosol='6N0400').count()
    info5 = Solucion.objects.filter(reguosa='ro28',uuoosol='6N0500').count()
    info5s = Solucion.objects.filter(reguosa='1810',uuoosol='6N0500').count()
    info6 = Solucion.objects.filter(reguosa='ro28',uuoosol='6N0000').count()
    info6s = Solucion.objects.filter(reguosa='1810',uuoosol='6N0000').count()
    info7 = Solucion.objects.filter(reguosa='ro28',uuoosol='801000').count()
    info7s = Solucion.objects.filter(reguosa='1810',uuoosol='801000').count()
    return render_to_response('reportes3.html',{'info1':info1,'info1s':info1s,'info2':info2,'info2s':info2s,'info3':info3,'info3s':info3s,'info4':info4,'info4s':info4s,'info5':info5,'info5s':info5s,'info6':info6,'info6s':info6s,'info7':info7,'info7s':info7s}, context_instance=RequestContext(request))

def usuarios(request):
    usuarios = User.objects.all()
    incidencias = Incidencia.objects.all()
    return render_to_response('usuarios.html',{'usuarios':usuarios,'incidencias':incidencias}, context_instance=RequestContext(request))

def lista_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render_to_response('incidencias.html',{'datos':incidencias}, context_instance=RequestContext(request))

def lista_incidencias_asignaciones(request):
    incidencias = Incidencia.objects.filter(flg_solucion=0)
    Incidencia.objects.filter(pk=1).update(flg_solucion=0)
    return render_to_response('incidencias.html',{'datos':incidencias}, context_instance=RequestContext(request))

def lista_incidencias_cierre(request):
    incidencias = Incidencia.objects.filter(flg_cierre=0,flg_solucion=1)
    Incidencia.objects.filter(pk=1).update(flg_cierre=0)
    return render_to_response('incidenciasc.html',{'datos':incidencias}, context_instance=RequestContext(request))

def detalle_incidencia(request, id_incidencia):
    dato = get_object_or_404(Incidencia, pk=id_incidencia)
    solucion = Solucion.objects.filter(incidencia=dato)
    return render_to_response('incidencia.html',{'incidencia':dato,'solucion':solucion}, context_instance=RequestContext(request))


def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde Registro Incidencias'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ver_solucion(request, id):
    inci = Incidencia.objects.get(pk=id)
    return render_to_response('solucionform.html',{'inci':inci}, context_instance=RequestContext(request))

def ver_cierre(request, id):
    inci = Incidencia.objects.get(pk=id)
    return render_to_response('cierreform.html',{'inci':inci}, context_instance=RequestContext(request))

def nueva_incidencia(request):
    if request.method=='POST':
        formulario = IncidenciaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/inicio')
    else:
        formulario = IncidenciaForm()
    return render_to_response('incidenciaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_cierre(request, id):
    inci = Incidencia.objects.get(pk=id)
    if request.method=='POST':
        formulario = CierreForm(request.POST, request.FILES)
        Cierre(
            solucion = inci,
            imagenfin = request.FILES["imagenfin"],
            comentario = request.POST["comentario"],
        ).save()
        inci.flg_cierre = request.POST["flg_cierre"]
        inci.save()
        return HttpResponseRedirect('/cierrei')
    else:
        formulario = CierreForm()
    return render_to_response('cierreform.html',{'formulario':formulario, 'inci':inci}, context_instance=RequestContext(request))

def nuevo_solucion(request, id):
    inci = Incidencia.objects.get(pk=id)
    if request.method=='POST':
        formulario = SolucionForm(request.POST)
        Solucion(
            incidencia = inci,
            uuoosol = request.POST["uuoosol"],
            fechaeje = request.POST["fechaeje"],
            uuooati = request.POST["uuooati"],
            reguosa = request.POST["reguosa"],
            tipo_ate = request.POST["tipo_ate"],
            regsup = request.POST["regsup"]
        ).save()
        inci.flg_solucion = request.POST["flg_solucion"]
        inci.save()
        return HttpResponseRedirect('/asignaciones')
    else:
        formulario = SolucionForm()
    return render_to_response('solucionform.html',{'formulario':formulario, 'inci':inci}, context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/consultas')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/incidencia/nueva')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    incidencias = Incidencia.objects.all()
    return render_to_response('inicio.html', {'usuario':usuario,'incidencias':incidencias}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

