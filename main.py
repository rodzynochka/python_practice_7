from app.io.input import read_text_from_console, read_file_builtin, read_file_with_pandas
from app.io.output import print_text_to_console, write_text_to_file_builtin, write_dataframe_to_csv


def main():
    console_text = read_text_from_console()
    builtin_text = read_file_builtin('data/sample.txt')
    pandas_df = read_file_with_pandas('data/sample.csv')

    print_text_to_console("\nYour input")
    print_text_to_console(console_text)

    print_text_to_console("\nRead the file using open()")
    if builtin_text:
        print_text_to_console(builtin_text)

    print_text_to_console("\nRead with pandas")
    if pandas_df is not None:
        print_text_to_console(pandas_df.to_string(index=False))

    # --- Запис до файлу (built-in) ---
    write_text_to_file_builtin('data/output.txt',
        f"[Console Input]\n{console_text}\n\n[From File (builtin)]\n{builtin_text}\n")

    # --- Запис DataFrame до CSV ---
    if pandas_df is not None:
        write_dataframe_to_csv('data/output_from_pandas.csv', pandas_df)

if __name__ == "__main__":
    main()