from employee.models import *
from datetime import date

e1 = Employee(name='Timur Popov', birth_date='1983-05-16', position='Manager', salary=60000, work_experience=15)
e1.save()
e2 = Employee(name='Ivan Ivanov', birth_date='1990-05-28', position='Engineer', salary=40000, work_experience=5)
e2.save()
e3 = Employee(name='Habib Habibov', birth_date='1970-01-31', position='Security', salary=20, work_experience=30)
e3.save()
e4 = Employee(name='Maria Vladimirova', birth_date='1980-09-28', position='Director', salary=80000, work_experience=16)
e4.save()

p1 = Passport.objects.create(inn='11983196052020', id_card='4147565798789009', employee=e1)
p2 = Passport.objects.create(inn='11990196052020', id_card='4147565788789009', employee=e2)
p3 = Passport.objects.create(inn='11970196052020', id_card='4147565458789009', employee=e3)
p4 = Passport.objects.create(inn='21980096052020', id_card='4147564678789009', employee=e4)

e4.delete()

wp = WorkProject.objects.create(project_name='Special trading')

wp.employees.set([e1, e2, e3], through_defaults={'date_joined': date(2017, 8, 1)})
wp.employees.remove(e3)

wp.employees.create(name='Sergey Sergeev', birth_date='2000-08-20', position='Manager', salary=40000, work_experience=5,
                    through_defaults={'date_joined': date(2019, 5, 1)})

c1 = Client.objects.create(name='Bakai Bakaev', birth_date='2001-05-20', address='23 Red street', phone_number='123345')
c2 = Client.objects.create(name='Akai Akaev', birth_date='1960-05-20', address='29 Red street', phone_number='129345')
c3 = Client.objects.create(name='Elena Ikeeva', birth_date='1988-05-30', address='50 Red street', phone_number='145545')

vc = VipClient.objects.create(name='Richi Richev',
                              birth_date='1960-05-20', address='23 Blue street', phone_number='1230045',
                              vip_status_start='2020-05-20', donation_amount=700000
                              )
c1.delete()

Employee.objects.all()
Passport.objects.all()
WorkProject.objects.all()
WorkProject.objects.filter(employees__name__startswith='Timur')
Client.objects.all()
VipClient.objects.all()
