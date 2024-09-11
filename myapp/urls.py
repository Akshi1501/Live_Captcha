from django.contrib import admin
from django.urls import path,include
from myapp import views
from  django.views.generic import RedirectView

urlpatterns = [  
   path('signup',views.signup,name='signup'),
   path('',views.signin,name='signin'),
   path('signin',views.signin,name='signin'),  
   path('home', views.food, name='food'),
   path('admin/', admin.site.urls),
   path('contact', views.contact, name='contact'),
   path('about1',views.about1,name='about1'),
   path('profile',views.profile,name='profile'),
   path('feed',views.feed,name='feed'),
   path('order/',views.order,name='order'),
   path('cart/',views.cart,name='cart'),
   path('check',views.checkout,name='checkout'),
   path('detail/',views.detail,name='detail'),
   path('ourorder/',views.ourorder,name='ourorder'),
   path('myorder',views.myorder,name='myorder'),
   path('recepie',views.recepie,name='recepie'),
   path('recepieview',views.recepieview,name='recepieview'),
   path('orderplaced',views.orderplaced,name='orderplaced'),
   path('changepassword',views.changepassword,name='changepassword'),
   path('services',views.services,name='services'),
   path('signout',views.signout,name='signout'), 
   path('logout/',RedirectView.as_view(url='/admin/logout')),
   path('handlerequest/',views.handlerequest,name='handlerequest'), 
   path('handlerequest/home', views.food, name='food'),
   path('captcha',views.captcha,name='captcha'),
   path('verify/',views.verify,name='verify')

]