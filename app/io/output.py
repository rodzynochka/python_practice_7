def print_text_to_console(text):
    """Function to print text to the console"""
    print(text)


def write_text_to_file_builtin(file_path, text):
    """Function to write text to a file using Python's built-in tools"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Failed to write to file: {e}")


def write_dataframe_to_csv(file_path, dataframe):
    """Function to write a DataFrame to a CSV file using pandas"""
    try:
        dataframe.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Failed to write DataFrame to CSV: {e}")