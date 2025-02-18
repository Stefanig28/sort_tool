import sys
import random
from io import StringIO
from pathlib import Path


def main(content: str, file: StringIO = sys.stdout, unique: bool = False, random_sort: bool = False) -> list[str]:
    lines = content.splitlines()

    if unique:
        sorted(set(lines))    
    if random_sort:
        random.shuffle(lines)
    else:
        sorted(lines)

    for line in lines:
        file.write(line  + "\n")
        file.flush()


def _cli():
    import argparse
    from signal import signal, SIGPIPE, SIG_DFL   
    signal(SIGPIPE,SIG_DFL) 

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=Path)
    parser.add_argument("-u", "--unique", action="store_true", default=False)
    parser.add_argument("-R", "--random_sort", action="store_true", default=False)
    args = parser.parse_args()

    content = args.filepath.read_text(encoding="utf-8")
    main(content, unique=args.unique, random_sort=args.random_sort)
    

if __name__ == "__main__":
    _cli()