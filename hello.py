def hello_world():
    file = open("/home/chanchal/gui/dummy_file.txt","w+")
    print("dummy file prepared")
    file.close()

if __name__ == "__main__":
    hello_world()