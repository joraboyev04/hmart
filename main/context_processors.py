from . models import Products,Banners,Salesproduct,Categories,Blogs


def products(request):
    products=Products.objects.all()
    return {'products': products}

def banners(request):
    banners=Banners.objects.all()
    return {'banners': banners}


def saleproduct(request):
    saleproduct=Salesproduct.objects.all()
    return {'saleproduct': saleproduct}

def blogs(request):
    blogs=Blogs.objects.all()
    return {'blogs': blogs}