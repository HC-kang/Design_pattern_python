from abc import ABCMeta, abstractmethod

# Product 인터페이스
class Section(metaclass = ABCMeta):
    
    @abstractmethod
    def describe(self):
        pass

# ConcreteProduct
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")
    
class PatentSection(Section):
    def describe(self):
        print("Patent Section")
        
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")
        
# Creator 추상 클래스
class Profile(metaclass = ABCMeta): 
    def __init__(self):
        self.sections = []
        self.createProfile()
        
    @abstractmethod
    def createProfile(self):
        pass
    
    def getSections(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)
        
# ConcreteCreator
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())
        
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
        
if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile...", type(profile).__name__)
    print("Profile has sections --", profile.getSections())