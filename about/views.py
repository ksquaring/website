from django.shortcuts import render
from .forms import CommentForm
from about.models import Comment



def aboutme(request):
    comments = Comment.objects.all().order_by('-created_on')
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],

            )
            comment.save()
    context = {
        "comments": comments,
        "form": form,
    }
    
    return render(request, 'aboutme.html', context)
    

# Create your views here.
