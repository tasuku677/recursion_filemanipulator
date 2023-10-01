import sys
import markdown
import pathlib
import shutil
if sys.argv[1] == "markdown":
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    with open(input_file,'r', encoding="utf-8") as f:
        contents = f.read()         
    output_html = pathlib.PurePath(output_file).stem + ".html"
    with open(output_html,'w') as f:
        f.write(markdown.markdown(contents))