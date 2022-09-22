from django.http import JsonResponse
from .models import CartLine


def cart_detail(request):
    lines = CartLine.objects.all()
    return JsonResponse({"lines": [line.to_dict() for line in lines]})
