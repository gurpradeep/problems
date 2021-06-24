class File:
    def __init__(self):
        self.is_file = False
        self.content = ""
        self.files = dict()

class FileSystem:

    def __init__(self):
        self.root = File()

    def ls(self, path):
        t = self.root
        files = []
        if path != "/":
            d = path.split("/")
            for i in d[1:]:
                t = t.files[i]
            if t.is_file:
                files.append(d[len(d) - 1])
                return files
        res_files = list(t.files.keys())
        return sorted(res_files)

    def mkdir(self, path):
        t = self.root
        d = path.split("/")
        for i in d[1:]:
            if i not in t.files:
                t.files[i] = File()
            t = t.files[i]
            
    def add_content_to_file(self, filePath, content):
        t = self.root
        d = filePath.split("/")
        for i in d[1:len(d) - 1]:
            t = t.files[i]
        
        if d[len(d) - 1] not in t.files:
            t.files[d[len(d) - 1]] = File()
        t = t.files[d[len(d) - 1]]
        t.is_file = True
        t.content = t.content + content

    def read_content_from_file(self, filePath):
        t = self.root
        d = filePath.split("/")
        for i in d[1:len(d) - 1]:
            t = t.files.get(i)
        return t.files[d[len(d) - 1]].content


## Driver Code
fs = FileSystem()
print(fs.ls("/"))
fs.mkdir("/dir1/dir2/dir3")
fs.mkdir("/dir4/dir2/dir3")
print(fs.ls("/"))
fs.add_content_to_file("/dir1/dir2/dir3/file1", "File")
print(fs.read_content_from_file("/dir1/dir2/dir3/file1"))
fs.add_content_to_file("/dir1/dir2/dir3/file1", " System")      
print(fs.read_content_from_file("/dir1/dir2/dir3/file1"))
