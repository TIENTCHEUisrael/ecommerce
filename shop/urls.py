"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from shop import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ecommerce.views import index, productdetail, add_to_cart, cart, delete_cart
from accounts.views import signup, logout_user, login_user, biblio
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
                  path('', index, name='index'),
                  path('admin/', admin.site.urls),
                  path('signup/', signup, name="signup"),
                  path('login/', login_user, name="login"),
                  path('biblio/', biblio, name="biblio"),
                  path('chat/', include('Chat.urls')),
                  path('cart/', cart, name="cart"),
                  path('cart/delete/', delete_cart, name="delete_cart"),
                  path('logout/', logout_user, name="logout"),
                  path('product/<str:slug>/', productdetail, name="product"),
                  path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
