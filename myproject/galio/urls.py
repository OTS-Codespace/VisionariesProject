from django.urls import path
from . import views







urlpatterns = [
    path('', views.home, name='galiohome' ),
    path('indexTwo/', views.indexTwo, name='indexTwo'),
    path('indexThree/', views.indexThree, name='indexThree'),
    path('indexFour/', views.indexFour, name='indexFour'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('blogDetailsAudio/', views.blogDetailsAudio, name='blogDetailsAudio'),
    path('blogDetailsImage/', views.blogDetailsImage, name='blogDetailsImage'),  
    path('blogDetailsVideo/', views.blogDetailsVideo, name='blogDetailsVideo'),
    path('blogDetails/', views.blogDetails, name='blogDetails'),
    path('blogFull2Column/', views.blogFull2Column, name='blogFull2Column'),
    path('blogFull3Column/', views.blogFull3Column, name='blogFull3Column'),
    path('blogLeftSidebar2Col/', views.blogLeftSidebar2Col, name='blogLeftSidebar2Col'),
    path('blogLeftSidebar/', views.blogLeftSidebar, name='blogLeftSidebar'),
    path('blogRightSidebar/', views.blogRightSidebar, name='blogRightSidebar'),
    path('cart/', views.cart, name='cart'),
    path('checkOut/', views.checkOut, name='checkOut'),
    path('compare/', views.compare, name='compare'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('loginRegister/', views.loginRegister, name='loginRegister'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('productDetailsAffiliate/', views.productDetailsAffiliate, name='productDetailsAffiliate'),
    path('productDetailsBox/', views.productDetailsBox, name='productDetailsBox'),
    path('productDetailsGroup/', views.productDetailsGroup, name='productDetailsGroup'),
    path('productDetailsVariable/', views.productDetailsVariable, name='productDetailsVariable'),
    path('productDetails/', views.productDetails, name='productDetails'),
    path('shopGridFull3Col/', views.shopGridFull3Col, name='shopGridFull3Col'),
    path('shopGridFull4Col/', views.shopGridFull4Col, name='shopGridFull4Col'),
    path('shopGridLeftSidebar3Col/', views.shopGridLeftSidebar3Col, name='shopGridLeftSidebar3Col'),
    path('shopGridLeftSidebar/', views.shopGridLeftSidebar, name='shopGridLeftSidebar'),
    path('shopGridRightSidebar3Col/', views.shopGridRightSidebar3Col, name='shopGridRightSidebar3Col'),
    path('shopGridRightSidebar/', views.shopGridRightSidebar, name='shopGridRightSidebar'),
    path('shopListFull/', views.shopListFull, name='shopListFull'),
    path('shopListLeftSidebar/', views.shopListLeftSidebar, name='shopListLeftSidebar'),
    path('shopListRightSidebar/', views.shopListRightSidebar, name='shopListRightSidebar'),
    path('singleProductGroup/', views.singleProductGroup, name='singleProductGroup'),
    path('singleProductSale/', views.singleProductSale, name='singleProductSale'),
    path('singleProduct/', views.singleProduct, name='singleProduct'),
    path('wishlist/', views.wishlist, name='wishlist'),
    
    






]