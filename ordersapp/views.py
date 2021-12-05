from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cartapp.cart import Cart



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/payment.html',
                          {'order': order.id})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})

def payment(request, order):
    order_element = Order.objects.get(id=order)
    order_element.paid = True
    order_element.save()
    return render(request, 'orders/order/created.html', {'orderid': order})
