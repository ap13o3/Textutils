#i have created this file - AP

from django.http import HttpResponse
from django.shortcuts import  render


def index(request):
    params= {'name':"AP",'place':'mds'}
    return render(request,'index.html',params)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html') # HttpResponse('''<h1> hello AP </h1> <a href="https://leetcode.com/tag/queue/"> queue leetcode </a>''')

def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')

    #check chcekbox values
    removepunc=request.GET.get('removepunc','off')
    fullcpas=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
    analyzed = ""
    purp=""
    #check which punc is on
    if(removepunc=="on"):
        purp+='Removed punctuations '
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        param = {'purpose': purp, 'analysed_text': analyzed}
        djtext=analyzed

    if(fullcpas=="on"):
        analyzed=""
        purp+='UPPERCASE '
        for char in djtext:
            analyzed+=char.upper()

        param = {'purpose': purp, 'analysed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        purp+='New Line Removed '
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed + char

        param = {'purpose': purp, 'analysed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        purp+= 'Extra Space Removed '
        for index,char in enumerate(djtext):
            if(not(djtext[index]==" " and  djtext[index+1]==" ")):
                analyzed+=char
        param = {'purpose': purp, 'analysed_text': analyzed}
        djtext = analyzed

    if(charcount=="on"):
        purp+= 'Character count'
        analyzed=0
        for char in djtext:
            if(char!=" "):
                analyzed+=1

        analyzed=str(analyzed)+"\n"
        analyzed+=djtext
        param = {'purpose': purp, 'analysed_text': analyzed}
    # else:
    #     return HttpResponse("No option is chosen")
    if(removepunc!="on" and fullcpas!="on" and newlineremover!="on" and extraspaceremover != "on" and charcount!="on"): return HttpResponse("Please select atleast one option")
    return render(request,'analyze.html',param)

def ex1(request):
    s='''
    <h2>Nevigation Bar</h2>
    <a href='https://www.facebook.com/'> Facebook </a> <br>
    <a href='https://www.instagram.com/?hl=en'>Insta</a> <br>
    <a href='https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12' >Youtube</a>
    '''
    return HttpResponse(s)
# def about(request):
#     return HttpResponse("hello AP in ABOUT <a href='/'>go to home </a>")
# def removepunc(request):
#     # get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     #analyse the text
#     return HttpResponse("remove punc")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newline remover")
# def spaceremove(request):
#     return HttpResponse('''space remover <a href="/"> back </a>''')
# def charcount(request):
#     return HttpResponse("char count")


