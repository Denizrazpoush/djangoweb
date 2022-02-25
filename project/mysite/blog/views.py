from re import template
from telnetlib import STATUS
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Post
# from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from django.views.generic import ListView




# Create your views here.

def index(request):
    return HttpResponse("به بلاگ من خوش امدید ")

# def postlist(request):
#     posts=Post.published.all()
#     paginator=Paginator(posts,2)
#     page_number=request.GET.get('page')

#     try:
#         posts=paginator.get_page(page_number)

#     except PageNotAnInteger:
#         posts=paginator.get_page(1)
#     except EmptyPage:
#         posts=paginator.get_page(paginator.num_pages)
#SHekl functional hastesh ! vali class based b nazaram khyli bhtre ! berim ke dashte bashim !
    #be tore default dakhele template HAST. BARAYE HAMIN BE IN shekl address midahim 
    # return render(request,'blog/post/list.html',{'posts':posts,'posts':posts})


class PostListView(ListView):
    queryset= Post.published.all()
    context_object_name ='posts'
    paginate_by= 2
    template_name = 'blog/post/list.html'

    #deqat beshe ke dar class based view ha url motefavet hast !


def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,status='published',publish__year=year,publish__month=month,publish__day=day,slug=post)
    return render(request,'blog/post/detail.html',{'post':post})

    #URL ekhtesasi detail view : baraye in kar az get_absolute_url estefade mikonim (dar model ) 
    #va az reverse estefade mikonim , ebdeda name app va url view morede nazar ra be An shekl midahim 
    #sepas yel args drust mikonim ke mohtavaye an baray qesmate url app miravad . 
    # dar anja yek moteqayer ra barabare meqdare morede nazar qarar midahim .
    #be in shekl har post url ekhtesasi khodash a migirad 
    #baraye namayesh an ham dar view taiin mikonim ba get object or 404 ke az model Post 
    #che post haii entekhab shavad ke migoiim an haii ke slug barabre post va id barabare pk bashad .
    

