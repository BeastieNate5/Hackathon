import random

suits = ("terms" , "definition" )
terms = ("Greenhouse Gas Emission", "Renewable Energy", "Fossil Fuels", "Carbon Dioxide (CO2)", "What is a way of reducing CO2 in the atmosphere?", "What initiatives can I take to improve the community?", "What can I do to help reduce my carbon footprint?", "How are people around you affected by climate change?", "Why should climate change concerns you?", "Intergovernmental Panel on Climate Change"  )
definitions = ("An instance in which a greenhouse gas is released into the air by an activity such as fossil fuel burning, industrial agriculture, and melting permafrost ",
               " Energy that comes from naturally replenishing sources. Does NOT produce greenhouse gases", 
               "A source of a non-renewable fuel that is formed by dead organisms that lived over a million years ago. Main source of greenhouse gases.", 
               "The primary greenhouse gas and driver of climate change",
             "Doing something designed to reduce greenhouse gas emissions", 
             "Calculate and reduce your carbon footprint, plant trees, conserve water, and spread the word", 
             "Using a bike as opposed to a car, use public transit, and recycling", 
             "Extreme weathers like hurricanes, wildfires and droughts that are a threat to world's food supply. These things have driven people out of their homes and also caused an increase to hunger and poverty.", 
             "Higher electrical bills, rising taxes, damage to your home/belongings, more allergies/health risks, water quality could suffer, expensive health insurance, and outdoors could become unbearable.",
             "United Nations organization that helps mitigate climate change." )


class card():
    def __init__ (self, suit, text, number,up):
        self.suit = suit
        self.text = text
        self.number = number
        self.up = up

    def __str__ (self ):
        if self.up:
            return(self.text)
        else:
            return ("x")


class deck():

    def __init__ ( self):
        self.all_cards = []
       
        for x in range (0,10):
            created_card = card("term", terms[x], x + 1, False )
            self.all_cards.append(created_card)
        for x in range (0, 10):
            created_card = card("definition" , definitions[x], x + 1, False)
            self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop(0)

class board():

    def __init__ (self):
        self.board = ['?', '?', '?', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         '?', '?', '?', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display(self):
        print(f' {self.board[1]} | {self.board[2]} | {self.board[3]} | {self.board[4]} | {self.board[5]}')              
        print('--------------------')
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]} | {self.board[9]} | {self.board[10]}')
        print('--------------------')
        print(f' {self.board[11]} | {self.board[12]} | {self.board[13]} | {self.board[14]} | {self.board[15]}'  )            
        print('--------------------')
        print(f' {self.board[16]} | {self.board[17]} | {self.board[18]} | {self.board[19]} | {self.board[20]}')


    


print('\n'*100)
new_deck = deck()
board = board()
won = False
new_deck.shuffle()
for x in range (1,len(new_deck.all_cards)+1):
    board.board[x] = new_deck.all_cards[x-1]

print("Hello judges and players! We have made a 'concentration' game where you match terms to the")
print("definitions, and problems to solutions. This is a fun and engaging way to bring awareness to SPACE,")
print("and how to reduce it. When many people hear 'climate change,' they think, 'oh politics, that's")
print("boring.' We wish to change that viewpoint via this game.")
print()

while not won:

    board.display()
    print()
    print("please select two cards to match. If the term matches the definition, they will be removed.")
    print("The cards are numbered from 1-20 where 1 is the top left, and you move across.")
    print()
    first_card = int(input("Enter the first card: "))
    second_card = int(input("Enter the second card: "))
    print()

    holder1 = board.board[first_card]
    holder2 = board.board[second_card]

    holder1.up = True
    holder2.up = True

    print(holder1.suit  , ": " , holder1)
    print(holder2.suit , ": " , holder2)
    print()

    if ( holder1.suit == holder2.suit):
        print("Please match a term with it's definition")
        print()
        board.board[first_card].up = False
        board.board[second_card].up = False

    else:
        guess = str(input("Do you think the definition matches the term? Y or N?: "))
        if (holder1.number == holder2.number):
            if (guess == "Y"):
                print("Correct, the definition matches the term")
                print()
            else:
                print("Actually, it is correct. The definition does in fact match the term")
                print()
            board.board[first_card] = " "
            board.board[second_card] = " "
            for x in board.board:
                if (x!=" "):
                    won = False
                    break
            else:
                won = True
        else:
            if (guess == "Y"):
                print("incorrect, the term and definition don't match")
                print()
            else:
                print("Yes, the definition does not match the definition")
                print()
            board.board[first_card].up = False
            board.board[second_card].up = False
            
                
    ready = "N"
    while (ready != "Y"):
        ready = str(input("Are you ready to continue? Y or N ?: "))
    print("\n"*100)
print("Yay, you won")
print("Hopefully you learned a lot about climate change!")



    










        



