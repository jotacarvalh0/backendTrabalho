from django.contrib import admin
from django.urls import path, include
from myapp.views import BookListCreateView, BookRetrieveUpdateDeleteView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:id>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
]
