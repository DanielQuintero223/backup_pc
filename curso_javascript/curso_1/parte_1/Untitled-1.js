console.log("Hola mundo"); // imprime por consola "Hola mundo"

console.log("Saludos a todos");

/* creacion de variables */

let nombre = "Juan";
let numero_ramdon = 10;

console.log(nombre);
console.log(numero_ramdon);

let varibleNumerica = 10;
let variableString = "Hola mundo";
let variableBooleana = true;
let variableNula = null;
let variableIndefinida = undefined;
let variableArray = [1, 2, 3, 4, 5];

console.log(typeof varibleNumerica);
console.log(typeof variableString);
console.log(typeof variableBooleana);
console.log(typeof variableNula);
console.log(typeof variableIndefinida);
console.log(typeof variableArray);

/* HOISTING */
x = 10;
console.log(x);
var x;

/* constantes */
const PI = 3.1416;
const GRAVEDAD = 9.8;

/* operadores aritmeticos */
let a, b, c, d, e, f;

// suma
a = 10 + 20;
console.log(a);

// resta
b = 20 - 10;
console.log(b);

// multiplicacion
c = 10 * 20;
console.log(c);

// division
d = 20 / 10;
console.log(d);

// residuo
e = 20 % 10;
console.log(e);

// exponente
f = 10 ** 2;
console.log(f);

// pre-incremento
let g = 10;
++g;
console.log(g);

// post-decremento
let h = 10;
--h;
console.log(h);

// pre-incremento
let i = 10;
i++;
console.log(i);

// post-decremento
let j = 10;
j--;
console.log(j);

// operadores de asignacion
let k = 10;
k += 5;
console.log(k);

// operadores de compuestos
let l = 10;
l *= 5;
console.log(l);
l %= 5;
console.log(l);
l **= 5;
console.log(l);

// operadores de comparacion
let m = 10;
let n = 10;

console.log(m == n);

// === compara el valor y el tipo de dato
console.log(m === n);

// != diferente
console.log(m != n);

// !== diferente en valor y tipo de dato
console.log(m !== n);

// operadores de comparacion
let o = 10;
let p = "120";

console.log(o > p);
console.log(o < p);
console.log(o >= p);
console.log(o <= p);
console.log(o == p);
console.log(o === p);

// operadores logicos

let q = 10;
let r = 20;
let s = 30;

console.log(q > r && q < s);
console.log(q > r || q < s);
console.log(!(q > r && q < s));

// valor de rango
let min = 10,
  max = 20;
let dato = 12;

console.log(dato >= min && dato <= max);

// sentencia IF
let edad = 18;

if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

// operador ternario
let edad2 = 18;
let mensaje =
  edad2 >= 18
    ? console.log("Eres mayor de edad")
    : console.log("Eres menor de edad");

let numero = 10;
let mensaje2 =
  numero >= 0
    ? console.log("El numero es positivo")
    : console.log("El numero es negativo");

let numero2 = -10;
let mensaje3 =
  numero2 >= 0
    ? console.log("El numero es positivo")
    : console.log("El numero es negativo");

// arreglos

let arreglo = [10, 22, 33, 44, 51];
console.log(arreglo);
console.log(arreglo[3]);
console.log(`Elemento 3 [3]: ${arreglo[3]}`);

let contador = 1;
for (let i = 0; i < arreglo.length; i++) {
  console.log(contador + ". " + arreglo[i]);
  contador++;
}

// matrices
let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

console.log(matriz);
console.log(matriz[1][2]);

let matriz2 = [[], []];
matriz2[0][0] = 10;
matriz2[0][1] = 20;
matriz2[1][0] = 30;
matriz2[1][1] = 40;
console.log(matriz2);


let matriz3 = [[100,200,300],[400,500,600]];

// Numero de filas
console.log(matriz3.length);
// numero de columnas (depende de la columna seleccionada)
console.log(matriz3[0].length);
console.log(matriz3[1].length);


// interar una matriz
for (let fila=0; fila < matriz3.length; fila++){
  for (let columna=0; columna < matriz3[fila].length; columna++){
    console.log(matriz3[fila][columna]);
  }
}



// procedimiento

function saludar(){
  console.log("Hola mundo");
}

saludar();

// funcion return
function suma(a,b){
  return a+b;
}

let resultado = suma(10,20);
console.log(resultado);


// funcion recursiva
function factorial(n){
  if (n == 0){
    return 1;
  }else{
    return n * factorial(n-1);
  }
}

function reducir(n){
  if (n == 0){
    console.log(n);
    return 0;
  }else{
    console.log(n);
    return reducir(n-1);
  }
}

reducir(10);



