import pandas as pd

def read_text_from_console():
    return input("Input your text: ")


def read_file_builtin(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"oops, there was an error: {e}")


def read_file_with_pandas(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except pd.errors.ParserError:
        print("Error while reading the CSV file.")
    except Exception as e:
        print(f"oops, there was an error with pandas: {e}")