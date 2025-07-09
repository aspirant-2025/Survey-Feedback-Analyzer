# Survey feedback Analyzer using Python Programming concepts.
To analyze and clean survey feedback data using core Python constructs such as lists, dictionaries, loops, string operations, and functions.
**Project Steps and Objectives:**
 📌 Project Objectives
- Store and manage feedback data in a dictionary of lists
- Allow dynamic addition of feedback via user input
- Clean text data to prepare it for analysis
- Count frequency of specific words across feedback entries
- Compute summary statistics and extract insights

# Step 1:Started program with a dictionary of lists, preloaded with 10 feedbacks:
 ```python
feedback_data = {
    'S_No': [...],
    'Name': [...],
    'Feedback': [...],
    'Rating': [...]
}


# Step 2: new feedbacks are added to the existing dictionary.
 -For each feedback, collected the following inputs from the user: 
○ Name 
○ Written Feedback (text) 
○ Rating (1–5)

 #Step 3: All feedback texts are cleaned; Lowercased, Stripped of punctuation (!, ., ,, ?) ,Normalized for extra spaces
 #Step 4:Created a function count_word_in_feedbacks(word) that: 
  - Takes a word as input. 
  - Returns how many feedbacks contained in  that word (case-insensitive match). 
  ### Used this function to print: 
      -Number of feedbacks containing "good" 
      - Number of feedbacks containing "poor" 
      - Number of feedbacks containing "excellent"
# Step 5: Summary and Insights
  - Displayed cleaned feedback data
  -Calculated average rating
  -Found feedback with the longest comment
  -Extracted all unique words used across feedbacks



