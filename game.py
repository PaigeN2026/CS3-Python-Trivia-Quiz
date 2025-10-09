trivia1 = [
    {
        'question': 'the first avenger',
        'answer': 'captian america',
    },
    {
        'question': 'ragnarok',
        'answer': 'thor',
    },
    {
        'question': 'days of future past',
        'answer': 'x-men',
    },
    {
        'question': 'the incredible',
        'answer': 'hulk',
    },
    {
        'question': 'the wasp',
        'answer': 'ant-man',
    }
]

trivia2 = [
    {
        'question': 'AIF',
        'answer': 'avengers infinity war',
    },
    {
        'question': 'CA TWS',
        'answer': 'captain american the winter soldier',
    },
    {
        'question': 'DP&WV',
        'answer': 'deadpool and wolverine',
    },
    {
        'question': 'GOTG',
        'answer': 'guardians of the galaxy',
    },
    {
        'question': 'TB TNA',
        'answer': 'thunderbolts the new avengers',
    }
]

trivia3 = [
    {
        'question': '__a__ _a____e_',
        'answer': 'black panther',
    },
    {
        'question': '_o_i',
        'answer': 'loki',
    },
    {
        'question': '__a___e_ _i___',
        'answer': 'scarlet witch',
    },
    {
        'question': '_a_e_e_i_',
        'answer': 'daredevil',
    },
    {
        'question': 'sue storm',
        'answer': '_ue __o__',
    }
]

trivia4 = [
    {
        'question': '🕷️🧑‍🦰🕸️🏙️',
        'answer': 'spiderman',
    },
    {
        'question': '💎👱‍♀️🧊🧠',
        'answer': 'emma frost',
    },
    {
        'question': '🔥🧑‍🚀💨🌟',
        'answer': 'human torch',
    },
    {
        'question': '🕷️🖤🕶️🔫',
        'answer': 'black widow',
    },
    {
        'question': '🪖❄️🔪🦾',
        'answer': 'winter soldier',
    }
]

def ask_q(question, answer):
    is_correct = False
    # Display the question -> loop
    print(question)
    # Take user input -> input('').lower()
    user_answer = input("answer: ").lower()
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect.")
    # Check if user input matches correct answer -> conditions
    return is_correct


# calculate_score(total_questions, num_correct)

def main():
    print("Starting a new Marvel trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")
    print(f"⎯⎯⎯⟡⎯⎯⎯◎⎯⎯⎯⟡⎯⎯⎯")
    # Test out your ask_q function
        
    print(f"Identify the character or team from the clue.")
    for question in trivia1:
        q = question['question']
        a = question['answer']
        ask_q(q, a)
        print(f"")
main()
