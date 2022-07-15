# The "re" Module

## Learning Goals

- Validate input using regular expressions.
- Search for patterns using regular expressions.

***

## Key Vocab

- **Regular Expression**: a sequence of characters used to search for a pattern
inside of a string.
- **Pattern**: a description of sequences of characters that share certain
traits with one another. Sequences do not need to be the same length or share
any common characters to pattern match. Also called a **filter**.

***

## Introduction

To start working with regular expressions in your IDE, you will first need to
import the `re` module from Python's standard library. Python's standard
library is a collection of modules that are downloaded when you install any
version of Python. These modules aren't keyword objects like `print()` or
`return`, but they can be imported without downloading them into your `pipenv`.

Open up your Python shell to get started:

```py
import re
text = "This is some regular text."
```

If we go to [regex101][regex101], we can try out some patterns to start
thinking about how to craft our regular expression. If we use the text itself,
we _do_ get a match- the `.` character matches anything. If we want to match
the period specifically, we should end our pattern with `\.`:

```py
import re
text = "This is some regular text."
pattern = r'This is some regular text\.'
```

Now let's dive into the `re` module to put this pattern to work.

## `re` Methods

The first thing that we need to do is turn our pattern over to the `re` module.
We'll use the `compile()` instance method:

```py
import re
text = "This is some regular text."
pattern = r'This is some regular text\.'
regex = re.compile(pattern)
```

> NOTE: You can use the `re` module without compiling your patterns beforehand.
> This is _not_ recommended because it will require you to include your pattern
> as an argument to every new `re` method that you run. Gross!

Let's use Python's `dir()` function to explore our `regex` object:

```py
dir(regex)
# => ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']
```

As with most Python objects, we can see that there are a lot of magic methods
in there- we're typically not meant to call those, so we'll skip ahead to the
standard instance methods. Let's start with `search()`.

### `search()`

The `search()` instance method of compiled `re` objects is exactly what it
sounds like- it searches to see if there is a match for your regular expression
in the text.

Let's take a look:

```py
import re
text = "I love text. Text text text text text."
pattern = r'text'
regex = re.compile(pattern)
match = regex.search(text)
print(match)
# => <re.Match object; span=(7, 11), match='text'>
```

The `search()` method returns an `re.Match` object. Let's use `dir()` once again
to learn more:

```py
dir(match)
# => [(ignoring magic methods...), 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']
```

An `re.Match` object contains an index for its start and end locations in the
string that your RegEx is being checked against. It also contains the original
string itself:

```py
match.start()
# => 7
match.end()
# => 11
match.span()
# => (7, 11)
match.string
# => 'I love text. Text text text text text.'
```

There is also a `match()` method that belongs to `re` objects. The `match()`
method searches to see if there is a match for your regular expression that
starts from the _beginning_ of the text, returning an `re.Match` object if
one is found.

If you're feeling _**very particular**_, the `fullmatch()` method checks the
text from beginning to end, returning an `re.Match` object if the whole thing
is a match.

The `search()`, `match()`, and `fullmatch()` methods are useful if you're just
checking to see if a match exists; if you're looking for the strings that match
your pattern, `findall()` is a better option.

### `findall()`

The `findall()` method is very straightforward (and therefore very useful).
Like `search()`, it searches to see if there are matches for your RegEx within
the text. `findall()` returns a list of matching strings instead of an
`re.Match` object.

```py
import re
text = 'The big red cat ate the fat rat.'
pattern = r'[A-z]{3}'
regex = re.compile(pattern)
regex.findall(text)
# => ['The', 'big', 'red', 'cat', 'ate', 'the', 'fat', 'rat']
```

As `findall()` finds and returns all strings that match your RegEx (and we
don't have to fuss around with `dir()` to find more information), it is the
`re` method that you will use the most frequently as a software engineer.

### `split()` and `sub()`

***

## Lesson Section

Lorem ipsum dolor sit amet. Ut velit fugit et porro voluptas quia sequi quo
libero autem qui similique placeat eum velit autem aut repellendus quia. Et
Quis magni ut fugit obcaecati in expedita fugiat est iste rerum qui ipsam
ducimus et quaerat maxime sit eaque minus. Est molestias voluptatem et nostrum
recusandae qui incidunt Quis 33 ipsum perferendis sed similique architecto.

```py
# python code block
print("statement")
# => statement
```

```js
// javascript code block
console.log("use these for comparisons between languages.")
// => use these for comparisons between languages.
```

```console
echo "bash/zshell statement"
# => bash/zshell statement
```

<details>
  <summary>
    <em>Check for understanding text goes here! <code>Code statements go here.</code></em>
  </summary>

  <h3>Answer.</h3>
  <p>Elaboration on answer.</p>
</details>
<br/>

***

## Conclusion

Conclusion summary paragraph. Include common misconceptions and what students
will be able to do moving forward.

***

## Resources

- [Resource 1](https://www.python.org/doc/essays/blurb/)
- [Reused Resource][reused resource]

[regex101]: https://regex101.com/
