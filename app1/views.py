from django.shortcuts import render
from django.http import HttpResponse
import pymysql
# Create your views here.


def index(request):
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'test',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    cursor.close()
    conn.close()
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    if request.method == 'GET':
        return HttpResponse("You're looking at question %s." % question_id)
    elif request.method == 'POST':
        return HttpResponse("This is detail's POST method")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)