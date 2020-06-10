from django.http import HttpResponse
from django.template import Template
from django.template import loader


def pagina(request):

    cab=loader.get_template("base.html")

    cabe=cab.render()

    return HttpResponse(cabe)


def conocenos(request):

    con=loader.get_template("bodies/conocenos.html")

    cono=con.render()

    return HttpResponse(cono)

def home(request):

    hom=loader.get_template("bodies/home.html")

    home=hom.render()

    return HttpResponse(home)

def galeria(request):

    gal=loader.get_template("bodies/galeria.html")

    gale=gal.render()

    return HttpResponse(gale)

def contacto(request):

    cont=loader.get_template("bodies/contacto.html")

    contact=cont.render()

    return HttpResponse(contact)