from src.sped_narrative import SPEDNarrative
from src.emotional_feedback import analyze_emotion
from src.quantum_forking import quantum_fork_decision
from src.blockchain_logger import log_interaction

def run_sped():
    story = SPEDNarrative("The world shimmers, uncertain of your intent.")
    
    print("\nWelcome to SPED - Schrödinger's Path: Emergent Design\n")
    while True:
        user_input = input("\nYour thoughts (or type 'exit'): ")
        if user_input.lower() == "exit":
            break

        emotion = analyze_emotion(user_input)
        branch = quantum_fork_decision()
        narrative = story.adapt_narrative(emotion)

        print("\n>>", narrative)
        print(f"(Emotion: {emotion}, Branch: {branch})")

        try:
            log_interaction(f"{emotion}:{branch}")
        except Exception as e:
            print(f"[Blockchain log failed: {e}]")

if __name__ == "__main__":
    run_sped()
