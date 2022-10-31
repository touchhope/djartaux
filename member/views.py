import csv

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Member

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'IP Address'])

    #for member in Base.Member.objects.all().values_list('first_name', 'last_name', 'email', 'ip_address'):
    #for member in Base.Member.objects.get(id=1).values_list('first_name', 'last_name', 'email', 'ip_address'):
    #for member in Base.Member.objects.last().values_list('first_name', 'last_name', 'email', 'ip_address'):
    for member in Base.Member.objects.filter(last_name="dgjhdk").values_list('first_name', 'last_name', 'email', 'ip_address'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    return response