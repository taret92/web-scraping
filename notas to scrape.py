resultado = requests.get(url_base.format(1))

sopa= bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')

rating = libros[0].select('.star-rating.Four')
titulo = libros[1].select('a')[1]['title']


print(libros)

