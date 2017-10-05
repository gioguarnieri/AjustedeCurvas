# AjustedeCurvas

Programa que ajusta um polinômio de grau N para um conjunto de dados, utilizando o método de minimos quadrados.

O programa cria uma matriz de tamanho NxN, sendo N o grau do polinômio, e pelo método de Gauss Jordan resolve a seguinte Equação:




           [xi^0 y1]   [xi^0 xi^1 xi^2 xi^3 . . . . . xi^n  ]   [a0]
           [xi^1 y2]   [xi^1 xi^2 xi^3 xi^4 . . . . . xi^n+1]   [a1]
           [. . . .] = [ . . . . . . . . . . . . . . . . . .] x [..]
           [. . . .]   [ . . . . . . . . . . . . . . . . . .]   [..]
           [. . . .]   [ . . . . . . . . . . . . . . . . . .]   [..]
           [xi^n yn]   [xi^n xi^n+1 xi^n+2 xi^n+3 . . . x^2n]   [an]

Onde, os _a_ são os coeficientes do polinômio, _xi_ e _yi_ são o somatorio de todos os valores de x e y do conjunto de dados que vão ser ajustados.
