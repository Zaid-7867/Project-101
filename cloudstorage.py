import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFile(self,source,destination):
        dbx=dropbox.Dropbox(self.accessToken)
        f = open(source,"rb")
        dbx.files_upload(f.read(),destination)

def main():
    accessToken='sl.BoLabCNmq788Ipb18uzmQgh-YuCO6s-g1aFbUF5afnspWMpgw2KA5jAO55JIihoJEE9hT81qlP7UfExoXQs-Ma69hyZcAox4xxtLo6fg7Z7SPYjCpHZ83ev-WCaE-tpd3H12xDOl5pNV'
    object = TransferData(accessToken)
    source="C:/Users/zaid_/Desktop/Zaid/Python/Class 101/test.txt"
    destination="C:/Users/zaid_/Dropbox/Test"
    object.uploadFile(source,destination)
    print("The file has been moved")

main()
    
