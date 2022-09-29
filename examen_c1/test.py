import random
from re import A
import threading
import time

mutex=threading.Lock()


class Person:
    def __init__(self,stick, full,number):
        self.stick=stick
        self.full=full
        self.number=number
    def getAll(self):
        return f"[sticks: {self.stick} ,number: {self.number} ,full: {self.full}]"

def eating(person):
    mutex.acquire()
    person.stick=2
    print(f'------------Person {person.number} eating NOW with chopsticks------------')
    print(f'|\tInitial data:{person.getAll()}  |')
    time.sleep(3)
    person.stick=1
    person.full=True
    print(f'|\t\t***Person {person.number} just finished eating***\t  |')
    print(f'|\t  Final Data:{person.getAll()}   |')
    print('-----------------------------------------------------------')
    mutex.release()
    


def table(people):
    for person in people:
        personEating=threading.Thread(target=eating, args=[person])
        print(f'Person {person.number} ready to eat (waiting for chopsticks)......')
        personEating.start()



def printRandom(people):
    time.sleep(int(random.uniform(3,24)))
    print('\n\t**************Random test*************')
    for singleP in people:
        print('\t*',singleP.getAll(),'*')
    print('\t************************************\n')
    

def printAtEnd(people):
    time.sleep(28)
    print('\n\t*************final states*************')
    for singleP in people:
        print('\t*',singleP.getAll(),'*')
    print('\t*************************************\n')

def startCounter(people):
    hiloToPrint =threading.Thread(target=printRandom, args=[people])
    hiloToPrint2=threading.Thread(target=printAtEnd,args=[people])
    hiloToPrint.start()
    hiloToPrint2.start()

def main():
    people=[]
    for i in range (0,8):
        person = Person(1,False,i+1)
        people.append(person)
    table(people)
    startCounter(people);
    
    
if __name__ == "__main__":
    main()