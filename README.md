# Levenshtein distance
This is a repo with different implementations of levenshtein distance algorithm (currently just recursive one is here, but ill get back to this eventually)

## What is Levenshtein distance

Its a string metric for measuring 'distance' between two text sequences (strings). It calculates minimum number of single-character *edits* required to change one word (string) to another.
What are allowed *edits*?
1. insertion 
2. delition, and
3. substitution

Other versions of this problems (strings distance) have different constrains on what edits are.

The distance between two strings *a* and *b* is given by  ![distance](/images/distance.svg) where ![function](/images/levenshtein.svg) 

In the 'otherwise' part, last segment of min function, 1 is the *indicator* function equal to 0 if a[i]==b[j] and 1 otherwise (I used brackets notation but you would use subscript for that..). Also, by |*a*| we denote the legnt of the string *a*.

On the internet, there are many 'versions' (read notations of this algorithm) and in this one, when you see ![notation](/images/notation.svg) you should think of it as levenshtein distance betweeb string prefixes (or substrings..), specifically first *i* characters of string *a*, and first *j* characters of string *b*.

I'll use zero-based indexing for strings.

The algorithms (currently just one :( ) are implemented following greate guide from https://www.baeldung.com/cs/levenshtein-distance-computation .

