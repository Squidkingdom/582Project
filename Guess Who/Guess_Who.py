# Import necessary modules
import random

# Define a Character class to hold attributes for each character
class character:
    def __init__(self, name, gender, hair_color, eye_color, hair_short, facial_hair, head_accessory, glasses, head_cover, earring):
        # Assign each attribute to the character
        self.name = name 
        self.gender = gender 
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.hair_short = hair_short 
        self.facial_hair = facial_hair 
        self.head_accessory = head_accessory 
        self.glasses = glasses 
        self.head_cover = head_cover
        self.earring = earring

# Define a list of character instances with their respective attributes
characters = [
    character("AMY", "FEMALE", "BLACK", "BROWN", True, False, True, True, False, False),
    character("AL", "MALE", False, "GREEN", False, True, False, True, False, False),
    character("SAM", "MALE", "BLACK", "GREEN", True, True, True, False, True, False),
    character("SOFIA", "FEMALE", "BROWN", "GREEN", True, False, False, False, False, True),
    character("OLIVIA", "FEMALE", "BLACK", "BROWN", False, False, False, False, False, False),
    character("MIKE", "MALE", "BLACK", "BROWN", True, False, True, False, True, False),
    character("DAVID", "MALE", "BLOND", "BROWN", True, True, True, False, True, False),
    character("FARAH", "FEMALE", "BLACK", "GREEN", False, False, False, False, False, False),
    character("BEN", "MALE", "BROWN", "BROWN", True, False, False, True, False, False),
    character("JORDAN", "MALE", "BLACK", "BROWN", False, True, False, False, False, True),
    character("LAURA", "FEMALE", "BLACK", "GREEN", False, False, False, False, False, True),
    character("LEO", "MALE", "SILVER", "BROWN", True, True, False, False, False, False),
    character("LIZ", "FEMALE", "SILVER", "BLUE", False, False, False, True, False, False),
    character("MIA", "FEMALE", "BLACK", "BROWN", False, False, False, False, False, False),
    character("NICK", "MALE", "BLOND", "BROWN", True, False, False, False, False, True),
    character("LILY", "FEMALE", "BROWN", "GREEN", False, False, True, False, True, False),
    character("JOE", "MALE", False, "BROWN", False, True, True, True, False, False),
    character("GABE", "MALE", "BLACK", "BROWN", True, False, False, False, False, False),
    character("ERIC", "MALE", "BLACK", "BLUE", True, False, False, False, False, False),
    character("EMMA", "FEMALE", "ORANGE", "BROWN", False, False, False, False, False, False),
    character("CARMEN", "FEMALE", "SILVER", "BROWN", True, False, True, False, False, True),
    character("DANIEL", "MALE", "ORANGE", "GREEN", False, True, False, False, False, False),
    character("RACHEL", "FEMALE", "BROWN", "BLUE", False, False, True, True, False, True),
    character("KATIE", "FEMALE", "BLOND", "BLUE", False, False, True, False, True, False)
]

# Define question types the computer can ask
question_types = {
    "gender": {
        "type": "string",
        "attribute": "gender",
        "prompt": "Is your character {value}?"
    },
    "hair_color": {
        "type": "string",
        "attribute": "hair_color",
        "prompt": "Does your character have {value} colored hair?"
    },
    "eye_color": {
        "type": "string",
        "attribute": "eye_color",
        "prompt": "Does your character have {value} eyes?"
    },
    "hair_short": {
        "type": "boolean",
        "attribute": "hair_short",
        "prompt": "Does your character have short hair?"
    },
    "facial_hair": {
        "type": "boolean",
        "attribute": "facial_hair",
        "prompt": "Does your character have facial hair?"
    },
    "head_accessory": {
        "type": "boolean",
        "attribute": "head_accessory",
        "prompt": "Does your character have a head accessory?"
    },
    "glasses": {
        "type": "boolean",
        "attribute": "glasses",
        "prompt": "Does your character wear glasses?"
    },
    "head_cover": {
        "type": "boolean",
        "attribute": "head_cover",
        "prompt": "Does your character have a head cover?"
    },
    "earring": {
        "type": "boolean",
        "attribute": "earring",
        "prompt": "Does your character wear an earring?"
    }
}

# Set of boolean questions already asked (to avoid duplicates)
asked_boolean = set()

# Function for the computer to randomly pick its secret character
def pick_cpu_player():
    return random.choice(characters)

# Function for the computer to take its turn
def computer_turn(candidates):
    global asked_boolean

    # If only one candidate left, computer makes a guess
    if len(candidates) == 1:
        guess = candidates[0]
        print(f"\nComputer: Is your character {guess.name}?")
        user_response = input("Yes/No: ").strip().lower()
        if user_response.startswith("y"):
            print("Computer: I win! (You lose!)")
            return None  # Game over
        else:
            print("Computer: Hmm... That's odd. Let's continue anyway.")
            return candidates

    available_questions = []  # List to store potential questions

    # Loop through all question types
    for key in question_types:
        q_data = question_types[key]
        attr = q_data["attribute"]

        # If boolean question
        if q_data["type"] == "boolean":
            if key in asked_boolean:
                continue  # Skip if already asked
            count_yes = sum(1 for cand in candidates if getattr(cand, attr) is True)
            count_no = len(candidates) - count_yes
            if count_yes > 0 and count_no > 0:
                available_questions.append((key, None, q_data["prompt"], q_data))

        # If string (color, gender, etc.)
        else:
            if key == "gender":
                possible_values = ["MALE", "FEMALE"]
            elif key == "hair_color":
                possible_values = ["BLACK", "BROWN", "BLOND", "SILVER", "ORANGE"]
            elif key == "eye_color":
                possible_values = ["BROWN", "GREEN", "BLUE"]
            else:
                possible_values = []

            for value in possible_values:
                count_yes = sum(1 for cand in candidates 
                                if isinstance(getattr(cand, attr), str) and getattr(cand, attr).upper() == value)
                count_no = len(candidates) - count_yes
                if count_yes > 0 and count_no > 0:
                    prompt = q_data["prompt"].format(value=value)
                    available_questions.append((key, value, prompt, q_data))

    # If no good elimination question, computer makes a guess
    if not available_questions:
        guess = random.choice(candidates)
        print(f"\nComputer: Is your character {guess.name}?")
        user_response = input("Yes/No: ").strip().lower()
        if user_response.startswith("y"):
            print("Computer: I win! (You lose!)")
            return None
        else:
            print("Computer: Hmm... That's odd. Let's continue anyway.")
            return candidates

    # Randomly pick one question
    chosen_question = random.choice(available_questions)
    key, chosen_value, prompt, q_data = chosen_question

    # Mark boolean questions as asked
    if q_data["type"] == "boolean":
        asked_boolean.add(key)

    # Ask the question
    print("\nComputer asks:", prompt)
    user_ans = input("Yes/No: ").strip().lower()

    # Filter candidates based on answer
    if q_data["type"] == "boolean":
        if user_ans.startswith("y"):
            new_candidates = [cand for cand in candidates if getattr(cand, q_data["attribute"]) is True]
        else:
            new_candidates = [cand for cand in candidates if getattr(cand, q_data["attribute"]) is False]
    else:
        if user_ans.startswith("y"):
            new_candidates = [cand for cand in candidates 
                              if isinstance(getattr(cand, q_data["attribute"]), str) and getattr(cand, q_data["attribute"]).upper() == chosen_value]
        else:
            new_candidates = [cand for cand in candidates 
                              if not (isinstance(getattr(cand, q_data["attribute"]), str) and getattr(cand, q_data["attribute"]).upper() == chosen_value)]
    return new_candidates

# Answering user questions about the computer's chosen character
def answer_user_question(cpu_character, question):
    lower_question = question.lower().strip()

    # Check for gender questions
    if "male" in lower_question or "female" in lower_question:
        if "male" in lower_question and cpu_character.gender.upper() == "MALE":
            return "Yes"
        elif "female" in lower_question and cpu_character.gender.upper() == "FEMALE":
            return "Yes"
        else:
            return "No"

    # Check for hair color questions
    if "hair" in lower_question and any(color in lower_question for color in ["black", "brown", "blond", "silver", "orange"]):
        for color in ["BLACK", "BROWN", "BLOND", "SILVER", "ORANGE"]:
            if color.lower() in lower_question:
                if isinstance(cpu_character.hair_color, str) and cpu_character.hair_color.upper() == color:
                    return "Yes"
                else:
                    return "No"

    # Check for eye color questions
    if "eyes" in lower_question:
        for color in ["BROWN", "GREEN", "BLUE"]:
            if color.lower() in lower_question:
                if cpu_character.eye_color.upper() == color:
                    return "Yes"
                else:
                    return "No"

    # Check for boolean features
    if "short" in lower_question and "hair" in lower_question:
        return "Yes" if cpu_character.hair_short else "No"
    if "facial hair" in lower_question:
        return "Yes" if cpu_character.facial_hair else "No"
    if "head accessory" in lower_question:
        return "Yes" if cpu_character.head_accessory else "No"
    if "glasses" in lower_question:
        return "Yes" if cpu_character.glasses else "No"
    if "head cover" in lower_question:
        return "Yes" if cpu_character.head_cover else "No"
    if "earring" in lower_question:
        return "Yes" if cpu_character.earring else "No"
    
    # Default fallback
    return "I don't understand the question."

# Main gameplay loop
def play_game():
    global asked_boolean
    asked_boolean = set()  # Reset asked questions

    print("Welcome to Guess Who!")
    input("Click enter once you have selected your secret character (from the list).")
    
    # Computer picks a secret character
    cpu_character = pick_cpu_player()
    user_candidates = characters.copy()

    # Game loop
    while True:
        # Computer's turn
        updated_candidates = computer_turn(user_candidates)
        if updated_candidates is None:
            break
        user_candidates = updated_candidates
        
        if len(user_candidates) == 0:
            print("There are no characters left. Something went wrong with the elimination. Game over.")
            break
        
        # User's turn
        while True:
            print("\nYour turn! Ask me a yes/no question about my character, or if you're ready to guess, type \"I'm ready to make a guess.\"")
            user_input = input("Your input: ").strip()
            if user_input.lower().startswith("i'm ready to make a guess"):
                print("Computer: Ok, what's your guess?")
                guess_input = input("Your guess: ").strip().upper()
                if guess_input == cpu_character.name:
                    print("You win!")
                    return
                else:
                    print("No, that's not my character.")
                break
            else:
                # Process question
                answer = answer_user_question(cpu_character, user_input)
                if answer == "I don't understand the question.":
                    print(answer, "Please rephrase your question.")
                    continue
                else:
                    print("Computer answers:", answer)
                break

# Entry point
def main():
    play_game()

# Start the game
if __name__ == "__main__":
    main()

'''
If we decide to use dictionaries:
AMY = {
    "name": "AMY",
    "gender": "FEMALE",
    "hair_short": True,
    "hair_color": "BLACK",
    "facial_hair": False,
    "head_accessory": True,
    "glasses": True,
    "head_cover": False,
    "earring": False,
    "eye_color": "BROWN"
}
'''
