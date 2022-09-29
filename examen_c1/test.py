import random
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

def eating(person,index,people):
    rPerson=people[index]
    if rPerson==8:
        rPerson=0

    mutex.acquire()
    if person.stick==1 and rPerson.stick==1:
        person.stick=2
        rPerson.stick=0
        print(f'------------Person {person.number} eating NOW with chopsticks------------')
        print(f'|\tInitial data:{person.getAll()}  |')
        time.sleep(3)
        person.stick=1
        person.full=True
        rPerson.stick=1
        print(f'|\t\t***Person {person.number} just finished eating***\t  |')
        print(f'|\t  Final Data:{person.getAll()}   |')
        print('-----------------------------------------------------------')
        mutex.release()
    


def table(people):
    index=0
    for person in people:
        personEating=threading.Thread(target=eating, args=[person,index,people])
        print(f'Person {person.number} ready to eat (waiting for chopsticks)......')
        personEating.start()
        index+=1



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