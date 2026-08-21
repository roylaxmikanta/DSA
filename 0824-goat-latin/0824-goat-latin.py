class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr=sentence.split(" ")
        vowel=('A','a','E','e','I','i','O','o','U','u')
        for i in range(len(arr)):
            if arr[i][0] in vowel:
                arr[i]=arr[i]+'ma'+'a'*(i+1)
            else:
                e=arr[i][0]
                arr[i]=arr[i][1:]+e
                arr[i]=arr[i]+'ma'+'a'*(i+1)
        return " ".join(arr)
