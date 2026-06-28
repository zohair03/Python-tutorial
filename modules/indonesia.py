from random import choice

capital = "Jakarta"
animal = "Komodo Dragan"

def random_facts():
    facts = ["fact1", "fact2", "fact3"]
    fact_chose = choice(facts)
    print(fact_chose)

if __name__ == "__main__":
    random_facts()