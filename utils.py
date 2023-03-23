import os


path_script = os.path.join('texts', 'script.txt')
path_log = os.path.join('texts', 'log.txt')


def load_script(keyword):
    with open(path_script, 'r', encoding='utf-8') as f:
        text = f.read().split('\n')
    match keyword:
        case 'greetings':
            return text[0]
        case 'inst':
            return text[1]
        case 'action1':
            return text[2]
        case 'action1/req':
            return text[3]
        case 'action2':
            return text[4]
        case 'action2/req':
            return text[5]
        case 'store/state':
            return text[6]
        case 'shop/state':
            return text[7]
        case 'for/end':
            return text[8]
        case 'start':
            return text[9]
        case 'end':
            return text[10]


def load_log(keyword):
    with open(path_log, 'r', encoding='utf-8') as f:
        text = f.read().split('\n')
    match keyword:
        case 'info/req':
            return text[0]
        case 'check/req':
            return text[1]
        case 'req/error':
            return text[2]
        case 'rmv/error':
            return text[3]
        case 'store/add':
            return text[4]
        case 'shop/add':
            return text[5]
        case 'loc/error':
            return text[6]
