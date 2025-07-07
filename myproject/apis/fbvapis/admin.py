from django.contrib import admin

from .models import Student

def mark_as_gpa_above_7(modeladmin, request, queryset):
    queryset.update(gpa=7.1)  # Set GPA to above 7.0

mark_as_gpa_above_7.short_description = "Mark selected students with GPA above 7.0"



class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'date_of_birth','gender','gpa')  #       Display these fields in the admin list view
    list_editable = ('gender', 'gpa')  # Allow these fields to be editable directly in the list view
    list_filter = ('first_name',)  # Add a filter sidebar for the first_name field
    search_fields = ('first_name', 'last_name', 'student_id', 'email')  # Enable search functionality for these fields
    ordering = ('gpa',)  # Default ordering by gpa field
    list_per_page = 2  # Number of records to display per page in the admin list view
    fields = ('first_name', 'last_name', 'student_id', 'email', 'date_of_birth',) # Fields to display in the admin form view
    exclude = ('date_of_birth',) # Fields to exclude from the admin form view
    '''fieldsets = (                    # Grouping fields into sections     
        ['Personal Information', {
            'fields': ('first_name', 'last_name', 'student_id', 'email', 'date_of_birth')

        }],


        ['Acadamic Details', {
            'fields': ('gpa',)

        }],
    )'''
       
     
    actions = [mark_as_gpa_above_7]  # Add custom action to the admin interface

admin.site.register(Student,StudentAdmin)