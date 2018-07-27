from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {'fields': ['question_text']}),
        ("Date information", {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.AdminSite.site_header = "django tutorials"
