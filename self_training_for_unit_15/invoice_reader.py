# Project 3: Invoice file loader with Error Message
# Idea: Open an invoice text file and show contents, if not fount , warm user

import os


def load_invoice(filename):
    try:
        with open(filename, "r") as f:
            print("Invoice Content: ")
            print(f.read())

    except FileNotFoundError:
        print(f'❌ File {filename} not found. Please check filename.')
    except Exception as e:
        print("❌ Unexpected error:", e)


# user input
file_to_load = input("Enter invoice file name: ")
load_invoice(file_to_load)
