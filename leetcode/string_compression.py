class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        left = 0
        while left < len(chars):
            char = chars[left]
            count = 0
            while left < len(chars) and char == chars[left]:
                left += 1
                count += 1
            chars[writer] = char
            writer += 1
            if count > 1:
                for c in str(count):
                    chars[writer] = c
                    writer += 1
        return writer
