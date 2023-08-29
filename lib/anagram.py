# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):

        return [word for word in words if sorted(word.lower()) == sorted(
            self.word.lower()) and word.lower() != self.word.lower()]


listen = Anagram("angel")
print(listen.match(["enlist", "google", "glean"]))