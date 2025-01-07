def count_string_with_k(word_list):
    total=0
    for word in word_list:
        if "K" in word:
            total+=1  # increment the count if "k" is found in the word
    return total
def main():
    words=["hi","koala","K","!@KKK#@"]
    print(count_string_with_k(words))
if __name__ == '__main__':
    main()