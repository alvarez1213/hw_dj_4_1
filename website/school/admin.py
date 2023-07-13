from django.contrib import admin

from .models import Student, Teacher, StudentTeachers

class StudentTeachersInLine(admin.TabularInline):
    model = StudentTeachers
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group',]
    list_filter = ['group',]
    inlines = [StudentTeachersInLine,]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['subject']


# @admin.register(StudentTeachers)
# class StudentTeachersAdmin(admin.ModelAdmin):
#     pass

