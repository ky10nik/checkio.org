from itertools import groupby
def is_stressful(subj):
    """
        recoognise stressful subject
    """
    return (subj[-1]==subj[-2]==subj[-3]=="!")or all(c.isupper() or not(c.isalpha()) for c in subj) or any(word in "".join(c for c, _ in groupby(subj.lower()) if c.isalpha()) for word in ["help", "asap", "urgent"])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
