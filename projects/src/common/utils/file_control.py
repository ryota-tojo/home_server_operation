import time

def get_file_to_target_row(file_path, keyword):
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                if keyword in line:
                    found_line = line
                    break
            else:
                time.sleep(0.5)
    return found_line