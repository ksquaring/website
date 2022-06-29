from django.shortcuts import render
from .forms import CommentForm
def aboutme(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],

            )
            comment.save()
    
    return render(request, 'aboutme.html')
    

# Create your views here.
