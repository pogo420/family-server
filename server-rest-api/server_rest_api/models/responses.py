# Rest response definition 

class AppInfo:
    __app_name: str
    __app_version: str

    def __init__(self, __app_name: str, __app_version: str):
        self.__app_name = __app_name
        self.__app_version = __app_version

    def app_name(self) -> str:
        return self.__app_name
    
    def app_version(self) -> str:
        return self.__app_version
    
    def __dict__(self):
        return {"app name": self.__app_name, "app version": self.__app_version}
