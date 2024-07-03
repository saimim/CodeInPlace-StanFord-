def main():
    words = load_words_from_file("words.txt")
    print_histogram_bar(words)

def print_histogram_bar(word):

    talk = {}
    for i in range(len(word)):
        m_word = word[i]
        if m_word not in talk:
            talk[m_word] = 1
        else:
            talk[m_word] += 1
    for key,value in talk.items():
        print(str(key)+":"+"x"*value)

def load_words_from_file(filepath):
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()
