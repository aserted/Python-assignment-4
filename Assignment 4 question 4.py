# We know that if the candy is divided evenly among 5 people, 2 pieces are left over.
# This means that the number of candy is 2 more than a multiple of 5.
# We also know that if the candy is divided evenly among 6 people, 3 pieces are left over.
# This means that the number of candy is 3 more than a multiple of 6.
# We also know that if the candy is divided evenly among 7 people, 2 pieces are left over.
# This means that the number of candy is 2 more than a multiple of 7.
# So, we can check all the numbers that are 2 more than a multiple of 5, 6, and 7
# to find the number of candy.

for num_candy in range(2, 200):
  if num_candy % 5 == 2 and num_candy % 6 == 3 and num_candy % 7 == 2:
    print(f"The number of candy is: {num_candy}.")
    break
