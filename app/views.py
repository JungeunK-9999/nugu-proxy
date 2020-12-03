from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from django.conf import settings
import json
from urllib.request import Request, urlopen


# Create your views here.

@csrf_exempt
def task_list(request):
    url = 'http://dev.sixthings.tech/api'
    api_request = Request(url)
    response = urlopen(api_request)
    rescode = response.getcode()
    ctx = {'code': rescode, 'msg': '에러'}
    # rescode = 200

    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        msg = result.get('msg')
        ctx['msg'] = msg

        respon = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {
                "msg": msg
            }
        }

    return JsonResponse(respon)


@csrf_exempt
def complete_task(request):
    url = 'http://dev.sixthings.tech/api/tasks/0?type=task'
    payload = {'completedAt': 1606137400000}
    jwtCH = getattr(settings, 'JWT_CH')
    print(jwtCH)
    print(type(jwtCH))
    headers = {'Authorization': jwtCH}
    response = requests.put(url, data=payload, headers=headers)
    rescode = response.status_code
    ctx = {'rescode': rescode, 'msg': '에러'}

    if (rescode == 200):
        result = response.json()
        msg = result.get('message')

        if msg == 'ok':
            ctx['msg'] = '태스크를 완수하였소.'

    respon = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            'ctx': ctx
        }
    }

    return JsonResponse(respon)


@csrf_exempt
def sample(request):
    url = 'https://3iyx959h3a.execute-api.ap-northeast-2.amazonaws.com/dev/test'
    payload = {'key': 'value'}
    response = requests.put(url, data=payload)
    rescode = response.status_code
    ctx = {'rescode': rescode, 'msg': '에러'}

    if (rescode == 200):
        result = response.json()
        method = result.get('method')
        msg = result.get('msg')
        ctx['result'] = method
        ctx['msg'] = msg

    return JsonResponse(ctx)


@csrf_exempt
def test(request):
    print('진입')
    ctx = {'code': 200, 'msg': 'hello, world', 'method': request.method}
    print('여기')
    return JsonResponse(ctx)
