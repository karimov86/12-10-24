from bs4 import BeautifulSoup
import requests
import tkinter as tk

# Find the rank
def get_rank(row):
    rank = row.find('span', class_='rank')
    rank_text = rank.text.strip() if rank else "N/A"
    return rank_text

# Find the title
def get_title(row):
    title_tag = row.find('span', class_='titleline').find('a')
    title = title_tag.text.strip() if title_tag else "No title"
    return title

# Find the link
def get_link(row):
    title_tag = row.find('span', class_='titleline').find('a')
    url = title_tag['href'] if title_tag else "No link"
    return url

# Find the corresponding score in the next <tr>
def get_score(row):
    next_row = row.find_next_sibling('tr')
    score_tag = next_row.find('span', class_='score') if next_row else None
    score = int(score_tag.text.split()[0]) if score_tag else 0
    return score

# Combine data in a dictionary
def combined_data(rows):
    data = []
    for row in rows:
        score = get_score(row)
        # Only take news with a score greater than or equal to 100
        if score >= 100:
            rank = get_rank(row)
            title = get_title(row)
            link = get_link(row)
            data.append({'rank':rank, 'title':title, 'score':score, 'link':link})
    return data

# Sort a dictionary from the highest score
def sort_data_by_score(data):
    sorted_data = sorted(data, key=lambda k:k['score'], reverse=True)
    return sorted_data

# Gets the url for the first page until max page for the next page button
def get_url_next_page():
    yield 'https://news.ycombinator.com/news'
    for page in range(2, 27):
        yield (f'https://news.ycombinator.com/news?p={page}')

def click_button(gen, text_widget):
    value = next(gen)
    text_widget.delete("1.0", tk.END)  # Clear the text widget
    text_widget.insert(tk.END, value)  # Insert the news

# Print only news with score higher than or equal to 100 sorted from high to low
def print_out(sorted_data):
    output = []
    for row in sorted_data:
        rank = row['rank']
        title = row['title']
        score = row['score']
        link = row['link']
        output.append(f'''Rank: {rank}
                      Title: {title}
                      Score: {score}
                      URL: {link}
{"-" * 40}''')
    return output

# Get response and define all data
def define_variables(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.find_all('tr', class_='athing')

    # Get the data
    data = combined_data(rows)
    sorted_data = sort_data_by_score(data)

    # Print out
    return "\n\n".join(print_out(sorted_data))

# Make define_variable() a generator
def gen(url_gen):
    for url in url_gen:
        yield define_variables(url)

def main():
    root = tk.Tk()
    root.title("Hacker News Copy")
    root.geometry("500x600")  # Set window size

    # Multiline Text widget
    text_widget = tk.Text(root, wrap="word", font=("Arial", 12), relief="solid", bd=6)
    text_widget.grid(row=0, column=0, columnspan=4, rowspan=5, sticky="nsew", padx=20, pady=20)

    # Create button and configure grid
    url_gen = get_url_next_page()  # Initialize URL generator
    button = tk.Button(root, text="More", font=("Arial", 16), command=lambda: click_button(gen(url_gen), text_widget))
    button.grid(row=0, column=4, rowspan=5, sticky="nsew")

    # Made window adjustable
    for i in range(5):  # 5 rows
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):  # 4 columns
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
        
if __name__ == '__main__':
    main()