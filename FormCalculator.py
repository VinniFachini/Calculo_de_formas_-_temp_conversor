import math
import os

print(f'''
+----------------------------+
| 1 - Áreas;                 |
| 2 - Volumes;               |
| 0 - Encerrar programa;     |
+----------------------------+
''')
opt_primary = int(input('Digite a opção: '))

if opt_primary == 1:
    print(f'''
+----------------------------+
| 1 - Quadrado;              |
| 2 - Retângulo;             |
| 3 - Triângulo;             |
| 4 - Triângulo Equilátero;  |
| 5 - Trapézio;              |
| 6 - Polígono regular;      |
| 7 - Círculo;               |
| 0 - Encerrar programa;     |
+----------------------------+
    ''')
    opt = int(input('Digite a opção: '))
    
    quadrado = lambda lado: lado * lado
    retangulo = lambda lado1, lado2: lado1 * lado2
    triangulo = lambda base, altura: (base * altura) / 2
    triangulo_eq = lambda lado: (lado ** 2 * math.sqrt(3)) / 4
    trapezio = lambda maior, menor, altura: ((maior + menor) * altura) / 2
    poligono_regular = lambda nl, tl, apotema:  ((nl * tl) * apotema) / 2
    circulo = lambda raio: math.pi * raio **2

    if opt == 0:
        command = 'cls' if os.name == 'nt' else 'clear'
        os.system(command)
    elif opt == 1:
        print('-=-=-=-=- Área do Quadrado -=-=-=-=-')
        lado = int(input('Digite o Lado: '))
        result = quadrado(lado)
        print(f'Resultado: {result}cm²')
    elif opt == 2:
        print('-=-=-=-=- Área do Retângulo -=-=-=-=-')
        h, w = int(input('Digite a Altura: ')), int(input('Digite a Largura: '))
        result = retangulo(h,w)
        print(f'Resultado: {result}cm²')
    elif opt == 3:
        print('-=-=-=-=- Área do Triângulo -=-=-=-=-')
        b, h  = int(input('Digite a Base: ')), int(input('Digite a Altura: '))
        result = triangulo(b,h)
        print(f'Resultado: {result}cm²')
    elif opt == 4:
        print('-=-=-=-=- Área do Triângulo Equilátero -=-=-=-=-')        
        lado = int(input('Digite o Lado: '))
        result = triangulo_eq(lado)
        print(f'Resultado: {result}cm²')
    elif opt == 5:
        print('-=-=-=-=- Área do Trapézio -=-=-=-=-')        
        maior, menor, altura = int(input('Digite o maior lado: ')),int(input('Digite o menor lado: ')),int(input('Digite a Altura: '))
        result = trapezio(maior, menor, altura)
        print(f'Resultado: {result}cm²')
    elif opt == 6:
        print('-=-=-=-=- Área do Polígono Regular -=-=-=-=-')        
        nl, nt, apotema = int(input('Digite a quantidade de lados: ')),int(input('Digite o perímetro do lado: ')),int(input('Digite a apótema: '))
        result = poligono_regular(nl, nt, apotema)
        print(f'Resultado: {result}cm²')
    elif opt == 7:
        print('-=-=-=-=- Área do Círculo -=-=-=-=-')        
        raio = int(input('Digite o raio: '))
        result = circulo(raio)
        print(f'Resultado: {result}cm²')

elif opt_primary == 2:
    print(f'''
+----------------------------------+
| 1 - Volume do Cubo;              |
| 2 - Volume do Paralelepípedo;    |
| 3 - Volume do Cilindro;          |
| 4 - Volume da Esfera;            |
| 5 - Volume da Pirâmide;          |
| 6 - Volume do Cone;              |
| 7 - Volume do Prisma;            |
| 0 - Encerrar o programa;         |
+----------------------------------+
''')
    opt = int(input('Digite a opção: '))

    volume_cubo = lambda lado : lado ** 3
    volume_paralelepipedo = lambda area_base, altura : area_base * altura;
    volume_cilindro = lambda area_base, altura : area_base * altura;
    volume_esfera = lambda raio: (4*math.pi*raio**3)/3
    volume_piramide = lambda area_base, altura : area_base * altura / 3;
    volume_cone = lambda area_base, altura : area_base * altura / 3;
    volume_prisma = lambda area_base, altura : area_base * altura;

    if opt == 1:
        print('-=-=-=-=- Volume do Cubo -=-=-=-=-')
        lado = int(input('Digite o tamanho do lado: '))
        result = volume_cubo(lado)
        print(f'Resultado: {result}cm³')
    elif opt ==2:
        print('-=-=-=-=- Volume do Paralelepípedo -=-=-=-=-')
        area_base, altura = int(input('Digite a área da Base: ')), int(input('Digite a altura: '))
        result = volume_paralelepipedo(area_base, altura)
        print(f'Resultado: {result}cm³')
    elif opt ==3:
        print('-=-=-=-=- Volume do Cilindro -=-=-=-=-')
        area_base, altura = int(input('Digite a área da Base: ')), int(input('Digite a altura: '))
        result = volume_cilindro(area_base, altura)
        print(f'Resultado: {result}cm³')
    elif opt == 4:
        print('-=-=-=-=- Volume da Esfera -=-=-=-=-')
        raio = int(input('Digite o Raio: '))
        result = volume_esfera(raio)
        print(f'Resultado: {result}cm³')
    elif opt ==5:
        print('-=-=-=-=- Volume da Pirâmide -=-=-=-=-')
        area_base, altura = int(input('Digite a área da Base: ')), int(input('Digite a altura: '))
        result = volume_piramide(area_base, altura)
        print(f'Resultado: {result}cm³')
    elif opt == 6:
        print('-=-=-=-=- Volume do Cone -=-=-=-=-')
        area_base, altura = int(input('Digite a área da Base: ')), int(input('Digite a altura: '))
        result = volume_cone(area_base, altura)
        print(f'Resultado: {result}cm³')
    elif opt == 7:
        print('-=-=-=-=- Volume do Prisma -=-=-=-=-')
        area_base, altura = int(input('Digite a área da Base: ')), int(input('Digite a altura: '))
        result = volume_prisma(area_base, altura)
        print(f'Resultado: {result}cm³')
    elif opt == 0:
        command = 'cls' if os.name == 'nt' else 'clear'
        os.system(command)

elif opt_primary == 0:
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)