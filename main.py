from tkinter import *
import weather_logic


def search_weather():
    city = city_entry.get()

    if not city:
        result_label.config(
            text="Please enter a city name.",
            fg="red"
        )
        return

    try:
        weather = weather_logic.get_weather(city)

        result_label.config(
            text=(
                f"Temperature: {weather['temp']}°C\n"
                f"Weather: {weather['desc']}\n"
                f"Humidity: {weather['humidity']}%"
            ),
            fg="green"
        )
        
    except Exception as e:
        result_label.config(
            text=f"Error: {e}",
            fg="red"
        )


window = Tk()
window.title("Weather App")
window.geometry("400x300")
#window color
window.configure(bg="lightblue")

title_label = Label(
    text="Weather App",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=10)

city_entry = Entry(width=30, bg="lightyellow")
city_entry.pack(pady=10)

search_button = Button(
    text="Search",
    command=search_weather,
    bg="White"
)
search_button.pack(pady=10)

result_label = Label(
    text="Enter a city.",
    font=("Arial", 12),
    wraplength=350,
    justify="left",
    bg="lightblue"
)
result_label.pack(pady=20)

window.mainloop()