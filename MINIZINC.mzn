int: A;
int: S;
int: B;

array[1..A, 1..B] of int: R;
array[1..A] of int: QA;
array[1..S] of int: QS;
array[1..A] of int: P;
array[1..A] of int: Z;

% Pegar Matriz del generador de instancias con 0 y 1 

array[1..A, 1..S, 1..B] of var 0..1: x;

var int: ct;

constraint ct = sum(i in 1..A, j in 1..S, k in 1..B) (x[i,j,k]P[i])- sum(i in 1..A)(Z[i]P[i]);

constraint forall(j in 1..S, k in 1..B)
(sum(i in 1..A)(x[i,j,k])<=1);
constraint forall(j in 1..S, k in 1..B)
(sum(i in 1..A)(QA[i]* x[i,j,k]) <= QS[j]);
constraint forall(i in 1..A, j in 1..S, k in 1..B)
(x[i,j,k] <= R[i,k]);


solve maximize ct;