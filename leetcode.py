
def isPalindrome(self, x: int) -> bool:
    myFor = str(x)
    myBack = str(x)
    myBack = myBack[::-1]
    if (myFor == myBack):
        return True
    else:
        return False


