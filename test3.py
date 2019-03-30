class Language:
    default_language = "English"
  
    def __init__(self):
        self.show = '나의 언어는' + self.default_language
  
    @classmethod
    def class_my_language(cls):
        return cls()
  
    @staticmethod
    def static_my_language():
        return Language()
  
    def print_language(self):
        print(self.show)
    
a = Language()

print(Language.default_language)
print(a.class_my_language)
print(a.static_my_language)