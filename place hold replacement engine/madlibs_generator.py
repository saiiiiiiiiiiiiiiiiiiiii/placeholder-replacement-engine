

with open("story.txt") as file:
    story = file.read()

words = set()
start_of_word = -1
opening_angle_bracket = "<"
closing_angle_bracket = ">"
for i, char in enumerate(story):
    if char == opening_angle_bracket:
        start_of_word = i

    if char == closing_angle_bracket and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])  # Reassign to update the story

print(story)
