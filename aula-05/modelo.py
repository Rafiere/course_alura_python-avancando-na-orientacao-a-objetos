# Se queremos que uma classe seja usada como um iterável, podemos implementar os métodos
# dessa classe, porém, sem criar um contrato.

# Por exemplo, para uma classe ser um iterável e poder ser usada no laço "for in", por exemplo, ela
# pode implementar o método "__getitem__", tendo todas as vantagens de um iterável.

# O duck typing consiste em não herdarmos métodos de uma classe, mas nos parecermos com uma
# classe, ou seja, termos os mesmos comportamentos dela.

# No Java, as interfaces garantem que todo mundo que implementar uma interface vai ser
# obrigado a implementar todos os métodos abstratos dessa interface.

# No Python, para uma subclasse ser obrigada a implementar uma lista de métodos, temos
# as classes "ABC", que são as "abstract base classes", assim, podemos usar várias
# baseclass que estão prontas, como as que estão no "collections.abc"
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

# Essa classe está herdando a classe ABC "MutableSequence", assim, ela deverá implementar os
# métodos dessa classe.
filmes = Playlist()