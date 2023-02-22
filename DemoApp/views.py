from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, "DemoApp/index.html") # with NULL domain HOME method will call and render the index.html default