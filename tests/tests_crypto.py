import unittest
from packages.encryption import crypto

class TestCryptoPackage(unittest.TestCase):
    def setUp(self):
        self.key = b"test_key"
        self.message = "Hello, Secure World!"

    def test_aes_encryption(self):
        enc = crypto("encrypt", self.message, self.key, "AES")
        dec = crypto("decrypt", enc, self.key, "AES")
        self.assertEqual(dec, self.message)

    def test_sha256_hashing(self):
        hashed = crypto("hash", self.message, None, "SHA-256")
        self.assertEqual(len(hashed), 64)

if __name__ == "__main__":
    unittest.main()
