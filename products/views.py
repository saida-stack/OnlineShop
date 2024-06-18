from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Product
from .forms import ProductForm, CommentForm


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.order_by('-date_modified')


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def product_detail_view(request, pk):
    # get book object
    product = get_object_or_404(Product, pk=pk)
    # get book comments
    book_comments = product.comments.all()

    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.product = product
    #         new_comment.user = request.user
    #         new_comment.save()
    #         comment_form = CommentForm()
    # else:
    #     comment_form = CommentForm()
    #
    return render(request, 'products/product_detail.html',)
    #               {'product': product, 'comments': product_comments, 'comment_form': comment_form})


class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm


class ProductUpdateView(generic.UpdateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products_list')
