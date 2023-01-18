from django.shortcuts import render

posts=[
    {
        'author':'Richard Mbuti',
        'title':'Blog tweet 1',
        'content':'My first django application tweet',
        'date_posted':'January 18,2022'
    },
    {
        
        'author':'Richard Mbuti',
        'title':'Blog tweet 2',
        'content':'My second django application tweet',
        'date_posted':'January 17,2022'
    
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})