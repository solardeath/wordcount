from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def count(request): 
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    count= 0
    for words in wordlist:
        for char in words:
            print(count)
            count+=1

    avgchars  = count/len(wordlist) 

    
    for words in wordlist:
        firstletter = words[0]
        print(firstletter)
        words+=1       

    return render(request, 'count.html',{'fulltext': fulltext, 'count':len(wordlist), 'avgchars':avgchars, 'firstletter': firstletter})   


def about(request):
    return render(request, 'about.html')