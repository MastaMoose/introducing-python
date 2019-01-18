# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:05:23 2019
Purpose: to create a finite state machine in python
    especiall to emulate the behaviour of the coke vending machine 
    example shown on the labview "state machines" tutorial from their website
@author: MastaMoose
"""

class Coke_Machine():
    '''The acceptable states are:
       "Nothing"
       "5 cents"
       "10 cents"
       "Dispanse"
    '''
    def __init__(self):
        self.state = "Nothing"
    def set_state(self, state):
        self.state = state
    def deposit_coin(self, coin):
        self.total = self.change_state(coin)
    def print_state(self):
        print("Current state is, ", self.state)
        return self.state
        
    def change_state(self,coin):
        if coin == "Dime":
            if self.state != "Nothing":
                self.set_state("Dispense")
            else:
                self.set_state(self.state)               
        elif coin == "Nickel":
            if self.state == "Nothing":
                self.set_state("5 cents")
            elif self.state == "5 cents":
                self.set_state("10 cents")
            elif self.state == "10 cents":
                self.set_state("Dispense")
            else:
                self.set_state(self.state)
        else:
            self.set_state(self.state)
                    
class User():
    '''This class models the behavior of a dude with money of Nickels
        and dimes and only accepts "Nickel" or "Dime" keywords
        the money variable is actually a list of coins that will be deposited
        '''
    
    def __init__(self, money):
        self.money = money
    def put_in_machine(self):
        coin = self.money.pop()
        print("putting in {} coin".format(coin))
        return coin 

def main():
    Machine1 = Coke_Machine()
    #John = User(["Nickel","Nothing","Dime"])
    Dave = ["Nickel","Dime","Dime"]
    
    print("Starting state of vending machine is", Machine1.print_state())
    for steps in Dave:
        print("Dave puts in ", steps)
        Machine1.deposit_coin(steps)
        Machine1.print_state()
    print("final state of Machine1 is ", Machine1.print_state())        
       

if __name__ == "__main__":
    main()