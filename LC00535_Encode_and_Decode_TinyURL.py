# LC00535_Encode_and_Decode_TinyURL.py

# Note: This is a companion problem to the System Design problem: Design TinyURL.
# https://leetcode.com/discuss/post/124658/design-url-shortening-service-like-tinyu-047o/
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
# and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL 
# can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Implement the Solution class:

# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. 
# It is guaranteed that the given shortUrl was encoded by the same object.
 

# Example 1:

# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"

# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding it.
 

# Constraints:

# 1 <= url.length <= 10**4
# url is guranteed to be a valid URL.

# Idea: change the first long url to "1", change the second url to "2"

class Codec:
    def __init__(self):
        self.long_urls=[]
        self.count_total=0
        self.dict_long_url_to_short={}


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.dict_long_url_to_short:
            ind_str=self.dict_long_url_to_short[longUrl]
            return ind_str
        else:
            self.dict_long_url_to_short[longUrl]=str(self.count_total)
            self.long_urls.append(longUrl)
            self.count_total+=1
            return str(self.count_total-1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.long_urls[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

