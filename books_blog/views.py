from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def post_book(request):
    post = models.PostBook.objects.all()
    return render(request, 'post_book.html', {'post_object': post})


def detail_book(request, id):
    post = get_object_or_404(models.PostBook, id=id)
    return render(request, 'detail_book.html', {'post_id': post})


def add_post(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            HttpResponse('Good!')

    else:
        form = forms.ShowForm

    return render(request, 'add_book.html', {'form': form})
