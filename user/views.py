from django.shortcuts import render, redirect
from .forms import userform
from . models import user_rec

def home(request):
    students = user_rec.objects.all().order_by('-id')
    context = {'students':students}

    return render (request, 'user/index.html',context)

def user_form(request):
    if request.method =='POST':
        form = userform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = userform()
    context = {'form':form}
    return render(request, 'user/user_form.html', context)


def update_rec(request, pk):
 if request.method == 'POST':
  pi = user_rec.objects.get(id=pk)
  fm = userform(request.POST,request.FILES, instance=pi)
  if fm.is_valid():
   fm.save()
   return redirect('home')
 else:
  pi = user_rec.objects.get(id=pk)
  fm = userform(instance=pi)
 return render(request, 'user/user_form.html', {'form':fm})

          
def delete(request, pk):
    user_rec.objects.get(id=pk).delete()
    return redirect('home')