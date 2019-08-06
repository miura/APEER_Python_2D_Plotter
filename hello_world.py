from shutil import copyfile

def execute(input):
    file_name = "hello_world.txt"
    copyfile(input, file_name)
    f = open(file_name, "w")
    f.write("Hello, World!")
    f.close()

    return {'Output': file_name}