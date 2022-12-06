from django.shortcuts import render
from .models import Product,TagLine,AboutUs,Image
from django.http import HttpResponseRedirect

# Create your views here.

product_1 = Product.objects.all()[0]
product_2 = Product.objects.all()[1]
product_3 = Product.objects.all()[2]
product_4 = Product.objects.all()[3]
product_5 = Product.objects.all()[4]
product_6 = Product.objects.all()[5]
product_7 = Product.objects.all()[6]
product_8 = Product.objects.all()[7]
tag_line1 = TagLine.objects.all()[0]
tag_line2 = TagLine.objects.all()[1]
about_us  = AboutUs.objects.all()[0]
images    = Image.objects.all()[0]

def index(request):
    if request.method == 'POST':
        entered_name = request.POST['name']
        entered_email = request.POST['email']
        entered_phone = request.POST['phone']
        entered_message = request.POST['message']
        print(entered_name, entered_email, entered_phone, entered_message)
        return render(request, 'hh/index.html',{
        'product1' :product_1,
        'product2' :product_2,
        'product3' :product_3,
        'product4' :product_4,
        'product5' :product_5,
        'product6' :product_6,
        'product7' :product_7,
        'product8' :product_8,
        'tagline1' :tag_line1,
        'tagline2' :tag_line2,
        'aboutus'  :about_us,
        'images'    :images,
        'formstatus':True
    })
   
    return render(request, 'hh/index.html',{
        'product1' :product_1,
        'product2' :product_2,
        'product3' :product_3,
        'product4' :product_4,
        'product5' :product_5,
        'product6' :product_6,
        'product7' :product_7,
        'product8' :product_8,
        'tagline1' :tag_line1,
        'tagline2' :tag_line2,
        'aboutus'  :about_us,
        'images'    :images,
        'formstatus':False
    })
