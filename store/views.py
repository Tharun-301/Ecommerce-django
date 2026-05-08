from django.shortcuts import render, get_object_or_404, redirect
from carts.views import _cart_id
from category.models import Category
from django.shortcuts import render

from orders.models import OrderProduct
from store.forms import ReviewForm
from .models import Product, ReviewRating

from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib import messages



# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,
        'reviews': reviews,

    }
    return render(request, 'store/product_detail.html', context)



def search(request):
    products = Product.objects.all()
    product_count = products.count()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword)
            )
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        review = ReviewRating.objects.filter(
            user_id=request.user.id,
            product_id=product_id
        ).first()

        form = ReviewForm(request.POST)

        if form.is_valid():
            if review:
                review.subject = form.cleaned_data['subject']
                review.rating = form.cleaned_data['rating']
                review.review = form.cleaned_data['review']
                review.ip = request.META.get('REMOTE_ADDR')
                review.save()
                messages.success(request, 'Thank you! Your review has been updated.')
            else:
                ReviewRating.objects.create(
                    subject=form.cleaned_data['subject'],
                    rating=form.cleaned_data['rating'],
                    review=form.cleaned_data['review'],
                    ip=request.META.get('REMOTE_ADDR'),
                    product_id=product_id,
                    user_id=request.user.id,
                )
                messages.success(request, 'Thank you! Your review has been submitted.')

    return redirect(url)