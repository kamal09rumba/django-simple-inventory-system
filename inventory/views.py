from django.shortcuts import render
from django.http import Http404

# from django.http import HttpResponse

from inventory.models import Item
    #importing item class from inventory models

def index(request):
    items = Item.objects.exclude(amount=0)
    # return HttpResponse('<h1>Index views</h1>')
    return render(request, 'inventory/index.html',{
        'items':items,
    })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404("item does not exist")
    return render(request,'inventory/item_detail.html',{
        'item':item,
    })#first parameter reuqest, second parameter template and third parameter is dictionary value

    # return HttpResponse('<p>in item_detail view with id {0}</p>'.format(id))

