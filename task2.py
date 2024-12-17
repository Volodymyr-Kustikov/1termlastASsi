import pandas as pd
import matplotlib.pyplot as plt

data_titles = pd.read_csv("titles.csv", on_bad_lines='skip')

if 'age_certification' in data_titles.columns:
  counter = age_certification_counts = data_titles['age_certification'].dropna().value_counts()

  plt.figure(figsize=(7,7))
  counter.plot.pie(autopct='%1.1f%%', startangle=140, cmap='viridis')
  plt.title('pie-chart вікових рейтингів серед усіх шоу доступних та платформі ')
  plt.ylabel('')
else: print("Error by reading column data_titles")
plt.show()

import pandas as pd

data_credits = pd.read_csv("credits.csv", on_bad_lines='skip')

if 'imdb_score' in data_titles.columns:
    data_titles = data_titles.dropna(subset=['imdb_score'])
    data_titles['imdb_score'] = pd.to_numeric(data_titles['imdb_score'], errors='coerce')
    data_titles = data_titles.dropna(subset=['imdb_score'])
    thousand_films = data_titles.sort_values(by='imdb_score', ascending=False).iloc[:1000]
else:
    print("Error: 'imdb_score' column not found in data_titles")
    exit()


merged_data = pd.merge(thousand_films, data_credits, on='id')
actors_count = merged_data['name'].value_counts()
ten_actors = actors_count.iloc[:10]
print(ten_actors)

if 'genres' in thousand_films.columns:
    genre_list = thousand_films['genres']
    genre_counts = genre_list.value_counts()

    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind='bar', color='red')
    plt.title('Genre Distribution of Top 1000 Films and Shows')
    plt.xlabel('Genres')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Error: 'genres' column not found in thousand_films")