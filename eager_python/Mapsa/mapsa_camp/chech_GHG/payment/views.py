
import os
import uuid

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from idpay.api import IDPayAPI
# from .models import Invoice
from cart.models import Cart,CartItem
from payment.models import Invoice
# Create your views here.


def payment_init():
    base_url = os.environ.get('BASE_URL')
    api_key = os.environ.get('IDPAY_API_KEY')
    sandbox = os.environ.get('IDPAY_SANDBOX')

    return IDPayAPI(api_key, base_url, bool(sandbox))


def payment_start(request):
    if request.method == 'POST':

        order_id = uuid.uuid1()
        amount = request.POST.get('amount')

        payer = {
            'name': request.user.username,
            'mail': request.user.email,
        }
        cart = Cart.objects.filter(user_id=request.user.id).first()
        items = cart.cart_fk.filter(status='pending', is_selected=True).values('id')
        item_id = [iid['id'] for iid in items]
        record = Invoice(user_id=request.user.id, order_id=order_id, amount=int(amount))
        record.save()
        record.save()
        record.m2m.add(*item_id)
        record.save()

        idpay_payment = payment_init()
        result = idpay_payment.payment(str(order_id), amount, 'payment-return/', payer)
        if 'id' in result:
            record.status = 1
            record.payment_id = result['id']
            record.save()

            return redirect(result['link'])

        else:
            txt = result['message']
    else:
        txt = "Bad Request"

    return render(request, '404.html', {'txt': txt})


@csrf_exempt
def payment_return(request):
    if request.method == 'POST':

        pid = request.POST.get('id')
        status = request.POST.get('status')
        pidtrack = request.POST.get('track_id')
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        card = request.POST.get('card_no')
        date = request.POST.get('date')

        if Invoice.objects.filter(order_id=order_id, payment_id=pid, amount=amount, status=1).count() == 1:

            idpay_payment = payment_init()

            payment = Invoice.objects.get(payment_id=pid, amount=amount)
            payment.status = status
            payment.date = str(date)
            payment.card_number = card
            payment.idpay_track_id = pidtrack
            payment.save()

            if str(status) == '10':
                result = idpay_payment.verify(pid, payment.order_id)

                if 'status' in result:
                    payment.status = result['status']
                    payment.bank_track_id = result['payment']['track_id']
                    payment.save()
                    if result['status'] == 100:
                        items = payment.m2m.all()
                        items.update(status="paid")
                        for item in items:
                            print(f'1 {item.product.inventory}')
                            item.product.inventory -= item.qty
                            print(f'2 {item.product.inventory}')
                            item.product.save()

                    return render(request, '404.html', {'txt': result['message']})

                else:
                    txt = result['message']

            else:
                txt = "Error Code : " + str(status) + "   |   " + "Description : " + idpay_payment.get_status(status)

        else:
            txt = "Order Not Found"

    else:
        txt = "Bad Request"

    return render(request, '404.html', {'txt': txt})


def payment_check(request):
    return None