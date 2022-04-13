from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.views import generic as views


from pythonMyProject.bikes.models import Bike, SellBike, Order


class HomeView(views.TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, views.ListView):
    model = SellBike
    template_name = 'store/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bikes = Bike.objects.all().order_by('-date_created')[:3]
        sell_bikes = SellBike.objects.all().order_by('-date_created')[:3]

        customer = self.request.user.id
        cust_order = Order.objects.filter(customer_id=customer)

        if len(cust_order) > 0:
            # if self.request.user.is_authenticated:

            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items
        else:

            cart_items = 0

        context.update({
            'bikes': bikes,
            'sell_bikes': sell_bikes,
            'cart_items': cart_items,
        })

        return context


class PostBikeView(LoginRequiredMixin, views.ListView):
    model = Bike
    template_name = 'bikes/posted_bikes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bikes = Bike.objects.all().order_by('-date_created')

        customer = self.request.user.id
        cust_order = Order.objects.filter(customer_id=customer)

        if len(cust_order) > 0:
            # if self.request.user.is_authenticated:

            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items
        else:

            cart_items = 0

        context.update({
            'bikes': bikes,
            'cart_items': cart_items,
        })

        return context


class BikesForSale(LoginRequiredMixin, views.ListView):
    model = SellBike
    template_name = 'bikes/bike_for_sale.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        sell_bikes = SellBike.objects.all().order_by('-date_created')

        cart_items = 0
        if self.request.user.is_authenticated:
            customer = self.request.user.id
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items

        context.update({
            'sell_bikes': sell_bikes,
            'cart_items': cart_items,
        })

        return context

