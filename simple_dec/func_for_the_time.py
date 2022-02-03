from datetime import datetime


def working_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 18:
            func()
        else:
            pass  # Нерабочее время, выходим
    return wrapper

@working_hours
def writing_tests():
    print("Я пишу тесты на python!")

writing_tests()

