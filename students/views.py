import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm

# Helper to build list context with course filtering and pagination
def _render_student_list(request, queryset, query='', selected_course=''):
    courses = Student.objects.values_list('course', flat=True).distinct().order_by('course')
    if selected_course:
        queryset = queryset.filter(course__iexact=selected_course)
    
    total_students = queryset.count()
    paginator = Paginator(queryset, 5)  # 5 students per page (Bonus: Pagination)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/student_list.html', {
        'students': page_obj,
        'page_obj': page_obj,
        'total_students': total_students,
        'courses': courses,
        'selected_course': selected_course,
        'query': query,
    })

# 1. Read / View Student List
def student_list(request):
    selected_course = request.GET.get('course', '').strip()
    students_qs = Student.objects.all().order_by('-created_at')
    return _render_student_list(request, students_qs, selected_course=selected_course)

# 2. Create / Add Student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add Student'
    })

# 3. Update / Edit Student Details
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student record updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student'
    })

# 4. Delete Student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })

# 5. Search Students (by Student Name, Email Address, or Course)
def student_search(request):
    query = request.GET.get('q', '').strip()
    selected_course = request.GET.get('course', '').strip()
    students_qs = Student.objects.all().order_by('-created_at')
    if query:
        students_qs = students_qs.filter(
            Q(student_name__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )
    return _render_student_list(request, students_qs, query=query, selected_course=selected_course)

# Bonus Challenge: Export Student Records to CSV (Excel Compatible)
def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_records.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Student Name', 'Email Address', 'Phone Number', 'Course', 'Date of Birth', 'Address', 'Created At'])

    for s in Student.objects.all().order_by('-created_at'):
        writer.writerow([
            s.id,
            s.student_name,
            s.email,
            s.phone_number,
            s.course,
            s.date_of_birth,
            s.address,
            s.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        ])
    return response

# ==============================================================================
# SELF-REFLECTION QUESTIONS & ANSWERS
# ==============================================================================
# Conceptual Questions:
# 1. What is CRUD and why is it important?
#    CRUD stands for Create, Read, Update, and Delete. It represents the four 
#    fundamental operations required for persistent data storage in web apps.
# 2. What is a Django model?
#    A Python class that maps to a database table and defines data fields/behaviors.
# 3. What is the purpose of ModelForms?
#    Automatically converts Django model fields into HTML forms with built-in validation.
# 4. How does Django ORM simplify database interaction?
#    Lets developers query the database using Python code instead of raw SQL.
#
# Code Understanding Questions:
# 1. What is the purpose of migrations?
#    Propagates changes made to Django models into the database schema.
# 2. How does search functionality work using query filters?
#    Uses Q objects and __icontains for case-insensitive matching across multiple columns.
#
# Critical Thinking Questions:
# 1. How can this system be used in schools and training institutes?
#    To digitize admissions, manage enrollments, and search student records centrally.
# 2. How would you add user authentication and role-based access control?
#    Using django.contrib.auth, @login_required, and Django Groups/Permissions.
