import requests
from textwrap import fill


def main_loop():
    while True:
        print('==== To send prompt and get response type "prompt" to exit "exit"')
        command = str(input())

        match command.lower():
            case 'prompt':
                prompt_loop()
            case 'exit':
                break


def prompt_loop():
    print('\n==== You are in prompt typing mode')
    print('\t To end prompt typing simply press ENTER')

    prompt = ''
    while True:
        line = str(input())

        if not line:
            break

        prompt += line + '\n'

    print('==== Your prompt is:')
    print(prompt)

    print('==== Model\'s response')
    with requests.post('http://127.0.0.1:8000/send-prompt', json={"content": prompt}, stream=True) as response:
        for line in response.iter_lines():
            print(fill(line.decode('utf-8'), width=64))

    print('\n')

    return


if __name__ == '__main__':
    main_loop()
