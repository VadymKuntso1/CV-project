from django.shortcuts import render
import requests

def index(request):

    return render(request, 'parsing/index.html', {'title':'Sites parsing','url': ''})


def search(request):
    try:
        if request.method == 'POST' and not request.POST.get('url',None)=='':
            url = request.POST.get('url',None)
            if not url.endswith("/"):
                url = url + '/'
            print(url)
            response = requests.get(url)
            res_parse_list = []
            response_text = response.text
            response_parse = response_text.split('<img ')
            for parse_elem_1 in response_parse:
                for parse_elem_2 in parse_elem_1.split('">'):
                    for parse_elem_3 in parse_elem_2.split('src="'):
                        for parse_elem_4 in parse_elem_3.split('"'):
                            if parse_elem_4.endswith('.png') or parse_elem_4.endswith('.jpg') or parse_elem_4.endswith('.jpeg'):
                                if parse_elem_4.lower().startswith('htt'):
                                    res_parse_list.append(parse_elem_4)
                                else:
                                    if (parse_elem_4.startswith('/')):
                                        res_parse_list.append('' + url + parse_elem_4[1:])
                                    else:
                                        res_parse_list.append(url + parse_elem_4)

            return render(request, 'parsing/index.html', {'urls': res_parse_list, 'url': url, 'title': 'Sites parsing'})
        else:
            return render(request, 'parsing/index.html', {'title': 'Sites parsing','url': ''})
    except( Exception ):
        return render(request, 'parsing/index.html', {'title': 'Sites parsing', 'url': '', 'error':'Enter valid value'})
