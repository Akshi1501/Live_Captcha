from django.contrib import admin
from myapp.models import *
# Register your models here.

  
class adminproduct(admin.ModelAdmin):
    list_display=['name','price','categories']

class admincatagory(admin.ModelAdmin):
    list_display=['name','id']
    
class adminrecipie(admin.ModelAdmin):
    list_display=['name']

class adminorder(admin.ModelAdmin):
    list_display=['orderid','customer','date','price']

class admincon(admin.ModelAdmin):
    list_display=['name','email','desc']

class adminfback(admin.ModelAdmin):
    list_display=['des','score']

class admintotalorder(admin.ModelAdmin):
    list_display=['orderid','name','address','phone','date','totalamount']

class adminprofile(admin.ModelAdmin):
    list_display=['username','email','address','phone']

class admincaptcha(admin.ModelAdmin):
    list_display=['name','image']



admin.site.site_header="admin site"

admin.site.register(con,admincon)
admin.site.register(fback,adminfback)
admin.site.register(product,adminproduct)
admin.site.register(catagory,admincatagory)
admin.site.register(Order,adminorder)
admin.site.register(recipie,adminrecipie)
admin.site.register(totalorder,admintotalorder) 
admin.site.register(sup,adminprofile)
admin.site.register(captcha,admincaptcha)