import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_review():
    name = name_entry.get()
    movie_title = movie_title_entry.get()
    genre = genre_combobox.get()
    review = review_entry.get("1.0", tk.END).strip()
    rating = rating_slider.get()
    emotions = emotions_combobox.get()
    recommend = recommend_var.get()

    if not name or not movie_title or not genre or not review or not emotions or not recommend:
        messagebox.showwarning("Помилка", "Будь ласка, заповніть всі поля.")
        return

    review_info = [name, movie_title, genre, review, rating, emotions, recommend]
    reviews_info.append(review_info)

    if rating >= 8:
        messagebox.showinfo("Успіх", "Ваш відгук успішно збережено!")
    else:
        messagebox.showinfo("Відгук збережено", "Ваш відгук збережено!")

    name_entry.delete(0, tk.END)
    movie_title_entry.delete(0, tk.END)
    genre_combobox.set('')
    review_entry.delete("1.0", tk.END)
    rating_slider.set(1)
    emotions_combobox.set('')
    recommend_var.set(None)

    root.after(4000, root.destroy)

reviews_info = []

root = tk.Tk()
root.title("Збір відгуків на фільми")

tk.Label(root, text="Ім'я:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Назва фільму:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
movie_title_entry = tk.Entry(root, width=30)
movie_title_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Жанр фільму:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
genre_combobox = ttk.Combobox(root, values=["Комедія", "Драма", "Бойовик", "Трилер", "Фантастика", "Жахи"])
genre_combobox.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Короткий відгук:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
review_entry = tk.Text(root, width=40, height=5)
review_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Рейтинг (1-10):").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
rating_slider = tk.Scale(root, from_=1, to_=10, orient=tk.HORIZONTAL)
rating_slider.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Емоції після перегляду:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
emotions_combobox = ttk.Combobox(root, values=["Щастя", "Смуток", "Страх", "Гнів", "Здивування", "Нейтральність"])
emotions_combobox.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Рекомендуєте фільм іншим?").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
recommend_var = tk.StringVar(value=None)
tk.Radiobutton(root, text="Так", variable=recommend_var, value="Так").grid(row=6, column=1, sticky=tk.W, padx=10, pady=5)
tk.Radiobutton(root, text="Ні", variable=recommend_var, value="Ні").grid(row=6, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Надіслати", command=submit_review)
submit_button.grid(row=7, column=1, padx=10, pady=10, sticky=tk.E)

root.mainloop()
