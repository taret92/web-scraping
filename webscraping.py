import requests
import bs4

url="https://www.escueladirecta.com/courses"

resultado = requests.get(url)
sopa= bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes= sopa.select('.course-box-image')[0]['src']

print(imagenes)

imagencurso1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagencurso1.content)
f.close()


#para web scraping de imagenes debo guardar el archivo en modo write binary con f=open('miarchivo','wb'),
#debo usar f.write('laimagendescargada'.content)
