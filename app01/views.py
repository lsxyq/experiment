# Create your views here.

from django.shortcuts import render
from django.views import View

from app01.tasks import test_multiply


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
        return render(request, 'a.html', )

    def post(self, request):
        pass


def index(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    test_multiply.delay(int(x), int(y))  # 加上delay才是异步执行，不然就是同步，而且如果将其赋予一个值，也是同步了
    if request.method == 'POST':
        pass
    return render(request, 'index.html', {'x': 10})
