import os

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400
NEWLINECHAR = "<N>"

full_paths = []
for dirpath, _, filenames in os.walk("repos"):
    for f in filenames:
        full_paths.append(os.path.join(dirpath, f))

print(f"Total files found: {len(full_paths)}")

with open("python_code_text_data.txt", "a", encoding="utf-8") as f:
    for fpath in full_paths:
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as file:
                d = file.read()

            print(f"File length: {len(d)}")

            fd = d.replace("\n", NEWLINECHAR)

            if 100 < len(d) <= MAX_CHAR_LENGTH:
                f.write(fd + "\n")
            else:
                print("Splitting content into chunks...")
                words = fd.split() 
                substring = ""

                for word in words:
                    if len(substring) + len(word) + len(NEWLINECHAR) > MAX_CHAR_LENGTH:

                        if len(substring) >= MIN_CHAR_LENGTH:
                            f.write(substring + "\n")
                            substring = ""  

                    substring += word + " "  


                if len(substring) >= MIN_CHAR_LENGTH:
                    f.write(substring + "\n")

        except Exception as e:
            print(str(e))

 
