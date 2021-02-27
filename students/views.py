from django.shortcuts import render
from rest_framework.views import APIView
from students.models import PropertyMasterApi
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


class SearchPhone(APIView):
    def get(self, request):
        if "phone" in request.GET:
            phone = request.GET.get("phone")
            print(phone)
            try:
                pma = PropertyMasterApi.objects.filter(phonenumber_0=phone).values()
                pma = pma[0]
                pma.update({
                    "status": True
                })
                # return Response(pma,status=200)
                return render(request, 'index.html', pma)
            except Exception as e:
                print(e)
                pma = {
                    "status": False
                }
                return render(request, 'index.html', pma)

        else:
            return Response({"detail": "Phone does not exists"}, status=404)

