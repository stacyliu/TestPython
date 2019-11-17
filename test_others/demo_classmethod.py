class Utils:


    @classmethod
    def getPackageName(cls):
        return "com.youku.phone"
    def getpid(self):
        return "1234567"


class DoRun:
    def run(self):
        print(Utils.getPackageName())
        print(Utils.getpid())

dorun=DoRun()
dorun.run()