function calcularSaldo(vitorias, derrotas) {
    return vitorias - derrotas;
}

// Função do nível do jogador 
function determinarNivel(vitorias) {
    if (vitorias < 10) {
        return "Ferro";
    } else if (vitorias <= 20) {
        return "Bronze";
    } else if (vitorias <= 50) {
        return "Prata";
    } else if (vitorias <= 80) {
        return "Ouro";
    } else if (vitorias <= 90) {
        return "Diamante";
    } else if (vitorias <= 100) {
        return "Lendário";
    } else {
        return "Imortal";
    }
}

// Função principal / main
function exibirResultado(vitorias, derrotas) {
    const saldo = calcularSaldo(vitorias, derrotas);
    const nivel = determinarNivel(vitorias);
    console.log(`O Herói tem de saldo de ${saldo} está no nível de ${nivel}`);
}


exibirResultado(78, 23);
