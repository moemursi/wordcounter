from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    count = len(word_list)

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] +=1 #increase the ount
        else:
            word_dictionary[word] = 1 #add to dictionary
    return render(request, 'count.html',{'fulltext':fulltext,'count':count,'word_dictionary':word_dictionary.items()})