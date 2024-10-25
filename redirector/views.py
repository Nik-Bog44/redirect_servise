from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from .serializers import EmailSerializer


class HomeView(APIView):
    def get(self, request):
        return Response("Добро пожаловать на главную страницу!")


class CreateEmailRedirectView(APIView):
    def post(self, request, *args, **kwargs) -> Response:
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        redirect_url = f"http://localhost:8000?goto_url={serializer.data['goto_url']}"
        return Response({"redirect_url": redirect_url}, status=status.HTTP_201_CREATED)


class RedirectToUrlView(APIView):
    def get(self, request, *args, **kwargs):
        goto_url = request.GET.get('goto_url')
        if goto_url:
            return HttpResponseRedirect(goto_url)
        else:
            return HttpResponseBadRequest("url is not valid")
