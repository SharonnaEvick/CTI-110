#Sharonna Evick
#07/12/2025
# P4HW1_EvickSharonna.py
#Calculate scores
# -----------------------------------------------
# Pseudocode:
# 1.Ask user to enter for number of scores they would like to enter
# 2. Create a loop to collect the number of scores the user wants to enter
# 3. Evaluate if the score is valid, it should be between 0 and 100 
#     a. If it is not, notify the user and ask for a VALID score to be entered
#     b. Add valid score to the list
# 4. If score is valid, add the score to a list. Make sure the score list is given an informative name
# 5. Score List after dropping lowest score
# 6. The average of scores in modified list
# 7. Determine the letter grade based on average
# 8. Display the lowest score, modified list, average, and letter grade
# -----------------------------------------------

# Step 1: Ask how many scores
num_scores = int(input("How many scores would you like to enter? "))

# Step 2: Create an empty list
scores = []

# Step 3: Collect and validate scores
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        if 0 <= score <= 100:
            scores.append(score)  # <-- FIXED: use 'scores' not 'score_list'
            break
        else:
            print("Invalid score. Please enter a value between 0 and 100.")

# Step 4: Analyze the scores
lowest_score = min(scores)
scores.remove(lowest_score)

# Step 5: Calculate average
average_score = sum(scores) / len(scores)

# Step 6: Determine letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Step 7: Display results
print("\n------------- Results -------------")
print("Lowest score  :", lowest_score)
print("Modified list :", scores)
print("Average score :", round(average_score, 2))
print("Letter grade  :", grade)
