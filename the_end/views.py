import datetime

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt


def time(request, text):
    ti = datetime.datetime.now()
    return render(request, text, locals(), )


def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    th = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'iop.html', {'off': offset, 'th': th})


def display_meta(request):
    values = list(request.META.items())
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
        return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('less than 20 characters.')
        else:
            from books.models import Book
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html', {'book': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


@csrf_exempt
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )  # 如果要发送，请先配置settings.py like EMAIL_HOST = 'smtp.sina.cn'                 #SMTP地址
            # EMAIL_HOST_USER = 'xxxxxxxxxxx@sina.cn'     #我自己的邮箱
            # EMAIL_USE_TLS = False                       #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false

            return render(request, 'contact_thanks.html', locals())
    return render(request, 'contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
