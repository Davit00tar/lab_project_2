def isemail(data):
    domains = ['gmail.com', 'yahoo.com', 'mail.ru', 'yandex.ru', 'outlook.com',
               'inbox.com']
    answer = False
    if '@' in data:
        end_part = data[data.index('@') + 1:]
        if end_part in domains:
            answer = True
    return answer


def isurl(data):
    protocols = ['https', 'http']
    web_pages = ['com', 'ru', 'org', 'io', 'am']
    subdomain = 'www'
    answer = False
    if '://' in data:
        mark = data.index('://')
        protocol = data[:mark]
        rest = data[mark + 3:]
        rest_lst = rest.split('/')
        page_lst = rest_lst[0].split('.')
        if page_lst[0] == subdomain and page_lst[-1] in web_pages and protocol in protocols:
            answer = True
    return answer


def isdate(data):
    answer = False
    data_lst = data.split('.')
    if len(data_lst) < 3:
        return answer
    day = data_lst[0]
    month = data_lst[1]
    year = data_lst[2]
    if day.isnumeric() and int(day) <= 31 and int(day) >= 1:
        if month.isnumeric() and int(month) <= 12 and int(month) >= 1:
            if year.isnumeric() and int(year) >= 0:
                answer = True
    return answer


def isnumber(data):
    answer = False
    i = 0
    k = 0
    if data[i] =='-':
        i = 1
        k = 1
    while i < len(data):
        if data[i].isnumeric() or data[i] == '.':
            k += 1
        i += 1
    if i == k:
        answer = True
    return answer

def iscard(data):
    answer = False
    if data.isnumeric() and len(data) == 16:
        answer = True
    return answer

def isphone(data):
    answer = False
    start = ['099', '098', '091', '097', '093', '077', '041', '010']
    if data.isnumeric() and len(data) == 9 and data[:3] in start:
        answer = True
    return answer












