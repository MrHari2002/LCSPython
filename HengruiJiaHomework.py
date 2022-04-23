#Hengrui Jia


string1 = "cgtcgttatccgtcactggttgagatcgagtaagcaagacg"
string2 = "caaccatcgagtttgacgataagccgcaccagcgcgacat"


def lcs(string_x, string_y):
    len_x = len(string_x)
    len_y = len(string_y)

    two_dimensional_array = [[""]*(len_y+1) for i in range(len_x+1)]

    for j in range(len_y + 1):
        for i in range(len_x + 1):
            # The Zero Spot
            if i == 0 or j == 0:
                two_dimensional_array[i][j] = ""
            # If string_x does not match with string_y
            elif string_x[i - 1] != string_y[j - 1]:
                if len(two_dimensional_array[i - 1][j]) > len(two_dimensional_array[i][j - 1]):
                    two_dimensional_array[i][j] = two_dimensional_array[i - 1][j]
                else:
                    two_dimensional_array[i][j] = two_dimensional_array[i][j - 1]
            else:
                two_dimensional_array[i][j] = two_dimensional_array[i - 1][j - 1] + string_x[i - 1]

    return two_dimensional_array[len_x][len_y]


print(lcs(string1, string2))
