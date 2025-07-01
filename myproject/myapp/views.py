from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


# Vue d'accueil : affiche les 5 derniers livres
def index(request):
    latest_books = Book.objects.order_by('-published_date')[:5]
    context = {'latest_books': latest_books}
    return render(request, 'myapp/index.html', context)


# Vue de détail (non encore utilisée pleinement)
def detail(request, book_id):
    return HttpResponse(f"Détail du livre n°{book_id}")



# Vue pour ajouter un livre via un formulaire ModelForm
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save() # Enregistre le livre dans la base
            return redirect('index') # Redirige vers la page d9accueil
        else:
            print(form.errors) # Affiche les erreurs dans le terminal
    else:
        form = BookForm() # Affiche un formulaire vide
    return render(request, 'myapp/add_book.html', {'form': form})