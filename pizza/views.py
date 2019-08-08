from django.shortcuts import render
from django.shortcuts import redirect
from .models import Pizzasize, Toppings
from .forms import OrderForm



# Create your views here.
def make_order(request):
    form = OrderForm()
    print('form', form)
    return render(request, 'menu.html', {'form':form})


def handle_order(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.cleaned_data['order']
        parsed_orders = parse_orders(order)
        receipt = generate_receipt(parsed_orders)
        print('Receipt', receipt)
        print('Parsed Order', parsed_orders)
    return render(request, 'menu.html', {'form':form, 'receipt':receipt})

def parse_orders(order):
    pizzas = []
    lines = order.split('\n')
    
    for line in lines:
        parts =line.split('-')
        size =parts[0].strip()
        pizza = {"size":size}
        toppings = parts[1].split(',')
        toppings = list(map(lambda s: s.strip(), toppings))
        pizza["toppings"] = toppings
        pizzas.append(pizza)
    return pizzas

def generate_receipt(order):
    subtotal = 0
    receipt = ''
    for pizza in order:
        price = 0
        order_string= ''
        size = Pizzasize.objects.get(size=pizza['size'])
        price += size.price
        order_string += '1 '+ size.size + ', '


        toppings = Toppings.objects.filter(name__in=pizza['toppings'])
        topping_len = str(len(toppings)) 
        order_string += topping_len + ' Topping Pizza - ' +  ' and '.join(pizza['toppings'])
        for topping in toppings:
            if size.size == 'Large':
                price += topping.large_price
            elif size.size == 'Medium':
                price += topping.medium_price
            elif size.size == 'Small':
                price += topping.small_price
        
        subtotal += price
        order_string += f': KES {price}'
        receipt += order_string + '\n'
    
    receipt += '\n\n'
    receipt += f'Subtotal: KES {subtotal}\n'
    tax = round(16*subtotal/100, 2)
    receipt += f'GTS: KES {tax}\n'
    total = subtotal + tax
    receipt += f'Total: KES {total}'

    return receipt