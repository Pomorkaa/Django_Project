from django.contrib import admin

# Register your models here.
from .models import question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ("question_quest", "question_topic",)

admin.site.register(question, QuestionAdmin)