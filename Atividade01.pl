#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use feature qw(say);
binmode STDIN,  ':encoding(UTF-8)';
binmode STDOUT, ':encoding(UTF-8)';
binmode STDERR, ':encoding(UTF-8)';

# --------- Helpers ---------
sub ler_inteiro {
    my ($prompt) = @_;
    while (1) {
        print $prompt;
        chomp(my $in = <STDIN> // '');
        $in =~ s/^\s+|\s+$//g;
        if ($in =~ /^[-+]?\d+$/) {
            return int($in);
        }
        say "Entrada inválida. Digite um número inteiro.";
    }
}

sub ler_inteiros {
    my ($qtd, $label) = @_;
    my @v;
    for my $i (1..$qtd) {
        push @v, ler_inteiro("$label $i: ");
    }
    return @v;
}

sub media {
    my (@v) = @_;
    return 0 unless @v;
    my $soma = 0; $soma += $_ for @v;
    return $soma / @v;
}

sub mediana_ordenada_5 {
    my (@v) = sort { $a <=> $b } @_;
    # para 5 elementos, a mediana é o índice 2 (0-based)
    return $v[2];
}

say "==============================";
say "      Programa em Perl        ";
say "==============================";

# 1) Mensagem de boas-vindas + nome personalizado
say "\n(1) Boas-vindas";
say "Bem-vindo(a) ao programa!";
print "Qual é o seu nome? ";
chomp(my $nome = <STDIN> // '');
$nome =~ s/^\s+|\s+$//g;
$nome = length($nome) ? $nome : "visitante";
say "Olá, $nome! Seja bem-vindo(a)!";

# 2) Operações com dois números inteiros
say "\n(2) Operações com dois números inteiros";
my $a = ler_inteiro("Digite o primeiro inteiro: ");
my $b = ler_inteiro("Digite o segundo inteiro: ");

my $soma  = $a + $b;
my $sub   = $a - $b;
my $mult  = $a * $b;

say "Soma:          $a + $b = $soma";
say "Subtração:     $a - $b = $sub";
say "Multiplicação: $a * $b = $mult";

if ($b == 0) {
    say "Divisão:       $a / $b = indefinida (não é possível dividir por zero)";
} else {
    my $div = $a / $b;  # divisão real
    say sprintf("Divisão:       %d / %d = %.6f", $a, $b, $div);
}

# 3) Classificação de inteiro: Positivo, Negativo ou Zero; Par ou Ímpar
say "\n(3) Classificação de número";
my $n = ler_inteiro("Digite um número inteiro: ");

my $sinal = $n > 0 ? "Positivo" : $n < 0 ? "Negativo" : "Zero";
my $parimpar = ($n % 2 == 0) ? "Par" : "Ímpar";
say "O número $n é $sinal e $parimpar.";

# 4) Tabuada formatada até um limite escolhido
say "\n(4) Tabuada formatada";
my $base  = ler_inteiro("Digite o número base da tabuada (inteiro): ");
my $lim   = ler_inteiro("Até onde vai a tabuada? (inteiro ≥ 1): ");
while ($lim < 1) {
    say "O limite deve ser pelo menos 1.";
    $lim = ler_inteiro("Até onde vai a tabuada? (inteiro ≥ 1): ");
}
say "Tabuada de $base até $lim:";
for my $i (1..$lim) {
    my $res = $base * $i;
    say "$base x $i = $res";
}

# 5) Estatísticas de 5 inteiros: maior, menor, média, mediana
say "\n(5) Estatísticas de 5 números inteiros";
my @nums = ler_inteiros(5, "Digite o inteiro");
my @ord  = sort { $a <=> $b } @nums;

my $maior   = $ord[-1];
my $menor   = $ord[0];
my $media   = media(@nums);
my $mediana = mediana_ordenada_5(@nums);

say "\nResultados:";
say "Números informados: @nums";
say "Maior:   $maior";
say "Menor:   $menor";
say sprintf("Média:   %.6f", $media);
say "Mediana: $mediana";

say "\nFim. Obrigado por utilizar o programa!";
