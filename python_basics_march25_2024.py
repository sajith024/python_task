class PythonBasics25:

    # check if characters in string is unique
    def unique_characters(self, input_string):
        flag = True

        # check if each character is present in string
        for i in range(len(input_string)):
            for j in range(len(input_string)):
                if input_string[i] == input_string[j] and i != j:
                    flag = False
                    break

        return flag

    # check if two string is anagram of each other
    def check_anagram(self, input_a, input_b):

        # sort both string and check if equal
        if sorted(input_a) == sorted(input_b):
            return True
        else:
            return False

    # check if string is palindrome
    def check_palindrome(self, input_string):
        check_string = ""

        # include only alphabet, number and convert to lowercase
        for s in input_string:
            if s.isalnum():
                check_string += s.lower()

        for i in range(int(len(check_string) / 2)):
            if check_string[i] != check_string[len(check_string) - i - 1]:
                return False
        return True

    # find missing number in a list
    def missing_number(self, number_list):
        number_list = sorted(number_list)
        result = []

        # loop until the max item in list,
        # while appending if it is not present
        for n in range(1, max(number_list) + 1):
            if n not in number_list:
                result.append(n)

        return result

    def common_element(self, list_a, list_b):
        result = []

        # append common and non-duplicate element
        for i in list_a:
            for j in list_b:
                if i == j and i not in result:
                    result.append(i)

        return result

    def counting_occurence(self, occurence_list):
        result = {}

        # add new value and set occurence as 1
        # if value exist, +1 occurence
        for key, value in occurence_list:
            if result.get(key):
                inner_value = result.get(key).get(value)
                if inner_value:
                    result[key][value] = inner_value + 1
                else:
                    result[key][value] = 1
            else:
                result[key] = {value: 1}
        return result

    # convert roman numerals to integer
    def roman_to_integer(self, input_roman):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        last = "I"

        # calculated from right to left
        for numeral in input_roman[::-1]:
            if roman[numeral] < roman[last]:
                result -= roman[numeral]
            else:
                result += roman[numeral]
            last = numeral

        return result


basics = PythonBasics25()
print(basics.unique_characters("Unique"))
print(basics.check_anagram("hello", "world"))
print(basics.check_palindrome("A man, a plan, a canal, Panama!"))
print(basics.missing_number([3, 7, 1, 2, 2, 8, 4, 6]))
print(basics.common_element([1, 2, 3, 3, 4, 5], [3, 4, 5, 6, 7]))
print(basics.counting_occurence([(1, "a"), (2, "b"), (1, "c"), (2, "a"), (3, "b")]))
print(basics.roman_to_integer("LVIII"))
