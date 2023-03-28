import requests
import bs4


#crear url sin numero de pagina
url_base= 'http://books.toscrape.com/catalogue/page-{}.html'

#lista de titulos con 4 o 5 estrellas
titulos_rating_alto= []

#iterar paginas
for pagina in range(1, 51):

    #crear sopa en cada pagina
    urldepagina= url_base.format(pagina)
    resultado= requests.get(urldepagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar en los libros
    for libro in libros:

        #checar que tenga 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #guardar titulo en variable
            titulolibro = libro.select('a')[1]['title']

            #agregar libro a la lista
            titulos_rating_alto.append(titulolibro)

#ver libros de 4 y 5 estrellas
for t in titulos_rating_alto:
    print(t)
print (len(titulos_rating_alto))

