import hashlib

class Codec:
    def __init__(self):
        self.tiny_to_long = {}
        self.long_to_tiny = {}
        self.prefix = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.long_to_tiny:
            return self.long_to_tiny[longUrl]

        hash_value = hashlib.sha1(bytes(longUrl, 'utf-8')).hexdigest()
        new_url = self.prefix + hash_value
        
        self.long_to_tiny[longUrl] = new_url
        self.tiny_to_long[new_url] = longUrl

        return new_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.tiny_to_long:
            return self.tiny_to_long[shortUrl]
        return ''
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))