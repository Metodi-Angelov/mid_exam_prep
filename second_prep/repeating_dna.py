def get_repeating_DNA(text):
    result = []
    for i in range(len(text) - 10):
        current = text[i: i + 10]
        if current in text[i+1:] and current not in result:
            result.append(current)
    return result


test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)