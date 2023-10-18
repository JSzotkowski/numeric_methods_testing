class UserConsole:
    @staticmethod
    def print_optimization_finished(record):
        print(f'Optimization of {record.get_label()} has finished...')

    @staticmethod
    def print_optimizations_finished():
        print(f'Optimizations have finished...')
        UserConsole.clear()

    @staticmethod
    def clear():
        for _ in range(8):
            print(" ")

    @staticmethod
    def let_user_select_from_menu(menu, message="You can do following things. Please select what you want to do."):
        print(message + "\n")

        for i, item in enumerate(menu):
            print(f'{i} - {item}')

        ix = int(input(f'\nEnter option number: '))

        assert 0 <= ix < len(menu)

        return ix
