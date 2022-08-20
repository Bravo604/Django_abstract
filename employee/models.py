from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        year = 2022 - self.birth_date.year
        return year

    def __str__(self):
        return self.name


class Employee(AbstractPerson):
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    work_experience = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'Поля {self.name}, {self.birth_date}, {self.position}, {self.salary}, '
              f'{self.work_experience} были изменены ')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.position}'


class Passport(models.Model):
    inn = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_gender(self):
        gender = ''
        for i in self.inn:
            if i == 1:
                gender = 'Male'
            if i == 2:
                gender = 'Female'
        return gender

    def save(self, *args, **kwargs):
        print(f'Поля {self.inn}, {self.id_card} были изменены ')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee} - {self.id_card}'


class WorkProject(models.Model):
    project_name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee, through='Membership')

    def save(self, *args, **kwargs):
        print(f'Поля {self.project_name} были изменены ')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'Поля {self.date_joined} были изменены ')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee} joined {self.work_project} on {self.date_joined}'


class Client(AbstractPerson):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        print(f'Поля {self.name}, {self.birth_date}, {self.address}, {self.phone_number}, '
              f'были изменены ')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class VipClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'Поля {self.vip_status_start}, {self.donation_amount} были изменены ')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.vip_status_start}'



