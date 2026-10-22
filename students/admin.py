from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'major', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'student_id', 'major')
    list_filter = ('major',)
    readonly_fields = ('created_at',)
    
