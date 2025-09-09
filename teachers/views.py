from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Teacher

def welcome(request):
    total_teachers = Teacher.objects.count()
    context = {
        'total_teachers': total_teachers,
        'total_subjects': 45,
        'total_departments': 12,
    }
    return render(request, 'teachers/welcome.html', context)

def teachers_details(request, teacher_id=None):
    teacher = None
    if teacher_id:
        teacher = get_object_or_404(Teacher, id=teacher_id)
    context = {'teacher': teacher}
    return render(request, 'teachers/details.html', context)

def teacher_list(request):
    teachers = Teacher.objects.all()
    paginator = Paginator(teachers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'teachers': page_obj}
    return render(request, 'teachers/list.html', context)

