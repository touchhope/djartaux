import csv

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Member

from django.db import connection


from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    """Shows the main page"""

    return render(request,'base/index.html')
    

'''def query_to_dicts(query_string, *query_args):
    """Run a simple query and produce a generator
    that returns the results as a bunch of dictionaries
    with keys for the column values selected.
    """
    #log.debug(str(dir(connection)))
    cursor = connection.cursor()
    #log.debug(str(dir(cursor)))
    cursor.execute(query_string, query_args)
    #log.debug(cursor.rowcount)log
    col_names = [desc[0] for desc in cursor.description]
    #log.debug(str(col_names))
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        
        row_dict = (col_names, row)
        yield row_dict
    
    return

#def export(request):
    #todo_obj = query_to_dicts()

    #response = HttpResponse(mimetype='application/ms-excel')
    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename=elagu.csv'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Todo")

 
    row_num = 0

    columns = [
        (u"ID", 6000),
        (u"t_stamp", 8000),
    
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in todo_obj:
        row_num += 1
        row = [
            row_num,
            obj['todo_job'],
            obj['creation_date'].strftime("%A %d. %B %Y"),
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            wb.save(response)
    return response
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])

    #for member in Member.objects.filter(last_name="dgjhdk").values_list('first_name', 'last_name', 'email'):
    #for member in Member.objects.all().values_list('first_name', 'last_name', 'email'):
    for obj in todo_obj:
        row_num += 1
        row = [
            obj['first_name'],
            obj['last_name'],
            obj['email'],
            
        ]
        writer.writerow(row)

    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    return response


def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row
'''
'''
import sqlite3 as db
import csv

# Run your query, the result is stored as `data`
with db.connect('vehicles.db') as conn:
    cur = conn.cursor()
    sql = "SELECT make, style, color, plate FROM vehicle_vehicle"
    cur.execute(sql)
    data = cur.fetchall()

# Create the csv file
with open('vehicle.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['make', 'style', 'color', 'plate']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    for row in data:
        writer.writerow(row)
'''        
'''        
def my_custom_sql(self):
    with connection.cursor() as cursor:
        #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT first_name, last_name, email FROM base_member WHERE id = 0")
        row = cursor.fetchone()
        

    return row
'''
'''
    #for member in Member.objects.filter(last_name="dgjhdk").values_list('first_name', 'last_name', 'email'):
    #for member in Member.objects.all().values_list('first_name', 'last_name', 'email'):
    for member in Member.objects.get(id=0).rows():
        writer.writerow(member)
'''

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])
    
    writer.writerow(my_custom_sql(row))
    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    return response

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])
    
    with connection.cursor() as cursor:
        #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT first_name, last_name, email FROM base_member WHERE id = 1")
        row = cursor.fetchone()

    #return row

    #for member in Member.objects.filter(last_name="dgjhdk").values_list('first_name', 'last_name', 'email'):
    #for member in Member.objects.all().values_list('first_name', 'last_name', 'email'):
    #for row in cursor():
        writer.writerow(row)

    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    return response
