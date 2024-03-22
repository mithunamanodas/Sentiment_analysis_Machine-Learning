#import os

#folder_path = r'C:\other\latest\Imdb-Sentiment-Analysis-Flask'
#os.system(f'start {folder_path}')
string = "too good and super"
new_string = ""

for letter in string:
    if letter not in new_string:
        new_string += letter

print(new_string) # Output: "abcdefghi"
