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


def update_book(request, id):
    book_object = get_object_or_404(models.PostBook, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated!')

    else:
        form = forms.ShowForm(instance=book_object)

    return render(request, 'update_book.html', {'form': form, 'object': book_object})


def delete_book(request, id):
    book_object = get_object_or_404(models.PostBook, id=id)
    book_object.delete()
    return HttpResponse('Deleted')
