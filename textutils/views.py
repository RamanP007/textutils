# # I have created this file
from django.http import HttpResponse
from django.shortcuts import render



# def index(request):
#     return HttpResponse("Hello")
# def about(request):
#     return HttpResponse("About Raman")

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")

def analyze(request):
    # Get the text
    djtext = (request.POST.get('text', 'default'))


    # Check box value
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    Charcounter = (request.POST.get('Charcounter', 'off'))

    # Check box which is on
    if removepunc == "on":
        analyzed = djtext
        punctuation = '''!@#$%^&*()_'+:;{}|[:]"\?><,./'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose' : 'Remove Punctuation', 'analyzed_text' : analyzed}
        djtext = analyzed
        # analyse the text
        # return render(request, 'analyze.html', params)
    if(fullcaps =="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (Charcounter == 'on'):
        analyzed = f"{djtext}\nTotal Character is " + str(len(djtext))
        params = {'purpose': 'Character counter', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != 'on'and Charcounter == 'on'):
        return HttpResponse("Please select any operation")




# def capitalizefirst(request):
#     return HttpResponse("Capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("New Line Remove")
#
# def spaceremove(request):
#     return HttpResponse("Space Remove")
#
# def charcount(request):
#     return HttpResponse("Char count")

def contact(request):
    return render(request, "Contactus.html")

def about(request):
    return render(request, "About.html")