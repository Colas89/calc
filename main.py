# coding=utf-8
print('\nЗдравствуйте!')


def choice():  # Меню
    restart = True
    while restart:
        choise = input('\nВыбирете пункт:\n'
                       '---------------\n'
                       'Калькулятор - (1)\n'
                       'Выход - (2)\n'
                       '----------------\n'
                       '>>>>> ')
        if choise == '1':
            print('\nВы выбрали калькулято\n')
            import calc
        elif choise == '2':
            return
        else:
            print(
                'Вы ввели символ не из предложеных.\nПовторите еще раз.\n---------------------------')
            restart = True


choice()