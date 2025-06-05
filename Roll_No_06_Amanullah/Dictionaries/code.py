# Hey Sir, this script checks out a text file and counts stuff like words, chars, spaces, commas, periods, sentences, vowels, digits, uppercase, lowercase, and special chars.
# Just drop your input file in the same folder as this script, output will also save right here as "output.txt". 📂
# I added a bunch of error handling to cover most probs, but if something’s off, Sir, just hit me up and I’ll fix it!


# just needed if u tryna pretty print the disctionary, otherwise no need to import json
import json

def read_input_file():
    max_attempts = 3
    attempt = 0

    while attempt < max_attempts:
        file_name = input("📂 Please enter the file name ( gotta be .txt, and gotta be in same folder/dir): ")
        if "." not in file_name:
            print(
                "📝 Looks like you forgot the file extension. Make sure it's a '.txt' file."
            )
            attempt += 1
            continue
        elif not file_name.lower().endswith(".txt"):
            print(
                f"❌ Sir, this program only works with '.txt' files. You entered something else."
            )
            attempt += 1
            continue

        try:
            with open(file_name, "r") as file_handler:
                full_text = ""
                for line in file_handler:
                    for char in line:
                        full_text += char
            print(f"✅ ok so, the file '{file_name}' was successfully opened!")
            return full_text
        except FileNotFoundError:
            print(
                f"❌ Oops! Sir, the file '{file_name}' wasn't found. Double-check the name and try again!"
            )
        except PermissionError:
            print(
                f"🚫 Sorry Sir, you dont have permission to open '{file_name}'. Maybe try another file or check your access?"
            )
        except Exception as e:
            print(f"⚠️ Whoa, something unexpected happened: {e}")

        attempt += 1
        remaining = max_attempts - attempt
        if remaining > 0:
            print(
                f"Give it another shot. Youve got {remaining} 'tries' left.\n"
            )
        else:
            print(
                "😞 No more tries left. Tbh, just give a correct file man! Just restart the program when you're ready."
            )

    return None


def count_words(text):
    inside_word = False
    word_count = 0
    current_word = ""
    word_list = []

    for char in text:
        if char not in (" ", "\n", "\t"):
            if not inside_word:
                word_count += 1
                inside_word = True
            current_word += char
        else:
            if inside_word:
                word_list.append(current_word)
                current_word = ""
            inside_word = False
    if current_word != "":
        word_list.append(current_word)

    return word_count, word_list


def count_characters(text):
    char_count = 0
    char_list = []
    for char in text:
        char_count += 1
        char_list.append(char)
    return char_count, char_list


def count_spaces(text):
    space_count = 0
    for char in text:
        if char == " ":
            space_count += 1
    return space_count


def count_commas(text):
    coumma_count = 0
    for char in text:
        if char == ",":
            coumma_count += 1
    return coumma_count


def count_periods(text):
    period_count = 0
    for char in text:
        if char == ".":
            period_count += 1
    return period_count


def count_sentences(text):
    sentence_count = 0
    sentence_list = []
    for char in text:
        if char in (".", "?", "!"):
            sentence_count += 1
            sentence_list.append(char)
    return sentence_count, sentence_list


def count_vowels(text):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    vowel_list = []
    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
    return vowel_count, vowel_list


def count_digits(text):
    digit_count = 0
    digit_list = []
    for char in text:
        if "0" <= char <= "9":
            digit_count += 1
            digit_list.append(char)
    return digit_count, digit_list


def count_uppercase(text):
    uppercase_count = 0
    uppercase_list = []
    for char in text:
        if "A" <= char <= "Z":
            uppercase_count += 1
            uppercase_list.append(char)
    return uppercase_count, uppercase_list


def count_lowercase(text):
    lowercase_count = 0
    lowercase_list = []
    for char in text:
        if "a" <= char <= "z":
            lowercase_count += 1
            lowercase_list.append(char)
    return lowercase_count, lowercase_list


def count_special_characters(text):
    special_char_count = 0
    unique_special_chars = set()
    special_char_list = []
    for char in text:
        if not (
            ("A" <= char <= "Z")
            or ("a" <= char <= "z")
            or ("0" <= char <= "9")
            or char in (" ", "\n", "\t")
        ):
            special_char_count += 1
            unique_special_chars.add(char)
            special_char_list.append(char)
    return special_char_count, sorted(unique_special_chars), special_char_list


def main():
    textyyy = read_input_file()
    if textyyy is None:
        return

    main_Output = {}
    details_Of_instances = {}

    word_count, word_list = count_words(textyyy)
    main_Output["func1"] = {"words_count": word_count}
    details_Of_instances["func1"] = {"all_words_found": word_list}

    total_characters, all_chars = count_characters(textyyy)
    main_Output["func2"] = {"characters_count": total_characters}
    details_Of_instances["func2"] = {"all_characters": all_chars}

    space_count = count_spaces(textyyy)
    main_Output["func3"] = {"spaces_count": space_count}
    details_Of_instances["func3"] = {}

    coumma_count = count_commas(textyyy)
    main_Output["func4"] = {"coummas_count": coumma_count}
    details_Of_instances["func4"] = {}

    perid_count = count_periods(textyyy)
    main_Output["func5"] = {"periods_count": perid_count}
    details_Of_instances["func5"] = {}

    sentence_count, sentence_list = count_sentences(textyyy)
    main_Output["func6"] = {"sentences_count": sentence_count}
    details_Of_instances["func6"] = {"sentence_endings": sentence_list}

    vowel_count, vowel_list = count_vowels(textyyy)
    main_Output["func7"] = {"vowels_count": vowel_count}
    details_Of_instances["func7"] = {"vowels_found": vowel_list}

    digit_count, digit_list = count_digits(textyyy)
    main_Output["func8"] = {"digits_count": digit_count}
    details_Of_instances["func8"] = {"digits_found": digit_list}

    uppercase_count, uppercase_list = count_uppercase(textyyy)
    main_Output["func9"] = {"uppercase_letters_count": uppercase_count}
    details_Of_instances["func9"] = {"uppercase_letters": uppercase_list}

    lowercase_count, lowercase_list = count_lowercase(textyyy)
    main_Output["func10"] = {"lowercase_letters_count": lowercase_count}
    details_Of_instances["func10"] = {"lowercase_letters": lowercase_list}

    special_chars_total, unique_special_chars_sorted, special_char_list = (
        count_special_characters(textyyy)
    )
    main_Output["func11"] = {"special_characters_count": special_chars_total}
    details_Of_instances["func11"] = {
        "unique_special_characters_sorted": unique_special_chars_sorted,
        "all_special_characters": special_char_list,
    }

    result = {"main_Output": main_Output, "details_Of_instances": details_Of_instances}

    with open("output.txt", "w") as output_file:
        # output_file.write(str(result))
        # Sir, We can ave the result as a JSON formatted string for easier readability, or use the above line (Uncomment above line if needed ) to write as un-formatted dictionary
        json.dump(result, output_file, indent=4)
        print("✅ Analysis complete! Results saved to 'output.txt'.")


main()
