from groupgame.groupcard import groupcard



class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            gameover = gameover()
            self.card.append(gameover)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        pull_card = input("pull a card? [y/n] ")
        self.is_playing = (pull_card == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.)):card
            game_over = self.card[i]
            game_over.pull()
            self.score += game_over.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.card)):
            game_over = self.card[i]
            values += f"{game_over.value} "

        print(f"You pulled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)