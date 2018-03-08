from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from .models import Kafedra, Student,Prepod


def index(request):
    num_kafedras = Kafedra.objects.count()

    num_students = Student.objects.all().count()

    num_prepods = Prepod.objects.count()

    return render(
        request,
        'index.html',

        context={' num_students':  num_students, ' num_kafedras':  num_kafedras,
                 ' num_prepods':  num_prepods},
    )


from django.views import generic


class KafedratListView(generic.ListView):
    model = Kafedra
    paginate_by = 2


class KafedraDetailView(generic.DetailView):
    model = Kafedra


class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2


class StudentDetailView(generic.DetailView):
    model = Student


class PrepodListView(generic.ListView):
    model = Prepod
    paginate_by = 2


class PrepodDetailView(generic.DetailView):
    model = Prepod
