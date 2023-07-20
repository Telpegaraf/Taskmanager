from django.contrib import admin
from  .models import Task
# Register your models here.


def site():
    return None


admin.site.register(Task)