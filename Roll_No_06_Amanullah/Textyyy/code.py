def read_input_file():
    max_attempts = 3
    attempt = 0

    while attempt < max_attempts:
        file_name = input("📂 Please enter the file name: ")
        if '.' not in file_name:
            print("📝 Looks like you didnt include a file extension. Please make sure its a '.txt' file.")
            attempt += 1
            continue
        elif not file_name.lower().endswith('.txt'):
            print(f"❌ Sir! This program only works with '.txt' files. You entered something else.")
            attempt += 1
            continue

        try:
            with open(file_name, "r") as file_handler:
                full_text = ""
                for line in file_handler:
                    for char in line:
                        full_text += char
            return full_text  
        except FileNotFoundError:
            print(f"❌ Oops! Sir! The file '{file_name}' was not found. Please check the name and try again!")
        except PermissionError:
            print(f"🚫 Sorry Sir!, you don't have permission to open '{file_name}'. Try a different file or check access rights.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")
        
        attempt += 1
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Try again. You have {remaining} {'attempt' if remaining == 1 else 'attempts'} left.\n")
        else:
            print("😞 Sorry, no more attempts left. Please restart the program when you're ready.")

    return None

def count_words(text):
    inside_word = False
    word_count = 0
    for char in text:
        if char not in (' ', '\n', '\t'):
            if not inside_word:
                word_count += 1
                inside_word = True
        else:
            inside_word = False
    return word_count


def count_characters(text):
    char_count = 0
    for char in text:
        char_count += 1
    return char_count


def count_spaces(text):
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
    return space_count


def count_commas(text):
    comma_count = 0
    for char in text:
        if char == ',':
            comma_count += 1
    return comma_count


def count_periods(text):
    period_count = 0
    for char in text:
        if char == '.':
            period_count += 1
    return period_count


def count_sentences(text):
    sentence_count = 0
    for char in text:
        if char in ('.', '?', '!'):
            sentence_count += 1
    return sentence_count


def count_vowels(text):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def count_digits(text):
    digit_count = 0
    for char in text:
        if '0' <= char <= '9':
            digit_count += 1
    return digit_count


def count_uppercase(text):
    uppercase_count = 0
    for char in text:
        if 'A' <= char <= 'Z':
            uppercase_count += 1
    return uppercase_count


def count_lowercase(text):
    lowercase_count = 0
    for char in text:
        if 'a' <= char <= 'z':
            lowercase_count += 1
    return lowercase_count


def count_special_characters(text):
    special_char_count = 0
    unique_special_chars = set()
    for char in text:
        if not (('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9') or char in (' ', '\n', '\t')):
            special_char_count += 1
            unique_special_chars.add(char)
    return special_char_count, sorted(unique_special_chars)

def main():
    textyyy = read_input_file()
    if textyyy is None:
        return 

    word_count = count_words(textyyy)
    total_characters = count_characters(textyyy)
    spaces = count_spaces(textyyy)
    commas = count_commas(textyyy)
    periods = count_periods(textyyy)
    sentences = count_sentences(textyyy)
    vowels = count_vowels(textyyy)
    digits = count_digits(textyyy)
    uppercase_letters = count_uppercase(textyyy)
    lowercase_letters = count_lowercase(textyyy)
    special_chars_total, unique_special_chars_sorted = count_special_characters(textyyy)

    report = f"""
Hey! Here's a friendly analysis of your file's contents:

- WORDS: Sir! You wrote {word_count} words.
- CHARACTERS: There are {total_characters} characters in total, including spaces and punctuation.
- SPACES: Sir! You used {spaces} spaces for word separation.
- COMMAS: Found {commas} commas, nice use of pauses!
- PERIODS: There are {periods} periods ending sentences.
- SENTENCES: Counting sentences ending with '.', '!', or '?', you have {sentences} total.
- VOWELS: Your text has {vowels} vowels, quite melodically vowellyy!
- DIGITS: Spotted {digits} digits.
- UPPERCASE LETTERS: {uppercase_letters} uppercase letters.
- LOWERCASE LETTERS: {lowercase_letters} lowercase leters.
- SPECIAL CHARACTERS: Total special characters count is {special_chars_total}.

  Special characters used: {', '.join(unique_special_chars_sorted) if unique_special_chars_sorted else 'None found!'}

Thanks for using my code, hope this gives u breif oversight of txt file u were lookin for!
"""

    with open("output.txt", "w") as output_file:
        output_file.write(report.strip())

main()
