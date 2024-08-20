import random
class flashcard:
	def __init__(self,term,definition):
		self.term=term
		self.definition=definition
		
class store:
    def __init__(self):
        self.cards=[]

    def add_card(self,term,definition):
        card=flashcard(term,definition)
        self.cards.append(card)

    def get_random_card(self):
        return random.choice(self.cards) if self.cards else None

    
class flashcardapp:
    def __init__(self):
         self.store=store()

    def add_flashcard(self):
         term=input("Enter the term=")
         definition=input("Enter the definition=")

         self.store.add_card(term,definition)

    def quiz(self):
        if not self.store.cards:
            print("No flashcards available. Add some first.")
            return
        
        card = self.store.get_random_card()
        user_answer = input(f"Term: {card.term}\nYour answer: ")
        
        if user_answer.strip().lower() == card.definition.strip().lower():
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is: {card.definition}")

def main():
    app = flashcardapp()
    
    while True:
        print("Flashcard App")
        print("1. Add Flashcard")
        print("2. Quiz")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            app.add_flashcard()
        elif choice == '2':
            app.quiz()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()


