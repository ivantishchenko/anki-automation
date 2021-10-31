#!/usr/bin/env python3

import argparse

def peek_next_block(f):
    pos = f.tell()
    line1 = f.readline()
    line2 = f.readline()
    f.seek(pos)
    return line1, line2

def main():
    parser = argparse.ArgumentParser(description='Parse a list of words from TTDictionary DE-RU')
    parser.add_argument('-w', type=str, required=True, help='File with a list of words')


    args = parser.parse_args()
    file_name = args.w

    words_map = {}
    with open(file_name, mode='r') as words_file:
        # Read key
        word = words_file.readline().rstrip()
        while word:
            print(word)
            # Skip dashes
            words_file.readline()
            
            # Build content
            content = []
            curr_line, next_line = peek_next_block(words_file)
            cursor = words_file.readline()
            while next_line and next_line.rstrip() != '----------':
                content.append(cursor)
                cursor = words_file.readline()
                curr_line, next_line = peek_next_block(words_file)
            
            content_string = ''.join(content).rstrip()
            print(content_string)
            print("")

            # Add to map
            words_map[word] = content_string

            # Read key
            word = words_file.readline().rstrip()
            print("........................................")

    print("Parsed {} words".format(len(words_map)))

    # 

    # for k, _ in words_map.items():
    #     print(k)

if __name__ == '__main__':
    main()