import pprint

#step 1
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!! ',
        'poor support,   not happy   ',
        'GREAT experience! will come again.',
        'okay   okay...',
        ' not   BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

#step 2
count = int(input("how many feedbacks you like to add: "))
srl_no = 11

while count>0:
    name = input("enter name: ")
    feedback = input("enter feedback: ")
    rating = int(input("enter rating(1-5): "))

    feedback_data['S_No'].append(srl_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

    srl_no = srl_no+1
    count = count - 1



#step 3

source_list = feedback_data["Feedback"]
cleaned_list = []

for feedback in source_list:
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")

    temp_list = feedback.split(' ')
    temp_list = [i for i in temp_list if i!='']
    feedback = ' '.join(temp_list)

    feedback = feedback.strip()
    feedback = feedback.lower()

    cleaned_list.append(feedback)

feedback_data["Feedback"] = cleaned_list


#step 4

def count_word_in_feedbacks(word):
    feedback_list = feedback_data["Feedback"]
    count = 0
    for feedback in feedback_list:
        if word in feedback:
            count = count+1

    return count

print(count_word_in_feedbacks('good'))
print(count_word_in_feedbacks('poor'))
print(count_word_in_feedbacks('excellent'))

#step 5

print('Cleaned data: ')
pprint.pprint(feedback_data)

ratings_list = feedback_data['Rating']
average_rating = sum(ratings_list)/len(ratings_list)
print('Average rating : ', average_rating)

feedback_list = feedback_data["Feedback"]
max_word_count = 0
longest_feedback = ""
for feedback in feedback_list:
    word_count = len(feedback.split(' '))
    if word_count > max_word_count:
        longest_feedback = feedback
        max_word_count = word_count
        
print("Longest feedback: ", longest_feedback)

words_set = set()
for feedback in feedback_list:
    words_list = feedback.split(' ')
    for word in words_list:
        words_set.add(word)

print('List of unique words: ', words_set)







    




        
    




    

    
    
                 
 


