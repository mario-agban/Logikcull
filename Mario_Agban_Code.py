#Import a couple of libraries
import pandas as pd
import csv
import operator


#TASK_1
#Read the csv file by pandas to create a dataframe
pd.set_option('display.max_rows', None)
data = pd.read_csv(r'C:\Users\felfe\Desktop\code-challenge\movies.csv')
df = pd.DataFrame(data, columns= ['movieId','title', 'genres'])


#Task_2
#For loop that iterates and checks how many genres are there in each movie
genre_count = []
count = df['genres'].str.count(r'\|')
for i in range(len(df['genres'])):
    #take into account that 'no genres listed' is not a genre
    if df['genres'].str.contains(r'no genres listed')[i]:
        genre_count.append(count[i])
    else:
        genre_count.append(count[i]+1)


#Task_3
#Inserted a new column 'genre_count' into the dataframe from the list genre_count
df['genre_count'] = genre_count


#BONUS_Task_1
#Average number of genres:
total = 0
for i in range(len(genre_count)):
    total += genre_count[i]
print(total/len(genre_count))

#Average number of genres per movie:
genre_count_average = []
for i in range(len(genre_count)):
    genre_count_average.append(genre_count[i]/len(genre_count))
print(genre_count_average)



#BONUS_Task_2
#Created a dictionary with keys as genres and values as the count of it being mentioned.
seperated_genres = df['genres'].str.split(r'\|')
all_the_genres = []
for row in seperated_genres:
    for gen in row:
            all_the_genres.append(gen)
dic_of_genres = {i: all_the_genres.count(i) for i in all_the_genres}
#sorted in desceding order and taken the first element. Key is 'Drama' and value is 4361.
sorted_dic_of_genres = sorted(dic_of_genres.items(), key=operator.itemgetter(1), reverse = True)
print(sorted_dic_of_genres[0])
  