"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from assignment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_detail/sales_product',views.GetDetailSalesProduct.as_view()),
    path('sales_little/by_id',views.SalesLittle.as_view()),
    path('sales_lot/by_id',views.SalesLot.as_view()),
    path('sales_zero/by_id',views.SalesZero.as_view()),
]
