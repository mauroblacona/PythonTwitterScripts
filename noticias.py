from data import api
import feedparser


#d = feedparser.parse('https://tn.com.ar/rss.xml')
#d['entries'][0]
#titulo = d['entries'][0]['title']
#cuerpo = d['entries'][0]['summary']
#api.PostUpdate("Noticia automatica: {}\n{}".format(titulo, cuerpo[:-2]))

retry = True

while retry:
    d = feedparser.parse('https://tn.com.ar/rss.xml')
    if d['entries']:
        retry = False
        titulo = d['entries'][0]['title']
        cuerpo = d['entries'][0]['summary']
        api.PostUpdate("Noticia automatica: {}\n{}".format(titulo, cuerpo[:-2]))
    else:
        retry = True
        