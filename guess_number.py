from random import randint

number = randint(1, 100)
print(number)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число: '))
    if guess < number:
        print('Ваше число меньше, чем загадано.')

    if guess > number:
        print('Ваше число больше, чем загадано.')

    if guess == number:
        break

print('Отличная интуиция! Вы угадали число :)')


##"terminal.integrated.defaultProfile.windows": "C:\\Program Files\\Git\\git-bash.exe"
#"terminal.integrated.defaultProfile.windows": "Git Bash",

#{
#    "terminal.integrated.shell.windows": "C:\\Program Files (x86)\\Git\\bin\\bash.exe",
#    "terminal.integrated.shellArgs.windows": ["--login","-i"]
#}