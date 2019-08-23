# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from celerytask.tasks import App01Task,multiply


# Create your views here.

class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.method.lower() == 'get':
            return response
        else:
            if request.user.is_superuser:
                return response
            else:
                return self.http_method_not_allowed

    def get(self, request):
        return render(request, 'app01/index.html', )

    def post(self, request):
        pass


def index(request):
    print('request accept')
    App01Task().delay()
    print('request finish')
    return JsonResponse({'result': 'ok'})


def multy(request):
    print('multiply accept')
    multiply.delay()
    print('multiply finish')
    return JsonResponse({'result': 'ok'})
