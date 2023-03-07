from django.shortcuts import render

# função que recebe uma request e renderiza um aquivo no caminho: 'recipes/pages/home.html'
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })
# função que recebe uma request e renderiza um aquivo no caminho: 'recipes/pages/home.html'
# o parametro id rece um valor inteiro e repassa como forma de separar as receiras após o caminho: 'dominio/recipes/id/'
def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })