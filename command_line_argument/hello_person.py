import argparse

def greeting(name, lang):
    salutes={
        "English": "Hello",
        "Spanish": "Holla",
        "German": "Hallo",
    }
    msg = f"{salutes[lang]} {name}!"
    print(msg)

parser = argparse.ArgumentParser(
    description="Greets the person."
)

parser.add_argument(
    "-n", "--name", metavar="name", required=True, help="Enter your name using -n."
)

parser.add_argument(
    "-l", "--lang", metavar="language", required=True, choices=["English","Spanish","German"], help="Enter your the language using -l."
)

args = parser.parse_args()

greeting(args.name,args.lang)