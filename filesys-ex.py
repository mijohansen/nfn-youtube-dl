import tempfile

temp_dir = tempfile.TemporaryDirectory()
print(temp_dir.name)
# use temp_dir, and when done:
#temp_dir.cleanup()
