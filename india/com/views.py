from django.shortcuts import render

# Create your views here.
from.models import Contact

def index (request):
    return render(request,'com/index.html')


def Aboutus (request):
    return render(request,'com/aboutus.html')

def Enquiry (request):
    return render(request,'com/enquiry.html')



def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'com/contactus.html', {'thank': thank})



def Bookyourtour (request):
    return render(request,'com/bookyourtour.html')



def Factorytour (request):
    return render(request,'com/factorytour.html')




def Faq (request):
    return render(request,'com/faq.html')

def Bag (request):
    return render(request,'com/bag.html')


def BOX (request):
    return render(request,'com/box.html')


def Cards (request):
    return render(request,'com/cards.html')



def Christmas (request):
    return render(request,'com/christmas.html')



def Festival (request):
    return render(request,'com/festivals.html')





def Giftitem (request):
    return render(request,'com/giftitem.html')



def Journal (request):
    return render(request,'com/journal.html')




def Papers (request):
    return render(request,'com/papers.html')



def Seedpapers (request):
    return render(request,'com/seedpapers.html')




def Star (request):
    return render(request,'com/star.html')

def Stationary (request):
    return render(request,'com/stationary.html')








