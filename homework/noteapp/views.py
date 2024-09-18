from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from  .forms import RegistrationForm, AuthorForm, QuoteForm
from .models import Author, Quote

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'noteapp/register.html', {'form':form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'noteapp/add_author.html', {'form':form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.added_by = request.user
            quote.save
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'noteapp/add_quote.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'noteapp/author_list.html', {'authors': authors})

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'noteapp/quote_list.html', {'quotes': quotes})