from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView
from .models import Recipe, FullRecipe, Saved, FullRecipeSaved
#from .forms import LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RecipeEditForm
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)
 
# Create your views here.

#class RecipeEdit(UpdateView):
#    model = FullRecipeSaved
#    template_name = 'edit.html'
#    form_class = RecipeEditForm

@login_required
def RecipeEdit(request, pk): 
    source = Saved.objects.get(pk=pk)
    post = get_object_or_404(FullRecipeSaved, title=source.title)
    if request.method == "POST":
        form = RecipeEditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'recipesite/recipe.html', {'fullrecipe': post})
    else:
        form = RecipeEditForm(instance=post)
    return render(request, 'recipesite/edit.html', {'form': form})
       

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipesite/index.html', {'recipes': recipes})

def recipe(request,pk):
    #if request.method == 'POST' and 'idef' in request.POST:
        #iden = int(request.POST['idef'])
        main = Recipe.objects.get(pk=pk)

        fullrecipe = FullRecipe.objects.get(preview_image=main.title)
        return render(request,'recipesite/recipe.html', {'fullrecipe': fullrecipe})
    #return render(request,'recipesite/recipe.html')

@login_required
def recipe_showsaved(request,pk):
    #if request.method == 'POST' and 'idef' in request.POST:
        #iden = int(request.POST['idef'])
        main = Saved.objects.get(pk=pk)
        fullrecipe = FullRecipeSaved.objects.get(title=main.title)
        return render(request,'recipesite/saved_full.html', {'fullrecipe': fullrecipe})
    #return render(request,'recipesite/recipe.html')


#def recipe_edit(request):
    #return render(request, 'recipesite/main_favs.html')


def fav(request):
    user = request.user

    return render(request, 'recipesite/main_favs.html', {'user': user})

@login_required
def add_to_wishlist(request):
    
    if request.method == 'POST' and 'idef' in request.POST:
        identific = int(request.POST['idef'])
       
        obj = Recipe.objects.get(id = identific)
        
        #logging.warning(obj.title, obj.description, obj.link)
        saved_one = Saved()
        #кто 
        saved_one.owner = request.user.username
        saved_one.title = obj.title
        saved_one.photo = obj.photo
        #saved_one.link = obj.link
        saved_one.description = obj.description
        

        saved_one.save()
        #вот это добавила
        obj.save_check = True
        obj.save()


        

        full_to_save = FullRecipe.objects.get(title=saved_one.title)
        full_for_saved = FullRecipeSaved()
        full_for_saved.title = full_to_save.title
        full_for_saved.ingredient1 = full_to_save.ingredient1
        full_for_saved.ingredient2 = full_to_save.ingredient2
        full_for_saved.ingredient3 = full_to_save.ingredient3
        full_for_saved.ingredient4 = full_to_save.ingredient4
        full_for_saved.ingredient5 = full_to_save.ingredient5
        full_for_saved.ingredient6 = full_to_save.ingredient6
        full_for_saved.description1 = full_to_save.description1
        full_for_saved.description2 = full_to_save.description2
        full_for_saved.preview = full_to_save.preview
        full_for_saved.motivation = full_to_save.motivation
        full_for_saved.preview_image = full_to_save.preview_image
        full_for_saved.save()

    
    if request.method == 'POST' and 'id_del' in request.POST:
        
        id_delete = int(request.POST['id_del'])
        to_del = Saved.objects.get(id = id_delete)
        #удаление отметки
        upd_recipe = Recipe.objects.get(title = to_del.title)
        upd_recipe.save_check = False
        upd_recipe.save()
        to_del_full = FullRecipeSaved.objects.get(title=to_del.title)
        #logging.warning(to_del.title)
        to_del.delete()
        to_del_full.delete()
        

    all_saved = Saved.objects.all().filter(owner = request.user.username)
    #    Saved.objects.create(title=obj.title, description = obj.description, photo = obj.photo, link = obj.link)
    #return JsonResponse()
    #return HttpResponse("some words")
    return render(request, 'recipesite/main_favs.html', {'saved': all_saved})


    


