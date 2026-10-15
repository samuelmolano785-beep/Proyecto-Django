from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category

# Create your views here.
# MVC = Model View Controller --> Acciones (metodos)
# MVT = Model View Template --> Acciones (metodos)

layout = """

"""

def index(request):

    html =("""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>             
     """)
    
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"
    nombre = 'Fabian Benavides 2'
    lenguajes = ['Python', 'JavaScript', 'PHP', '#C']
  
    

    return render(request, 'index.html',{
       'title': 'Inicio 2',
       'mi_variable': 'Soy un dato que esta en la vista',
       'nombre': nombre,
       'lenguajes': lenguajes,
    })

def holaMundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')
    
    return render(request, 'pagina.html')

def contacto(request, nombre="", apellido=""):
    html="" 
        
    if nombre and apellido:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellido}</h3>"
    return HttpResponse(layout + f"<h2>Contacto</h2>"+html)  

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulo(request):

    try:
        articulo = Article.objects.get(title="Matrix", public=True)
        response = f"Articulo: <br/>{articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017" 
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} actualizado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all()

    articulos = Article.objects.filter(title__contains="articulo" )

    articulos = Article.objects.filter(
                                title = "Articulo", 
                                ).exclude(
                                    public=True
                                )
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=0")
    
    return render(request, 'articulos.html', {
        'articulos': articulos
    })


def borrar_articulo(request, id): 
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')