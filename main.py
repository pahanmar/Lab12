import calc
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    progam_is_running = True

    while (progam_is_running):

        calc.run()

        answer = input('Желаете продолжить?\n'

                       ' Введите + если да и прочий символ, если нет: ')

        if answer != '+':
            progam_is_running = False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
