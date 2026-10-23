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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A separator like `,` fails as soon as a string contains it. What information could you store instead of relying on a separator?
2. Write each string's length, then a marker, then the string itself. When decoding, the length tells you exactly how many characters to take.
3. Read digits up to the marker `#` to get the length `n`, take the next `n` characters (even if they include `#` or digits), then continue after them. An empty string is just `0#`.

</details>
