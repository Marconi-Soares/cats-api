from random import randint

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CatModelSerializer
from .models import Cat 

# Create your views here.
def get_cat():
    cats_total = Cat.objects.count()
    cat_pk = randint(1, cats_total)
    return Cat.objects.get(pk=cat_pk)

@api_view(['GET'])
def cat_view(request):
    cat = get_cat()
    serializer = CatModelSerializer(cat)
    return Response(serializer.data)
