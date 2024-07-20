# Similar to the previous exercise, write a function that 
# extracts the region code from a locale. For example:

# Copy Code
# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

def extract_region(locale):
  lang = locale.split('_')
  region = lang[1].split('.')
  return region[0]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR