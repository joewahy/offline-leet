### Approach

Put the length of each string in front of it, followed by a `#`: `["ab", "c"]` becomes `2#ab1#c`. To decode, read digits up to the next `#` to learn the length, then take exactly that many characters.

Because the length is read first, the content itself can contain `#`, digits or anything else without confusing the decoder. That is why a plain separator character does not work.

### Complexity

- Time: O(total characters) for both encode and decode.
- Space: O(total characters) for the encoded string and the result.

### Watch out

`s.index("#", i)` searches from the current position, so it stops at the length prefix's own `#` and never at one inside a string.
