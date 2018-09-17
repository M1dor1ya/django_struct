from django.contrib import admin

# Register your models here.
# 如果model需要在admin后台被管理，需要在此处添加以下内容：
from django.contrib import admin

from .models import Question

admin.site.register(Question)