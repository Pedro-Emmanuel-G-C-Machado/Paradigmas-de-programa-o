<?php
// 1. Exibir uma mensagem na tela
echo "Hello, World!";
echo "<br>";

// 2. Realizar um cálculo básico (soma de dois números)
$num1 = 10;
$num2 = 20;
$soma = $num1 + $num2;
echo "A soma de $num1 + $num2 é: $soma";
echo "<br>";

// 3. Criar uma pequena função (calcular a área de um retângulo)
function areaRetangulo($base, $altura) {
    return $base * $altura;
}

$base = 5;
$altura = 8;
echo "A área de um retângulo de base $base e altura $altura é: " . areaRetangulo($base, $altura);
?>
