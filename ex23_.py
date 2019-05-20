from sys import argv

script, ip_encodings, ip_errors = argv

def print_line(line, encoding, error):
        line = line.strip()
        raw_bytes = line.encode(encoding, error)
        cooked_string = raw_bytes.decode(encoding, error)
        print(raw_bytes, " <==========================> ", cooked_string)
        languagesOut.write(str(raw_bytes)+"\n")

if __name__ == "__main__":
        languages = open('languages.txt', encoding = "utf-8")
        languagesOut = open('languagesOut.txt', 'w', encoding = "utf-8")
        for iterline in languages.readlines(): 
                if iterline:
                        print_line(iterline, ip_encodings, ip_errors)
        languagesOut.close()







