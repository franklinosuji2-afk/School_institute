from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# from .models import Student  # Import your Student model

def welcome(request):
    return render(request, 'students/welcome.html')

def student_list(request):
    # students = Student.objects.all()  # Get your students from database
    # paginator = Paginator(students, 10)  # Show 10 students per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    context = {
        # 'students': page_obj,
        'students': [],  # Empty for now - replace with your data
    }
    return render(request, 'students/student_list.html', context)

def student_details(request, student_id=None):
    # student = get_object_or_404(Student, id=student_id) if student_id else None
    context = {
        # 'student': student,
        'student': None,  # None for now - replace with your data
    }
    return render(request, 'students/details.html', context)

    

