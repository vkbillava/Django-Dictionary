from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from bs4 import BeautifulSoup
import requests

# Create your views here.

def home(request):
    if request.method == "POST":
        word = request.POST['word']
        url1 = 'https://www.dictionary.com/browse/'+word
        url2 = "https://www.vocabulary.com/dictionary/" + word + ""
        r1 = requests.get(url1)
        r2 = requests.get(url2)
        data = r1.content
        a_data = r2.content
        soup = BeautifulSoup(data, 'html.parser')
        a_soup = BeautifulSoup(a_data, 'html.parser')
        span = soup.find_all('span', {"class": "one-click-content"})
        soup_a = a_soup.find(class_="instances")

        txt = soup_a.get_text()
        txt1 = txt.rstrip()

        additional = ' '.join(txt1.split())

        param = {'label1': "Meaning of", 'label2': "Additional Info of",
                 'text': span[0].text, 'addon': additional, 'word': word}
        return render(request, 'index.html', param)
    else:
        return render(request, 'index.html')


