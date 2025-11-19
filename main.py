import flet as ft
import random

# Beginner-level Guess the Number Game using Flet

def main(page: ft.Page):
    page.title = "Guess the Number Game"
    target_number = random.randint(1, 100)
    attempts = 0

    info = ft.Text(value="Guess a number between 1 and 100")
    input_field = ft.TextField(label="Your Guess", width=200)

    def check_guess(e):
        nonlocal attempts
        guess = input_field.value
        try:
            guess = int(guess)
        except ValueError:
            info.value = "Please enter a valid number!"
            page.update()
            return

        attempts += 1

        if guess < target_number:
            info.value = f"Try higher! Attempts: {attempts}"
        elif guess > target_number:
            info.value = f"Try lower! Attempts: {attempts}"
        else:
            info.value = f"Correct! You guessed it in {attempts} attempts."

        input_field.value = ""
        page.update()

    submit_btn = ft.ElevatedButton("Submit", on_click=check_guess)

    page.add(
        info,
        input_field,
        submit_btn
    )

ft.app(target=main)