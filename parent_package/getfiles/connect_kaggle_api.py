import os


from kaggle import api





class kaggle_auth:
    def __init__(self):
        pass

    def authenticate_key():
        api.authenticate()

    def download(self,path,name):
        self.path = path
        self.name = name
        if not os.path.exists(self.path):
            os.makedirs(self.path,exist_ok=True)
            print(f"Sucessfully created {self.path} directory")
            api.competition_download_files(self.name,path = self.path,quiet=False)

    def list_files(self, name):
        self.name = name


        file_list = api.competitions_list(search=self.name)

        return file_list





