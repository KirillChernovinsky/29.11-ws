from django.http import HttpResponse

def index(request, name="Noname",age=0):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    user_ip = request.META['REMOTE_ADDR']
    path = request.path

    return HttpResponse(f'host {host} <br> browser {user_agent} <br> Path: {path} <br>'
                        f'user: {name}, age: {age}, IP: {user_ip}',
                        headers={'SecretCode': '1234456'})
def error(request):
    return HttpResponse(f"К сожалению произошла ошибка", status=400, reason="Incorrect data")

def login(request, login="Nologin", directory_name="Noname directory", directory_number=0):
    return HttpResponse(f"Ваш свой логин и имя папки с постами и номер поста: "
                        f"<br> Login: {login}, directory_name: {directory_name}, directory_number: {directory_number}")
# Create your views here.
