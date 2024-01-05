class AnimalGame:
    def __init__(self):
        self.animal = "elephant"  # You can change this to any other animal
        self.questions = {
            "mammal": lambda x: x.lower() == "yes",
            "herbivore": lambda x: x.lower() == "yes",
            "big ears": lambda x: x.lower() == "yes",
            # Add more characteristics/questions as needed
        }

    def play(self):
        print("Welcome to Guess the Animal!")
        print("Think of an animal and answer the following questions with 'yes' or 'no'.")

        for question in self.questions:
            answer = input(f"Is the animal a {question}? ")
            if self.questions[question](answer):
                print("Yes! It could be the animal.")
            else:
                print("No, it's not the animal.")

        print(f"The animal is probably a {self.animal.capitalize()}.")

if __name__ == "__main__":
    game = AnimalGame()
    game.play()
