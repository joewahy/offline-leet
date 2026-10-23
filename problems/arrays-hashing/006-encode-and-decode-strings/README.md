# 6. Encode and Decode Strings (Medium)

Design an algorithm that turns a list of strings into one single string (`encode`), and turns that string back into the original list (`decode`).

The two methods are called on separate `Solution` objects, so nothing may be remembered between them: everything needed to rebuild the list must be inside the encoded string. Strings can contain any characters, including digits, `#`, and separators you might be tempted to use. Do not use built-in serialization helpers.

## Examples

```
Input:  ["neet", "code", "love", "you"]
decode(encode(...)) must return ["neet", "code", "love", "you"]

Input:  ["we", "say", ":", "yes"]
decode(encode(...)) must return ["we", "say", ":", "yes"]
```

## Constraints

- `0 <= len(strs) <= 100`
- `0 <= len(strs[i]) <= 200`
- Strings may contain any ASCII character, and may be empty.

## Hints

- A separator character is not safe, because a string might contain it.
- What if each string is stored together with its own length?
