import random

num_questions = 10
num_correct = 0

for i in range(num_questions):
  # Generate two random numbers between 1 and 12
  num1 = random.randint(1, 12)
  num2 = random.randint(1, 12)

  # Ask the player to solve the multiplication problem
  answer = int(input(f"Question {i + 1}: {num1} x {num2} = "))

  # Check if the answer is correct
  if answer == num1 * num2:
    print("Right!")
    num_correct += 1
  else:
    print(f"Wrong. The answer is {num1 * num2}.")

# Print out the final score
print(f"You got {num_correct} out of {num_questions} questions correct.")
