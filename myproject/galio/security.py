# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View
# from django.core.cache import cache


# def singleProduct(request):

#     return render(request, 'e-commerce/single-product.html')


# class SingleProductView(View):
#     template_name = 'e-commerce/single-product.html'
#     def get(self, request, *args, **kwargs):
#         product_id = kwargs["pk"]
#         if cache.get("product_id"):
#             product = cache.get("product_id")
#             print("Hit the Cache")
#         else:
#             try:
#                 product = Product.objects.get(pk=product_id)
#                 cache.set("product_id", product)
#                 print("Hit the DB!")
#             except product.DoesNotExist:
#                 return HttpResponse("Product not found")
#         context = {
#             product: product
#         }
#         return render(request, self.template_name, context)



