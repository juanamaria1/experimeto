from filtrado_datos import DATA

def run():
    # ///////// hig order funtions ////////// nombre de quienes manejan paython
    # nombre = list(filter(lambda idioma: idioma["language"]=="python",DATA))
    # lenguaje = list(map(lambda nose: nose["name"],nombre))
    # for cosa in lenguaje:
    #     print(cosa)

    # ///////////hig order funtions////////// nombre d equienes trabajan en platzi
    # lista = list(filter(lambda workers:workers["organization"]=="Platzi",DATA))
    # nombre = list(map(lambda work: work["name"],lista))
    # for names in nombre:
    #     print(names)

    # /////// list comprehension /////////
    # ages = [i["name"] for i in DATA if i["age"]>=31]
    # for comprobar in ages:
    #     print(comprobar)

    pass

if __name__=="__main__":
    run()
