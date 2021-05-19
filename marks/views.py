from django.shortcuts import render,redirect
from django.views import View
from .forms import marksenteringform
from .models import Marks
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class home(View):
    def get(self,request):
        form = marksenteringform()
        return render(request,'base.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form =marksenteringform(request.POST, request.FILES)
        if form.is_valid():
            old=form.save(commit=False)
            if old.MarksInPhysics<=100 and old.MarksInChemistry<=100 and old.MarksInMathematics<=100:
                old.Total = old.MarksInPhysics+old.MarksInChemistry+old.MarksInMathematics
                old.Percentage = (old.Total/300)*100
                old.save()
                messages.success(request,'Congratulation! Marks Updated Successfully')
            else:
                messages.error(request, 'Enter Correct Marks')

        form1 = marksenteringform()
        return render(request,'base.html',{'form':form1,'active':'btn-primary'})

class leaderboard(View):
    def get(self,request):
        students = reversed(Marks.objects.all().order_by('Percentage'))
        return render(request,'leader.html',{'data':students,'active':'btn-primary'})
    
    def post(self,request):
        Roll=request.POST['search']
        datas = Marks.objects.filter(Roll_no=Roll)
        students = reversed(Marks.objects.all().order_by('Percentage'))
        if not datas.exists():
            messages.error(request,'Enter Correct RollNo')
            return render(request,'leader.html',{'data':students,'active':'btn-primary'})
        return render(request,'leader.html',{'data':datas,'active':'btn-primary'})

def asc(request):
    students = (Marks.objects.all().order_by('Percentage'))
    return render(request,'leader.html',{'data':students,'active':'btn-primary'})