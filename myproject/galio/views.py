from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'e-commerce/index.html')

def indexTwo(request):
    return render(request, 'e-commerce/index-2.html')

def indexThree(request):
    return render(request, 'e-commerce/index-3.html')

def indexFour(request):
    return render(request, 'e-commerce/index-4.html')

def aboutUs(request):
    return render(request, 'e-commerce/about-us.html')

def blogDetailsAudio(request):
    return render(request, 'e-commerce/blog-details-audio.html')

def blogDetailsImage(request):
    return render(request, 'e-commerce/blog-details-image.html')

def blogDetailsVideo(request):
    return render(request, 'e-commerce/blog-details-video.html')

def blogDetails(request):
    return render(request, 'e-commerce/blog-details.html')

def blogFull2Column(request):
    return render(request, 'e-commerce/blog-full-2-column.html')

def blogFull3Column(request):
    return render(request, 'e-commerce/blog-full-3-column.html')

def blogLeftSidebar2Col(request):
    return render(request, 'e-commerce/blog-left-sidebar-2-col.html')

def blogLeftSidebar(request):
    return render(request, 'e-commerce/blog-left-sidebar.html')

def blogRightSidebar(request):
    return render(request, 'e-commerce/blog-right-sidebar.html')

def cart(request):
    return render(request, 'e-commerce/cart.html')

def checkOut(request):
    return render(request, 'e-commerce/checkout.html')

def compare(request):
    return render(request, 'e-commerce/compare.html')

def contactUs(request):
    return render(request, 'e-commerce/contact-us.html')

def loginRegister(request):
    return render(request, 'e-commerce/login-register.html')

def myAccount(request):
    return render(request, 'e-commerce/my-account.html')

def productDetailsAffiliate(request):
    return render(request, 'e-commerce/product-details-affiliate.html')

def productDetailsBox(request):
    return render(request, 'e-commerce/product-details-box.html')

def productDetailsGroup(request):
    return render(request, 'e-commerce/product-details-group.html')

def productDetailsVariable(request):
    return render(request, 'e-commerce/product-details-variable.html')

def productDetails(request):
    return render(request, 'e-commerce/product-details.html')

def shopGridFull3Col(request):
    return render(request, 'e-commerce/shop-grid-full-3-col.html')

def shopGridFull4Col(request):
    return render(request, 'e-commerce/shop-grid-full-4-col.html')

def shopGridLeftSidebar3Col(request):
    return render(request, 'e-commerce/shop-grid-left-sidebar-3-col.html')

def shopGridLeftSidebar(request):
    return render(request, 'e-commerce/shop-grid-left-sidebar.html')

def shopGridRightSidebar3Col(request):
    return render(request, 'e-commerce/shop-grid-right-sidebar-3-col.html')

def shopGridRightSidebar(request):
    return render(request, 'e-commerce/shop-grid-right-sidebar.html')

def shopListFull(request):
    return render(request, 'e-commerce/shop-list-full.html')

def shopListLeftSidebar(request):
    return render(request, 'e-commerce/shop-list-left-sidebar.html')

def shopListRightSidebar(request):
    return render(request, 'e-commerce/shop-list-right-sidebar.html')

def singleProductGroup(request):
    return render(request, 'e-commerce/single-product-group.html')

def singleProductSale(request):
    return render(request, 'e-commerce/single-product-sale.html')

def singleProduct(request):
    return render(request, 'e-commerce/single-product.html')

def wishlist(request):
    return render(request, 'e-commerce/wishlist.html')




