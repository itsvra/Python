import glob, os
os.chdir("C:\\allure")
for file in glob.glob("*.txt"):
    print(file)
