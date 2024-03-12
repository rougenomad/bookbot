def main():
    book_path = "books/Frankenstien.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = chars_sorted_list(chars_dict)
    
    #Prints the meat and potatos of books
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char in sorted_list:
        
        print(f"The {char["char"]} character was found {char["num"]} times")
    print("--- End report ---")

def get_book_text(book_path): #Pulls the book Frankenstein but from the Berenstien universe
        with open(book_path) as f:
            return f.read()
        
def get_num_words(text):
        #Basic word count; Simple but you can count on it
        wordcount = text.split()
        return len(wordcount)
 
         
def get_chars_dict(text):
        #Ok here we get fancy (lower your standards); We lower the case and count unique letters
        unique_count = {}
        for letter in text:
              lowered_stien = letter.lower()
              if lowered_stien.isalpha():
                if lowered_stien in unique_count:
                    unique_count[lowered_stien] += 1
                else:
                    unique_count[lowered_stien] = 1
        return unique_count

def sort_on(d):
    #Sets key for sorting dict
    return d["num"]

def chars_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()