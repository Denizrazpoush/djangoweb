from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish','status','slug') #soton hai ke neshon mide
    list_filter = ('status','publish','created','author') # box e filternig on goshe 
    search_fields = ('title' , 'body') #baraye search
    prepopulated_fields = {'slug':('title',)} #baraye por kardan slug ba title
    raw_id_fields = ('author',) #on searche hast baraye user ha maslan 
    date_hierarchy = 'publish' # Time haro balae jadval neshon mide hatman reshte bashe touple nabashe
    ordering = ('status' , 'publish') #tartino ok mikone 
    list_editable = ('status',) # didane yesei dastana va avz krdnshon az haminja
    list_display_links=('slug',) #yejor halate link torish mikone dastano 
 
