from django.shortcuts import render


finches = [
    {'id': 1, 'name': 'Zebra Finch', 'color': 'Gray', 'age': 2, 'description': 'A small bird with a distinctive black and white striped tail.'},
    {'id': 2, 'name': 'Gouldian Finch', 'color': 'Green', 'age': 1, 'description': 'Known for its bright colors and peaceful nature.'},
    {'id': 3, 'name': 'Society Finch', 'color': 'Brown', 'age': 3, 'description': 'A social bird often found in flocks.'},
    {'id': 4, 'name': 'Owl Finch', 'color': 'White and Black', 'age': 4, 'description': 'Named for its owl-like face and markings.'},
    {'id': 5, 'name': 'Star Finch', 'color': 'Yellow', 'age': 2, 'description': 'Recognized by the star-like spots on its chest.'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches':finches
    })

