from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cake': {
        'творог, г': 100,
        'сахар, ч.л.': 1,
        'сметана, ч.л': 0.5,
        'изюм, шт': 5
    },
    'draniki': {
        'картофель, г': 100,
        'яйцо, шт': 1,
        'мука, ст.л.': 3,
        'соль, ч.л.': 0.5
    }
}

def dish(request, recipe):
    if recipe in DATA.keys():
        servings = request.GET.get('servings', 1)
        ingridients = {}
        for ingridient in DATA[recipe]:
            ingridients[ingridient] = round(DATA[recipe][ingridient] * int(servings), 2)
        context = {
            'recipe': ingridients
        }
    else:
        context = {}
    return render(request, 'calculator/index.html', context)


def home_view(request):
    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, template_name='home/index.html', context=context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
