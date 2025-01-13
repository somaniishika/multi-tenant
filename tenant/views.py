from django.shortcuts import render

# Create your views here.
class First():
    def get(self, request):
        data = name.objects.all()
        serializer = FirstSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)