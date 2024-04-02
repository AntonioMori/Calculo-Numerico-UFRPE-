# Atividade para calcular o zero da linguagem pythom em um computador - Aluno Antonio Umberto Camargo Mori
# O código se baseia na ideia de

a = 1 # definimos uma variável a iniciando ao valor 1
s = 2 # definimos uma variável s com o valor 2 inialmente

while s > 1 :   # enquanto o valor de "S" for maior que o valor 1
    a = a/2     # ele irá atribuir "a" por sua metade, e isto acontece quantas vezes for até o valor de "a" ser tão baixo que ele aproxime o valor de zero
    s = 1+a     # o valor de "s" é atribuido a 1+a o que significa que quando o "a" for infinitamente pequeno ao ponto da máquina não conseguir mais guardar ele de tão pequeno é,
                # ele irá ser igual 1+ um valor tão pequeno de "a" , que então satisfaz a condição de parada do while s > 1 == false

print(a)
print(2*a) # como é que o a = um valor extremamente baixo que satisfez 1+a = 1 e terminou o while porém se fizermos 2*a = um valor viável? tipo não era para ele fazer 2*0 = 0
print("ele satisfez o (s = 1+a) = 1 e terminou o loop do while porque o while(s>1) resultou em false, porém quando fazemos 2*a ele resulta em algo diferente de zero, curioso")


b = 1
while (b > 0):
    if (b/2 == 0):
        print("O ultimo valor de b antes de ser arredondado para zero é : ", b)
        print("o atual valor de b é : ", b/2)
    b = b/2




