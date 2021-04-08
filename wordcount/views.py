from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordsdict = {}

    for word in wordlist:
        if word in wordsdict:
            wordsdict[word] += 1
        else:
            wordsdict[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext,'wordsdict':wordsdict.items(), 'wordcount':len(wordlist)})
