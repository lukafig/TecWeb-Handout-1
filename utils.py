import json
def extract_route(string):
    #route = string.split('/', 1)[1].split(' ', 1)[0]
    route = string.split()[1][1:]
    return route

def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    return content

def load_data(file_name):
    with open("data/" + file_name, 'r') as file:
        data = json.load(file)
    return data

def load_template(file_name):
    with open("templates/" + file_name, 'r') as file:
        template = file.read()
    return template

def add_note(note):
    with open("data/notes.json", 'r+') as file:
        data = json.load(file)
        data.append(note)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def build_response(body='', code=200, reason='OK', headers=''):
    if code == 302:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n{body}\n'
    else:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n{body}'
    return response.encode()