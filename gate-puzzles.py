import string


def find_word(message):
    for punctuation_item in string.punctuation:
        message = message.replace(punctuation_item, '')
    word_list = message.lower().split(" ")
    table = [[0 for j in range(len(word_list))] for i in range(len(word_list))]

    for i in range(len(word_list)):
        for j in range(len(word_list)):
            score = 0
            #self continue
            if i == j:
                table[i][j] = 0
                continue

            #first and end letters
            if word_list[i][0] == word_list[j][0]:
                score = score + 10
            if word_list[i][-1] == word_list[j][-1]:
                score = score + 10

            #compare len
            length_of_word1 = float(len(word_list[i]))
            length_of_word2 = float(len(word_list[j]))
            if length_of_word1 <= length_of_word2:
                score = score + (length_of_word1 / length_of_word2) * 30
            else:
                score = score + (length_of_word2 / length_of_word1) * 30

            #uniq letters
            set_word_1 = set(word_list[i])
            set_word_2 = set(word_list[j])
            common_letter_number = float(len(set_word_1 & set_word_2))
            unique_letters_numbers = float(len(set().union(set_word_1, set_word_2)))
            score = score + (common_letter_number / unique_letters_numbers) * 50

            table[i][j], table[j][i] = score, score

    sumall = [0]*len(table)
    for i in range(len(table)):
        for j in range(len(table)):
            sumall[j] = sumall[j] + table[i][j]
    m = max(sumall)
    maxi = [i for i, j in enumerate(sumall) if j == m]
    return word_list[maxi[-1]]


def test_function():
    assert find_word(u"Friend Fred and friend Ted.") == "friend", "Friend"
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
