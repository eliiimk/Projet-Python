class Quest:
    def __init__(self, name, description, reward_xp):
        self.name = name
        self.description = description
        self.reward_xp = reward_xp
        self.is_completed = False

    def complete(self):
        self.is_completed = True
        return self.reward_xp
