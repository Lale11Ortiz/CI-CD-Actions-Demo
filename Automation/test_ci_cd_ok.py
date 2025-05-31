# Prueba flake8 limpio
import unittest

class BasicCICDTest(unittest.TestCase):
    def test_ci_cd_pipeline(self):
        print("✅ GitHub Actions funciona correctamente con unittest.")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()