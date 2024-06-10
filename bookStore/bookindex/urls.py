from django.urls import path
from bookindex.views import (books_list, books_info, books_landing, index, show, delete,create, create_std_modelform, edit)

urlpatterns = [
    path('books_list', books_list, name='books_list'),
    path('books_info/<int:id>', books_info, name='books_info'),
    path('index', books_landing, name ='books_landing' ),
    path('index2', index, name ='books_index' ),
    path('<int:id>', show, name ='show' ),
    path('<int:id>/delete', delete, name ='delete' ),
    path('create', create, name='create'),
    path('create/form', create_std_modelform, name='create_std_modelform'),
    path('<int:id>/edit', edit, name ='edit' )
]

