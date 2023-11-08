# compiling a pattern
import re
text = "This is some regular text."
pattern = r'This is some regular text\.'
regex = re.compile(pattern)

# match()
import re
text = "I love text. Text text text text text."
pattern = r'text'
regex = re.compile(pattern)
match = regex.search(text)
print(match)

# findall()
import re
text = 'The big red cat ate the fat rat.'
pattern = r'[A-z]{3}'
regex = re.compile(pattern)
regex.findall(text)

# split()
story = "I went to the park and I saw my friend and my friend's dog was there and we ran around and there was another dog and the other dog didn't like my friend's dog but then they got used to each other and they ran to the creek and we ran to the creek too to keep them out of the water and they went in the water and then we went in the water and the water was cold and we got out of the water and Mrs. Smith got mad at us and we went back to the classroom and got hot chocolate and then we watched a movie and now we're going home."
and_pattern = re.compile(r'\sand')
and_pattern.split(story)