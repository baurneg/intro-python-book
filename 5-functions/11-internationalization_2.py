# Building on your solutions from the previous exercises, write a function 
# local_greet that takes a locale as input, and returns a greeting. 
# The locale lets us greet people from different countries appropriately, 
# even when they share a common language, for example:

# Copy Code
# print(local_greet('en_US.UTF-8'))       # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!
# Distinguish greetings for English speaking countries like the US, UK, 
# Canada, or Australia in your implementation, and feel free to fall back 
# on the language-specific greetings in all other cases, for example:

# Copy Code
# print(local_greet('fr_FR.UTF-8'))       # Salut!
# print(local_greet('fr_CA.UTF-8'))       # Salut!
# print(local_greet('fr_MA.UTF-8'))       # Salut!
# When implementing local_greet, make sure you re-use your extract_language, 
# extract_region, and greet functions from the previous exercises.

# If you're interested, you can find a list of locales here.
def local_greet(local_abb):
  language = extract_language(local_abb)
  if language == 'en' and extract_region(local_abb) == 'US':
    return 'Hey!'
  elif language == 'en' and extract_region(local_abb) == 'GB':
    return 'Hello!'
  elif language == 'en' and extract_region(local_abb) == 'AU':
    return 'Howdy!'
  else:
    return greet(language)

def greet(lang):
    match lang:
        case 'en':
            return 'Hi!'
        case 'fr':
            return ('Salut!')
        case 'pt':
            return ('Ola!')
        case 'de':
            return ('Hallo!')
        case 'sv':
            return ('Hej!')
        case 'af':
            return ('Haai!')
def extract_language(lang_code):
  index = lang_code.find('_')
  return lang_code[:index]
  
def extract_region(locale):
  lang = locale.split('_')
  region = lang[1].split('.')
  return region[0]

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!