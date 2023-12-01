class Usuario:
    def __init__(self,login:str,senha:str) -> None:
        self.login = login
        self.senha = senha
    
    def concluiu_cadastro(self):
        return f'O usuario {self.login}  foi cadastrado'
    
class Personagem:
    def __init__(self,nome:str,sexo:str,classe:str,magia:bool=False) -> None:
        self.nome = nome
        self.sexo = sexo
        self.classe = classe
        self.magia = magia

    def escolha_do_personagem(self):
        return  'personagem criado'


class Humano(Personagem):
    def __init__(self, nome: str, sexo: str, classe: str, magia:str,bibede:bool=True,inteligencia:bool= True,mortal:bool=True) -> None:
        super().__init__(nome, sexo, classe, magia)
        self.bibede = bibede
        self.inteligencia =inteligencia
        self.mortal = mortal
     
class Elfo(Personagem):
    def __init__(self,nome:str,sexo:str,classe:str,cargo:str,magia:bool= True,bibede:bool=True,inteligencia:bool= True,longevidade:bool=True,resistencia:bool=True) -> None:
        super().__init__(nome,sexo,classe,magia)
        self.cargo = cargo
        self.bibede = bibede
        self.inteligencia = inteligencia
        self.longevidade = longevidade
        self.resistencia = resistencia

# classes = [1,2,3,4,5,6,7,8,9,10]

# # classePersonagem = input("Digite a classe do seu personagem: ")
# # if classePersonagem in '[!@#$%¨&*()_+=§,<>.:;?°/\|ªº''" -]':
# #     print('Opção invalida')

# case = input("escolha um valor de 0 a 10").isnumeric()  
 

# if case == True:  
#     print ('O número digitado foi {}'.format(case))  
# elif case== False:  
#     print ('Digite apenas numeros!')