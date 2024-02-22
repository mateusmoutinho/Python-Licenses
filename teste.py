from python_licenses import Licenses

licenses = Licenses(path_folder="licenses")

licenses.create_license(license_key="1234567890", expiration_date="2024-12-31")

license = licenses.check_license("1234567890")

print(license)