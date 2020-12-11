from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests


# Create your views here.
@csrf_exempt
def task_complete(request):
    jwt = getattr(settings, 'JWT')
    headers = {'Authorization': jwt}
    ctx = {}

    number_url = 'https://dev.sixthings.tech/api/tasks'
    number_response = requests.get(number_url, headers=headers)
    rescode = number_response.status_code

    complete = 0
    ctx['message'] = '무언가 잘못되었소. 앱을 확인해보시오.'

    if (rescode == 200):
        result = number_response.json()
        meta = result.get('meta')
        tasks = result.get('tasks')

        complete = meta['complete']
        inComplete = meta['inComplete']

    complete = str(complete)
    print('complete:', complete)
    print(meta)
    print(tasks)

    url = 'https://dev.sixthings.tech/api/tasks/' + complete + '?type=task'
    payload = {'completedAt': 1708614682229}
    response = requests.put(url, headers=headers, data=payload)
    rescode = response.status_code

    if (rescode == 200):
        result = response.json()
        msg = result.get('message')
        print('진입')

        if msg == 'ok':
            print('진입2')
            if inComplete > 1:
                complete = int(complete)
                next_task = tasks[complete + 1]
                ctx['next_title'] = next_task['title']
                message = '수고가 많소. 다음 할 일은 ' + ctx['next_title'] + '오.'
                ctx['message'] = message
            else:
                message = '오늘도 고생했소. 오늘의 일과를 모두 끝내셨소.'
                ctx['message'] = message

    respon = {
        "version": "2.0",
        "resultCode": "OK",
        "output": ctx
    }

    return JsonResponse(respon)


@csrf_exempt
def task_check(request):
    url = 'https://dev.sixthings.tech/api/tasks'
    jwt = getattr(settings, 'JWT')
    headers = {'Authorization': jwt}
    response = requests.get(url, headers=headers)
    rescode = response.status_code

    complete = 0
    current_title = '태스크 등록'

    if (rescode == 200):
        result = response.json()
        meta = result.get('meta')
        tasks = result.get('tasks')
        complete = meta['complete']
        inComplete = meta['inComplete']

        if inComplete > 0:
            current_task = tasks[complete]
            current_title = current_task['title']
            complete = complete + 1
        else:
            current_title = '오늘의 임무를 모두 완수하였소.'

    respon = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            'current_number': complete,
            'current_title': current_title,
            'rescode': rescode
        }
    }
    return JsonResponse(respon)


@csrf_exempt
def tasklist_check(request):
    url = 'https://dev.sixthings.tech/api/tasks'
    jwt = getattr(settings, 'JWT')
    headers = {'Authorization': jwt}
    response = requests.get(url, headers=headers)
    rescode = response.status_code

    message = '아직 일정을 시작하지 않았습니다.'

    if (rescode == 200):
        result = response.json()
        meta = result.get('meta')
        tasks = result.get('tasks')

        complete = meta['complete']
        inComplete = meta['inComplete']

        if inComplete > 0:
            current_task = tasks[complete]
            current_title = current_task['title']

            message = f'지금까지 {complete + inComplete}개의 태스크 중 {complete}개를 완수했고,' \
                      f'지금은 {current_title}를 수행중이오.' \
                      f'앞으로 남은 태스크는 {inComplete} 가지오.'
        else:
            message = '오늘의 임무를 모두 완수하였소.'

    respon = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            'message_list': message,
            'rescode': rescode
        }
    }
    return JsonResponse(respon)


@csrf_exempt
def taskdetail_check(request):
    url = 'https://dev.sixthings.tech/api/tasks'
    jwt = getattr(settings, 'JWT')
    headers = {'Authorization': jwt}
    response = requests.get(url, headers=headers)
    rescode = response.status_code

    complete = 0
    message_detail = '태스크를 등록하시오.'

    if (rescode == 200):
        result = response.json()
        meta = result.get('meta')
        tasks = result.get('tasks')
        complete = meta['complete']
        inComplete = meta['inComplete']

        if inComplete > 0:
            current_task = tasks[complete]
            if current_task.get('todos'):
                todos = current_task['todos']
                word = ''
                for todo in todos:
                    if todo['isCompleted'] == False:
                        word = word + todo['content'] + ', '
                current_title = current_task['title']
                message_detail = current_title + f'에 완료하지 않은 항목은 {word}이오.'
                if word == '':
                    message_detail = current_title + f'의 모든 세부항목을 완료했소. 다음 태스크로 넘어가길 추천하겠소.'
        else:
            message_detail = '오늘의 임무를 모두 완수하였소.'

    respon = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            'current_number': complete,
            'message_detail': message_detail,
            'rescode': rescode
        }
    }
    return JsonResponse(respon)
