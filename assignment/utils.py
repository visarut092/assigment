from .models import *
from test_project.settings import set_db

def CollectData():
    collect_data = []
    get_product_id = []
    get_product = Product.objects.using(set_db).all()

    for product in get_product:
        get_product_id.append(product.product_id)

    for product_id in get_product_id:
        product_total_price = 0
        sales_product_total = 0
        product_detail = get_product.get(product_id = product_id)
        get_sales = Sales.objects.using(set_db).filter(product_id = product_id)
        for sales in get_sales:
            product_total_price += (sales.quantity * sales.price)
            sales_product_total += sales.quantity

        data = {
            'product_id' : product_detail.product_id,
            'product_name' : product_detail.product_name,
            'product_total_sales' : sales_product_total,
            'product_total_price' : product_total_price
        }
        collect_data.append(data)
    return collect_data