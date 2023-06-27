function ackerman(m: number, n: number) {
    if (m === 0) {
        return n + 1;
    } else if (m > 0 && n === 0) {
        return ackerman(m - 1, 1);
    } else {
        return ackerman(m - 1, ackerman(m, n - 1));
    };
};

function hanoi(discos: number, origen: number, auxiliar: number, destino: number) {
    if (discos === 1) {
        console.log("Mover de", origen, "a", destino);
    } else {
        hanoi(discos - 1, origen, destino, auxiliar);
        console.log("Mover de ", origen, " a ", destino);
        hanoi(discos - 1, auxiliar, origen, destino);
    };
};

function factorial(num: number) {
    if (num === 1) {
        return 1;
    } else {
        return num * factorial(num - 1);
    };
};
console.log(factorial(5));
console.log(ackerman(3, 5));
hanoi(3, 1, 2, 3);

// FIBONACCI NORMAL

function fibonacci1(n: number): number {
    if (n < 2) {
        return n;
    } else {
        return fibonacci1(n - 1) + fibonacci1(n - 2);
    };
};

let variable: number = fibonacci1(10);
console.log(variable);

// FIBONACCI C3D

function fibonacci1(n: number): number {
    if (n < 2) {
        return n;
    } else {
        let fib1 = fibonacci1(n - 1);
        let fib2 = fibonacci1(n - 2);
        return fib1 + fib2;
    };
};

let variable: number = fibonacci1(10);
console.log(variable);

// PAR IMPAR
function par(num: number) :boolean{
    if (num === 0) {
        return true;
    };
    return impar(num - 1);
};

function impar(num: number) :boolean{
    if (num === 0) {
        return false;
    };
    return par(num - 1);
};

console.log(impar(251));