from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'name':'sibu','age':26,'hobbies':['cricket','football','f1']}
    return render (request,'condition.html',context=d)


def new(request):
    d={'football':['messi','neymar','r9'],'cricket':['yuvi','sachin','gambhir'],'f1':['alonso','nikki','michel']}
    return render (request,'new.html',{'new_d':d})
