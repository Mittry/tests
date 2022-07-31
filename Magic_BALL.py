from random import *

answer = ['Undoubtedly', 'It seems to me - yes', 'Not yet clear', 'try again', 'Do not even think', 'Agreed',
          'Most Likely', 'Ask Later', 'My Answer Is No', 'No doubt', 'Good prospects', 'Best not to tell',
          'According to my knowledge - no', 'Definitely yes', 'The signs say yes', 'It is impossible to predict now',
          'The prospects are not very good', 'You can be sure of it', 'Yes Concentrate and ask again', 'Very doubtful']
def random_answer():
    return choice(answer)
def main():
    question = input('🦍: Lets ask me a question: ')
    print(random_answer())
print('🦍:I am a magic ball  Mitry, and I know the answer to any of your questions.')
name = input("🦍: What's your name?")
print("🦍: Suuuu", name )
while True:
    main()
    want_continue = input('🦍: Would you like to ask one more question? Only the answer \'yes\' will be accepted as:')

    if want_continue.lower() == 'yes':
        continue
    else:
        print('🦍: Good luck, have fun!')
        break

