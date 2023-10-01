import sys

if sys.argv[1] == "reverse":
    inputpath = sys.argv[2] 
    outputpath = sys.argv[3]
    with open(inputpath, 'r') as f:
        contents = f.read()
        contents_rev = ""
        for i in range(1, len(contents) + 1):
            contents_rev += contents[-i]
    with open(outputpath, 'w') as f:
            f.write(contents_rev)
elif sys.argv[1] == "copy":
    inputpath = sys.argv[2] 
    outputpath = sys.argv[3]
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(outputpath,'w') as f:
        f.write(contents)
elif sys.argv[1] == "duplicate-contents":
    inputpath = sys.argv[2]
    n = sys.argv[3]
    n = int(n)
    with open(inputpath,'r+') as f:
        contents = f.read()
        for i in range(n-1):
            f.write("\n" + contents)
elif sys.argv[1] == "replace-string":
    inputpath = sys.argv[2]
    with open(inputpath, 'r+') as f:
        contents = f.read()
        print(len(contents))
        contents = contents.replace("needle", "newstring")
        f.write(contents)

