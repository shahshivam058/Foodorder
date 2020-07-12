from django.shortcuts import render,redirect
from .forms import ItemFrom
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

# def index(request):
#     item_list = Item.objects.all()
#     # template = loader.get_template("Food/index.html")
#     context = {
#         "item_list" :item_list
#     }
#     return render(request,"Food/index.html",context)
#     # return HttpResponse(template.render(context,request))

class IndexClassView(ListView):
    model = Item
    template_name = "Food/index.html"
    context_object_name = "item_list"

def item(request):
    return HttpResponse("<h1>this is an item view</h1>")

# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         "item" : item
#     }
#     return render(request,"Food/details.html",context)

class DetailClassView(DetailView):
    model = Item
    template_name = "Food/details.html"



# def create_item(request):
#     form = ItemFrom(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("Food:index")
#     return render(request,"Food/item_form.html",{"form" : form})

class CreateItem(CreateView):
    model = Item
    fields = ["item_name","item_desc","item_price","item_image"]
    template_name = "Food/item_form.html"

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemFrom(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect("Food:index")
    return render(request,"Food/item_form.html",{"form" : form,"item" : item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("Food:index")
    return render(request,"Food/item_delete.html",{ "item" : item })
    