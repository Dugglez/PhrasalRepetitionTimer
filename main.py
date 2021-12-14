import random
import os
import time


def main():
    sentences = []
    want_to_play = True
    with open("sentences.txt", "r") as file:
        for line in file:
            sentences.append(line)
    print("Welcome to the Phrasal Repetition Timer.")
    print("A few sentences will appear and your job will be to type them out as fast as possible.")
    print("Statistics will be provided after completing the sentences.")
    print("Be sure to type out the sentence exactly as it appears and press enter only when you are finished.")
    while want_to_play:
        print("Please select the number of sentences you would like to write (1 - 4).")
        sentence_count = input("")
        while sentence_count not in ["1", "2", "3", "4"]:
            print("Please select the number of sentences you would like to write (1 - 4).")
            sentence_count = input("")
        print("After pressing enter, your sentence will appear and the timer will start. Press enter when you are ready.")
        input("")
        sentences_int = int(sentence_count)
        sentence_to_write = ""
        for i in range(sentences_int):
            rand_sentence = random.choice(sentences)
            sentence_to_write += rand_sentence
            sentence_to_write += " "
        os.system("cls")
        start = time.time()
        print(sentence_to_write)
        response = input("")
        finish = time.time()
        words = response.split(" ")
        word_count = 0
        for i in words:
            word_count += 1
        time_taken = 60/(finish-start)
        WPM = word_count * time_taken
        if response == sentence_to_write:
            print(f"You completed the sentences with no errors! This took you {round((finish - start),2)} seconds. "
                  f"You typed {word_count} words, meaning you had an average WPM of {round(WPM,2)}.")
            choice = input("Press enter to exit or P to play again.")
            while choice not in ["", "P", "p"]:
                print("Press enter to exit or P to play again.")
                choice = input("")
            if choice == "":
                break
            if choice == "P" or choice == "p":
                pass
        else:
            response_split = list(response)
            sentence_to_write_split = list(sentence_to_write)
            count = 0
            while len(response_split) < len(sentence_to_write_split):
                response_split.append("")
            sentence_to_write_split.pop()
            sentence_to_write_split.pop()
            for i in range(len(sentence_to_write_split)):
                if response_split[i] != sentence_to_write_split[i]:
                    print(f"Letter number {i}: Sample: {sentence_to_write_split[i]}, Response: {response_split[i]}.")
                    count += 1
            print(f"You completed the sentences with {count} errors. This took you {round((finish - start),2)} seconds. "
                  f"You typed {word_count} words, meaning you had an average WPM of {round(WPM,2)}.")
            choice = input("Press enter to exit or P to play again.")
            while choice not in ["", "P", "p"]:
                print("Press enter to exit or P to play again.")
                choice = input("")
            if choice == "":
                break
            if choice == "P" or choice == "p":
                pass


if __name__ == '__main__':
    main()
