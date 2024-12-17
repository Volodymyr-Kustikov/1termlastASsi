import pandas as pd
import matplotlib.pyplot as plt

def open_file(path):
    return pd.read_csv(path)

def show_table(file, name, bins):
    plt.figure(figsize=(8, 4))
    plt.hist(file[["imdb_score"]].dropna(), bins=bins, alpha=0.8, edgecolor='black')
    plt.title(f'Гістограма для {name}')
    plt.xlabel("imdb_score")  
    plt.ylabel('Кількість')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def show_bar_plot(bar_plot):
    bar_plot.plot(kind='bar', color='skyblue', edgecolor='black')

    plt.title('Середній рейтинг по роках', fontsize=14)
    plt.xlabel('Рік випуску', fontsize=12)
    plt.ylabel('Середній рейтинг IMDB', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Поворот подписей на оси X для читаемости
    plt.grid(axis='y', alpha=0.75)

    plt.tight_layout()
    plt.show()
file_path = './data/titles.csv'
all_file = open_file(file_path)
all_file = all_file

missing_imdb_scores = all_file['imdb_score'].isnull().sum()


movies_data = all_file[all_file['type'] == 'MOVIE']
show_data = all_file[all_file['type'] == 'SHOW']
bins = int((movies_data['imdb_score'].max() - movies_data['imdb_score'].min()) // 0.2) + 1


film = all_file[['type']]
# show_table(movies_data, "movies_data", bins)

# show_table(show_data, "show_data", bins)

movies_data_new = movies_data[movies_data["release_year"] >= 2000]
show_data_new = show_data[show_data["release_year"] >= 2000]

movies_data_new = movies_data_new[movies_data_new["imdb_score"] > 8.0]
show_data_new = show_data_new[show_data_new["imdb_score"] > 8.0]
movies_ratings_per_year = movies_data_new.groupby('release_year')['imdb_score'].mean().round(1)
show_ratings_per_year = show_data_new.groupby('release_year')['imdb_score'].mean().round(1)



show_bar_plot(show_ratings_per_year)
show_bar_plot(movies_ratings_per_year)
print(f"Best film year since '00s is {movies_ratings_per_year.idxmax()}")
print(f"Best show year since '00s is {show_ratings_per_year.idxmax()}")