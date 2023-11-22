from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Book

@method_decorator(csrf_exempt, name='dispatch')
class BookListCreateView(View):
    def get(self, request):
        books = Book.objects.all()
        data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_book = Book.objects.create(title=data['title'], author=data['author'])
        response_data = {'id': new_book.id, 'title': new_book.title, 'author': new_book.author}
        return JsonResponse(response_data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class BookRetrieveUpdateDeleteView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        data = {'id': book.id, 'title': book.title, 'author': book.author}
        return JsonResponse(data)

    def put(self, request, id):
        book = get_object_or_404(Book, id=id)
        data = json.loads(request.body)
        book.title = data['title']
        book.author = data['author']
        book.save()
        response_data = {'id': book.id, 'title': book.title, 'author': book.author}
        return JsonResponse(response_data)

    def delete(self, request, id):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return JsonResponse({'message': 'Livro excluído com sucesso'})
