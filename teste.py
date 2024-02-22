from licenses import License

licenses = License(path_folder="licenses")

license = licenses.delete_license(license_key="4312412341")
license = licenses.check_license(license_key="4312412341")
print(license) # False

