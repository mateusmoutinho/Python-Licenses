# Python-Licenses
A python library that help you to handle software licenses

## Installation
```bash
pip install python_licenses==0.0.1
```

## Usage
```python
from python_licenses import Licenses

licenses = Licenses(root_secret="siasdiaijaijdsa")

v = licenses.create_license(license_key="1234567890", expiration_date="2024-12-31")

print(f"store these:\n{v}")

result = licenses.check_license(v)
print(result)
```
## How to use
Python Licenses is a library that helps you to handle software licenses. It's possible to create, update and delete licenses.

#### Example Create License
```python
from licenses import Licenses

licenses = Licenses(path_folder="licenses")

licenses.create_license(license_key="4312412341", expiration_date="2024-12-31")
```


#### Example Verify License
```python
from licenses import Licenses

licenses = Licenses(path_folder="licenses")

license = licenses.check_license(license_key="4312412341")

print(license) # True
```


