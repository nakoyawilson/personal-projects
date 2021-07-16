import turtle
import pandas

screen = turtle.Screen()
screen.title("The Caribbean Region Game")
image = "blank_caribbean.gif"
screen.addshape(image)
turtle.shape(image)
answer = turtle.Turtle()
answer.penup()
answer.hideturtle()

data = pandas.read_csv("caribbean_countries.csv")
country_list = data.country.to_list()
number_of_countries = len(country_list)

game_is_on = True
correct_guesses = []
score = 0
while game_is_on:
    answer_country = screen.textinput(title=f"{score}/{number_of_countries} Countries Correct",
                                      prompt="Name a country:").title()
    if answer_country == "Exit":
        to_learn = [country for country in country_list if country not in correct_guesses]
        new_data = pandas.DataFrame(to_learn, columns=["country"])
        new_data.to_csv("countries_to_learn.csv")
        break
    if answer_country in country_list:
        if answer_country in correct_guesses:
            pass
        else:
            country = data[data.country == answer_country]
            answer.goto(int(country.x), int(country.y))
            answer.write(f"{answer_country}", font=("Arial", 10, "normal"))
            correct_guesses.append(answer_country)
    score = len(correct_guesses)
    if score == number_of_countries:
        answer.goto(-320, 250)
        answer.write("Congratulations! You named all the countries in the Caribbean Region.",
                     font=("Arial", 20, "normal"))
        game_is_on = False

screen.exitonclick()

# # Get cooridinates of countries
# # Source code from: https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
