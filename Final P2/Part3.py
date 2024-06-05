from abc import ABC,abstractmethod
class DocumentFactory(ABC):
    def __init__(self,filename,filesize,content):
        self.filename=filename
        self.filesize=filesize
        self.content=content
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def save(self):
        pass
class Document(DocumentFactory):
    def __init__(self,filename,filesize,content):
        super().__init__(filename,filesize,content)
    def open(self):
        print(f"Opening a Document {self.filename} with the content {self.content}")
    def read(self):
        print(f"Reading the document file {self.filename} of size {self.filesize}")
    def save(self):
        print(f"Saving the document file {self.filename}")
class Pdf(DocumentFactory):
    def __init__(self,filename,filesize,content):
        super().__init__(filename,filesize,content)
    def open(self):
        print(f"Opening a pdf {self.filename} with the content {self.content}")
    def read(self):
        print(f"Reading the pdf file {self.filename} of file size {self.filesize}")
    def save(self):
        print(f"Saving the pdf file {self.filename}")
class Excel(DocumentFactory):
    def __init__(self,filename,filesize,content):
        super().__init__(filename,filesize,content)
    def open(self):
        print(f"Opening a pdf {self.filename} with content {self.content}")
    def read(self):
        print(f"Reading the pdf file {self.filename} of size {self.filesize}")
    def save(self):
        print(f"Saving the pdf file {self.filename}")
e1=Excel('Expenses','434Kb',"number")
e1.open()
e1.read()
e1.save()
d1=Document("CV",'234kb','text')
d1.open()
d1.read()
d1.save()
p1=Pdf('Calculus','3.2 MBs','Text')
p1.open()
p1.read()
p1.save()