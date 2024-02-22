from python_licenses import Licenses

licenses = Licenses(root_secret="siasdiaijaijdsa")

v = licenses.create_license(license_key="1234567890", expiration_date="2024-12-31")

print(f"store these:\n{v}")

result = licenses.check_license(v)
print(result)