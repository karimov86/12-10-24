from random import randint

answer = randint(1,10)

def guess(number_guess, answer):
    if number_guess == answer:
        print('you are a genius')
        return True
    if not(1<=number_guess<=10):
        print('number has to be 1-10')
        return False
    
    print('try again')
    return False

if __name__ == '__main__':
    while True:
        try:
            number_guess = int(input('guess a number 1-10: '))
            if guess(number_guess, answer):
                break
        except ValueError:
            print('Invalid input please enter a number')
