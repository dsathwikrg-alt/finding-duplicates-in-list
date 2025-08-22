import ast
from typing import Any, List



def find_duplicate(input_list: List[Any]) -> List[Any]:

    input_list_size = len(input_list)
    duplicates_list: List[Any] = []

    for i in range(0, input_list_size):
        for j in range(0, input_list_size):
            if i!=j:
                # counter=0
                if input_list[i] == input_list[j]:
                    # counter += 1
                    # if duplicates_list.__contains__(input_list[i]):
                    if input_list[i] in duplicates_list:
                        print(f"Already {input_list[i]} is present in the duplicates list")
                        continue
                    else:
                        duplicates_list.append(input_list[i])
    
    return duplicates_list

def find_duplicate_set(input_list: List[Any]) -> List[Any]:

    seen = set()
    duplicates: List[Any] = []

    for x in input_list:
        if x not in seen:
            seen.add(x)
        elif x not in duplicates:
            duplicates.append(x)

    return duplicates            


def main():

    user_input = input("Enter the List items :")

    input_list = ast.literal_eval(user_input)

    duplicates = find_duplicate(input_list)

    duplicates_set = find_duplicate_set(input_list)

    print(f"Duplicates in the list are: {duplicates}")

    print(f"Duplicates in the list are: {duplicates_set}")


if __name__ == '__main__':
    main()


        


