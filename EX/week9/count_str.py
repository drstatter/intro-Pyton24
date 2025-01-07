def count_k_in_list(data_list):
    number_of_words=0
    for word in data_list:
        if "K" in word:
            number_of_words+=1
    return number_of_words
def main():
    words=["Koala","k","1230","KKK","LKLKLK"]
    print(count_k_in_list(words))
if __name__ == '__main__':
    main()