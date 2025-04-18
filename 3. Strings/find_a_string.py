def count_substring(string, sub_string):
    rep = [i for i in range(len(string)) if string.startswith(sub_string,i)]
    count = len(rep)
    return count