import pandas as pd
import pyautogui
import time

# ==============================
# Configuration
# ==============================

LOGIN_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "example@email.com"
PASSWORD = "password123"

pyautogui.PAUSE = 0.5


# ==============================
# Browser Automation Functions
# ==============================

def open_browser():
    pyautogui.click(x=151, y=754)  # Adjust if necessary
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(6)


def navigate_to_login():
    pyautogui.write(LOGIN_URL)
    pyautogui.press("enter")
    time.sleep(7)


def login():
    pyautogui.click(x=648, y=368)  # Adjust if necessary
    pyautogui.write(EMAIL)
    pyautogui.press("tab")
    pyautogui.write(PASSWORD)
    pyautogui.press("enter")
    time.sleep(5)


# ==============================
# Product Registration
# ==============================

def load_products():
    return pd.read_csv("data/products_sample.csv")


def register_products(products_df):
    for index in products_df.index:
        pyautogui.click(x=589, y=257)  # Adjust if necessary

        fields = [
            "codigo",
            "marca",
            "tipo",
            "categoria",
            "preco_unitario",
            "custo",
            "obs"
        ]

        for field in fields:
            value = products_df.loc[index, field]

            if pd.notna(value):
                pyautogui.write(str(value))

            pyautogui.press("tab")

        pyautogui.press("enter")
        pyautogui.scroll(10000000)
        time.sleep(0.5)


# ==============================
# Main Execution
# ==============================

def main():
    open_browser()
    navigate_to_login()
    login()
    products = load_products()
    register_products(products)


if __name__ == "__main__":
    main()
