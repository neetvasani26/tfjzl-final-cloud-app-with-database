from django.contrib import admin
from .model import Question, Choice, Submission, Lesson, Course, Instructor, Learner


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('id', 'question_text')
    search_fields = ('question_text',)


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('id', 'lesson_name')
    search_fields = ('lesson_name',)


# ✅ REQUIRED CourseAdmin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name')
    search_fields = ('course_name',)


# Registering models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)   # ✅ fixed
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)