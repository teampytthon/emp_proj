from django.shortcuts import render

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import  Department



class IndexView(ListView):
    template_name = 'department/index.html'
    context_object_name = 'dep_list'

    def get_queryset(self):
        #return Department.objects.all()
        return Department.objects.raw('select * from department_department d,department_employee e where d.id=e.dep_id_id')



class saveData(CreateView):
    model = Department
    fields = ['dept_name']
    success_url = reverse_lazy('department:index')


class EditData(UpdateView):
    model = Department
    fields = ['dept_name']



class deleteData(DeleteView):
    model = Department
    success_url = reverse_lazy('department:index')
