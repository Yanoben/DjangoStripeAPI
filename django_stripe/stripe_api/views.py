import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
from django.shortcuts import render, get_object_or_404


def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def index(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'home.html', {'item': item})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def buy(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url +
                'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=[
                    'card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                    },
                    'quantity': 1,
                }],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
