class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_dict = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4};
        idx_dict = {(0, 0, 0, 0, 0): -1};
        answer = 0;

        vowel_parity = [0, 0, 0, 0, 0];
        for i, c in enumerate(s):
            if c in vowel_dict: vowel_parity[vowel_dict[c]] ^= 1;

            vow_tuple = tuple(vowel_parity);
            if vow_tuple in idx_dict:
                answer = max(answer, i - idx_dict[vow_tuple]);

            else: idx_dict[vow_tuple] = i;

        return answer;
