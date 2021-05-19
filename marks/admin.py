from django.contrib import admin
from .models import Marks

@admin.register (Marks)
class Marks_admin(admin.ModelAdmin):
    list_display = ['id','Name','Roll_no','MarksInPhysics','MarksInMathematics','MarksInChemistry','Total','Percentage']