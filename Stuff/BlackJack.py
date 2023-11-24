#Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

#Colors
colors = ["Aqua","Blue","Fuchsia","Lime","Maroon","Navy","Orange","Red","White","Yellow"]

#Final State Machine
fsm = {
    "playerWaits" : ["Hit or stand?"],
    "hits" : ["Another one?"],
    "stand": [" "],
    "resultWin": ["You WIN!"],
    "resultLose": ["Dealer WINs!"],
    "waiting": ["Wait..."],
    "resultWait": ["Wait..."]
}

#Global vars
Win, Lose, Draft = 0, 0, 0
gameState = "playerWaits"
message = fsm[gameState]

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

in_play = False

#Classes
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank
        
    def __repr__(self):
        return "Card('" + self.suit + "','" + self.rank + "')"

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.stroke = "Hand contains "
        self.cards = []
        
    def __str__(self):
        if len(self.cards) != 0:
            for i in range(len(self.cards)):
                line = str(Card.get_suit(self.cards[i])) + str(Card.get_rank(self.cards[i]))
                if line != None:
                    self.stroke += str(line) + " "
                    return (self.stroke)
        else:
            return self.stroke
        
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        s = 0
        A_check = False
        for i in self.cards:
            if str(i)[1] == "A":
                A_check = True
            s += VALUES[str(i)[1]]
        if s + 10 <= 21:
            if A_check == True:
                s += 10
        return s
    
    def draw(self, canvas, pos):
        for j in range(len(self.cards)):
            Card.draw(self.cards[j], canvas, (pos[0] + pos[0]*3*j, pos[1]))
   
class Deck:
    def __init__(self):
        self.stroke = ""
        self.decka = []
        for i in SUITS:
            for j in RANKS:
                self.decka.append([i+j])

    def shuffle(self):
        random.shuffle(self.decka)

    def deal_card(self):
        card = random.choice(self.decka)
        self.decka.remove(card)
        return Card(card[0][0], card[0][1])
    
    def __str__(self):
        self.stroke = "Deck contains "
        for i in self.decka:
            for j in i:
                self.stroke += str(j) + " "
        return self.stroke
    
#Finale State Machine Logic
def next_state():
    global gameState, Win, Lose, message, in_play
    
    if gameState == "playerWaits":
        pass
    
    elif gameState == "hits":
        message = fsm[gameState]
        hitting()
        
    elif gameState == "stand":
        message = fsm[gameState]
        gameState = "waiting"
        next_state()
        
    elif gameState == "resultLose":
        in_play = False
        Lose += 1
        message = fsm[gameState]
        
    elif gameState == "resultWin":
        in_play = False
        Win += 1
        message = fsm[gameState]
    
    elif gameState == "waiting":
        message = fsm[gameState]
        dealer()
        
    elif gameState == "resultWait":
        message = fsm[gameState]
        results()

#FSM Logic methods
def dealers():
    global gameState
    
    if deal_hand.get_value() <= 17:
        deal_hand.add_card(my_deck.deal_card())
        gameState = "waiting"
        next_state()
    
    elif deal_hand.get_value() > 17: 
        gameState = "resultWait"
        next_state()
        
def results():
    global gameState, Draft
    
    timer.stop()
    
    if deal_hand.get_value() > 21 or deal_hand.get_value() < my_hand.get_value():
        in_play = False
        gameState = "resultWin"
        next_state()
    elif deal_hand.get_value() == my_hand.get_value():
        in_play = False
        gameState = "resultLose"
        Draft += 1
        next_state()
    else:
        in_play = False
        gameState = "resultLose"
        next_state()
        
def deal():
    global my_deck, my_hand, deal_hand, hand_cnt, Lose, gameState, in_play, message

    timer.stop()
    
    gameState = "playerWaits"
    message = fsm[gameState]
    
    if in_play == True:
        Lose += 1
    
    my_deck = Deck()
    my_hand = Hand()
    deal_hand = Hand()

    my_deck.shuffle()
    
    my_hand.add_card(my_deck.deal_card())
    my_hand.add_card(my_deck.deal_card())
    
    hand_cnt = 2
    
    deal_hand.add_card(my_deck.deal_card())
    deal_hand.add_card(my_deck.deal_card())

    in_play = True
    next_state()

def dealer():
    global Lose, Win, gameState, in_play
    
    if gameState == "waiting":
        timer.start()
               
def hit():
    global gameState
    
    if (in_play == True) and gameState == "playerWaits":
        gameState = "hits"
        next_state()
    else:
        pass
    
def hitting():
    global my_hand, my_deck, hand_cnt, Lose, gameState
    
    if gameState == "hits":
        
        if my_hand.get_value() <= 21:
            my_hand.add_card(my_deck.deal_card())
            hand_cnt += 1
            if my_hand.get_value() > 21:
                gameState = "resultLose"
                next_state()
            else:
                gameState = "playerWaits"
                next_state()

        else:
            gameState = "resultLose"
            next_state()
            
def stand():
    global gameState
    
    if in_play == True and gameState == "playerWaits":
        gameState = "stand"
        next_state()

#Canvas        
def draw(canvas):
    #player box
    canvas.draw_line([235, 432], [365, 432], 4, "Black")
    canvas.draw_line([235, 388], [365, 388], 4, "Black")
    canvas.draw_line([235, 388], [235, 432], 4, "Black")
    canvas.draw_line([365, 388], [365, 432], 4, "Black")
    
    #dealer box
    canvas.draw_line([235, 188], [365, 188], 4, "Black")
    canvas.draw_line([235, 232], [365, 232], 4, "Black")
    canvas.draw_line([235, 232], [235, 188], 4, "Black")
    canvas.draw_line([365, 232], [365, 188], 4, "Black")
    
    #DILER AND YA
    canvas.draw_text("Player", [240, 420], 36, colors[0], "monospace")
    canvas.draw_text("Dealer", [240, 220], 36, colors[1], "monospace")

    #RUBASHKA DLYA COLODI
    canvas.draw_image(card_back, (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]), CARD_BACK_SIZE, (10, 398), CARD_BACK_SIZE, 1.575)

    #RISUNOK KARTOCHEK
    my_hand.draw(canvas, [30, 450])
    deal_hand.draw(canvas, [30, 250])

    #IGRA AND STATUS
    canvas.draw_text("BlackJack", [190, 50], 48, colors[2], "monospace")
    canvas.draw_text(str(message[0]), [180, 150], 48, colors[3])

    #lines
    canvas.draw_line([0, 65], [600, 65], 3, "Black")
    canvas.draw_line([0, 560], [600, 560], 3, "Black")
    
    #WINS AND LOSES
    canvas.draw_text("Wins: " + str(Win) + " Loses: " + str(Lose) + " (Draft: " + str(Draft) + ")", [20, 590], 24, colors[4])

    #RUBASHKA KARTI DILERA
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (65, 298), CARD_BACK_SIZE)
    else:
        deal_hand.draw(canvas, [30, 250])

#color choice
def colorr():
    global colors
    
    random.shuffle(colors)
        
#Frames
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Раздать", deal, 200)
frame.add_button("Ещё",  hit, 200)
frame.add_button("Хватит", stand, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000, dealers)
color_timer = simplegui.create_timer(500, colorr)

deal()

frame.start()
color_timer.start()