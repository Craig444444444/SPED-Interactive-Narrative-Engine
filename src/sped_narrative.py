class SPEDNarrative:
    def __init__(self, intro):
        self.story = intro
        self.history = [intro]

    def adapt_narrative(self, emotion):
        if emotion == "happy":
            self.story += " A strange joy dances in the air."
        elif emotion == "sad":
            self.story += " A soft drizzle echoes your inner quiet."
        elif emotion == "angry":
            self.story += " Thunder cracks where none should be."
        else:
            self.story += " Time halts, awaiting your true feeling."

        self.history.append(self.story)
        return self.story
