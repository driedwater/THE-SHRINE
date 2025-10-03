# Topic 1 Sequences

Sequences are ordered and may be infinite
- $(a_1,a_2,a_3,...)$

$a_n$ is a number  
$_n$ is the index

## Other Notation
- $∞$: infinity  
- $∈$: “is an element of”  
- $ℕ$ = 0, 1, 2, 3, ... : the set of natural numbers*  
- $ℤ$ = ... , −2, −1, 0, 1, 2, ... : the set of integers  
- $ℤ^+$ = 1, 2, 3, ... : the set of positive integers  
- $ℤ^−$ = ... , −3, −2, −1 : the set of negative integers  

if notation has subscript, 

## Important Formula

Number of terms  
for $\displaystyle\sum_{k=1}^5$, there are 5 terms,  
for $\displaystyle\sum_{k=0}^4$, there are also 5 terms  


to find num of terms for$\displaystyle\sum_{k=n}^p$: $$p-n+1$$
 


Arithmetic Series Summation  
General formula:
$$a_n = a+(n-1)d$$
Summation formula:
$$S_n = \frac{n[2a+(n-1)d]}{2}$$
$$= \frac{n(a_1+a_n)}{2}$$

Geometric Series Summation  
General Formula: 
$$a_n = ar^{n-1}$$
Summation Formula:  
$$S_n = \frac{a(1 - r^n)}{1 - r}$$
$$ = \frac{a(r^n)-1}{r-1} $$

Infinite Summation 
$$S_∞=\frac{a}{1-r},\ \ \ \ when |r|<1,$$
$a$ is the first element in the sequence,  
$r$ is the ratio

## Recurrance relation

find out next element based on previous element

$$a_n = a_{n-1} [operand] [something]$$

Explicit (General) Formula: reflecting the correlation between term value and its index
$$a_n = f(n)$$

Reursive formula: reflecting the correlation between term value and the value(s) of prior term(s)
$$a_n =f(a_{n-1}),\ \ \  assuming\ (n>1)\ and\ a_1\ is\ given$$
Recurrance relations can use any operand.  
Only important part is that to find $a_{n+1}$, must use $a_n$ and cannot use $_n$

## Series Formula

able find any element based on index  
got 2 kinds, arithmetic and geometric

## Arithmatic Progression

is a sequence of numbers where the **difference** between 2 consective terms is the same

is a sequence with first term a and common difference d
has its terms given by a formula
e.g.  
$$a_n = a+(n-1)d$$

e.g. sequence is 5, 8, 11, 14

## Geometric Progression

is a sequence of numbers where the **ratio** between consecutive terms is the same

is a sequence with first term and common ratio 
has its terms given by a formula  
$$a_n = ar^{n-1}$$

## Summation
$\displaystyle\sum_{k=m}^n a_k = a_m + a_{m+1} + ... + a_n$  

when m=1, often use:  
$S_n = \displaystyle\sum_{k=1}^n a_k$

additivity:  
$\displaystyle\sum_{k=m}^n a_k + \displaystyle\sum_{k=m}^n b_k = \displaystyle\sum_{k=m}^n (a_k+b_k)$  
 
homogenity:  
$\displaystyle\sum_{k=m}^n ca_k = c\displaystyle\sum_{k=m}^n a_k$


**Arithmetic Series Summation**
$$S_n = \frac{n[2a+(n-1)d]}{2}$$
$$= \frac{n(a_1+a_n)}{2}$$

**Arithmetic Summation Application:**

Sum of all positive int $1\leq i \leq 100$  
$S_n = a_1 + ... + a_{100}$  
$= \frac{n[a_1+a_{100}]}{2}$  
$= \frac{100[1+100]}{2}$  
$= 5050$

**Geometric Series Summation**  
when n < ∞ : $$S_n = \frac{a(r^n-1)}{r-1}$$

when n approach ∞:
$$lim_{n->∞},\ \ \ S_n = \frac{a}{r-1}$$

**Geometric series summation application:**  

Investor adds $P$ dollars to an account at the beginning of each year.  
Interest rate $k$ paid at the end of the year  
At beginning of 2nd year, account will have $P(1+k)+P$
At yeat $t$, account will have $P + P(1+k) + ... +P(1+k)^{t-1}$  
  
Value when $t=50, P=100,k=0.01$:
$$S_t = \frac{P[(1+k)^t-1]}{(1+k)-1}$$
$$= \frac{P[(1+k)^t-1]}{k}$$
$$= \frac{100[(1+0.01)^50-1]}{0.01}$$
$$= \$6,446.32$$

## Series , Infinite Summation

Infinite Summation 
$$S_∞=\frac{a}{1-r},\ \ when \ |r|<1,$$
$a$ is the first element in the sequence,  
$r$ is the ratio

**Infinite Summation Application**

$S_∞ = \displaystyle\sum_{n=1}^∞ \frac{1}{3^n}$  
Since exponent in denominator, take out and put in brackets  
$S_∞ = \displaystyle\sum_{n=1}^∞ (\frac{1}{3})^n$  
This makes $\frac{1}{3}$ the ratio.  
So, using Geometric Series summation formula:  
$S_∞ = \frac{\frac{1}{3^1}}{1-\frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{3}*\frac{3}{2} = \frac{1}{2}$


# Topic 2 Number Theory

Purpose: Cryptography  
based on: factoring int into prime factor is hard  
$n = p*q$ where $p$ and $q$ are distinct primes

RSA = Rivest, Shamir adleman  
key length = 1024 - 4096 bits  
- in 2003 estimated 1024 RSA crackable by 2010  
- no evidence yet but minimum recommendation to use at least 2048 RSA

greatest common demoninator (gcd)

1. choose $p$ and $q$, find $n = p*q$
2. choose $e$ such that $gcd(e,(p-1)(q-1)) = 1$
3. solve $d*e == 1(mod(p-1)(q-1))$
4. pub key: ( e, n ), priv key: ( p, q, d )

in number theory,  
mod is modulo which is % in python  
not modulus where is absolute value |x|

## Key formulae

$$a = d*q +r$$
$$r = a \mod d$$

if $a ≡ b \mod m$ and $c ≡ d \mod m$:  

$$a + c ≡ b + d \mod m$$

$$a*c = b*d \mod m$$

given int $I$ and trying see if prime:  
largest number to check shld be $\sqrt{I}$

$$LCM = \frac{a * b}{GCD}\ \ \ \ OR\ \ \ \ GCD = \frac{a * b}{LCM}$$

## Division

a != 0  
a divides b means $\frac{b}{a}$ no remainder  
a does not divide b means $\frac{b}{a}$ have remainder

$$a = d*q+r$$
 a is dividen, d is divisor, q is quotient, r is remainder

## Division Algorithm

let $a$ be integer, $d$ be +ve integer.  
let $q$ and $r$ be unique with $0 <= r < d$

formula is thus

$$a = d*q +r$$
$$r = a \mod d$$


## Modular Arithmetic

≡ triple bar means congruent

$a ≡ b \mod{m}$  
is same as  
$a \mod{m} = b \mod{m}$

**Theorem**  
- let $m$ be +ve int  
- if $a ≡ b \mod{m}$ and $c ≡ d \mod{m}$
- then  
- $$a + c ≡ b + d (\mod{m})$$
- and  
- $$a*c = b*d (\mod{m})$$

Other equations:
- $(a+b)\mod{m} = ((a\mod{m})+(b\mod{m}))\mod{m}$
- $(a-b)\mod{m} = ((a\mod{m})-(b\mod{m}))\mod{m}$
- $(a*b)\mod{m} = ((a\mod{m})*(b\mod{m}))\mod{m}$
- $a^b\mod{m} = (a\mod{m})^b\mod{m}$

$98 \mod{97} = 1$  
$9800 \mod{97} ≡ 100 \mod{97} = 3$  
$98^5 \mod{97} ≡ 98 \mod {97} = 1$  
$10001 \mod{97} ≡ 301 \mod{97} ≡ 10$

## Primes

**Define prime**  
$p > 1$ and only positive factor is 1 and p  
if int $> 1$ and not prime, is a composite

**Theorem**  
every int $> 1$ can be written uniquely as a prime or as a product of 2 or more primes, where prime factors are written in order of non-decreasing size

**Theorem**  
if $n$ is composite int,  
then n has prime divisor $\leq \sqrt{n}$

^ can use theorem to check is num is prime, using brute force method called trial division
divide n by all primes no exceeding $\sqrt n$  
can conclude n is prime if n no divisible by any of these primes

**Theorem**  
there are infintely many primes

## Greatest common Divisor

GCD is the largest integer that divides 2 integers

let $a,b$ be int, non-zero  
largest int $d$ such that $d$ divides $a$ and $d$ divides $b$  
$d$ is therefore the GCD, denoted as $gcd(a.b)$

if $gcd(a, b) =1$  
$a$, $b$ are relatively prime  
e.g. 17 and 22 relatively prime but 22 is not actual prime

integers in set $a^1,a^2,...,a^n$ are pairwise relativly prime if  
$gcd (a^i, a^j) = 1$  when   $1 <= i < j <= n$  
e.g. determine if 10, 17 and 21 are pairwise relativly prime  
$gcd(10,17) =1$  
$gcd(10,21) =1$  
$gcd(17,21) =1$  
thus they are pairwise relatively prime

suppose prime factorisation for +ve int a and b

$a = p_1^{a1},p_2^{a2}, ... ,p_n^{an}$  
$b = p_1^{b1},p_2^{b2}, ... ,p_n^{bn}$  

then, gcd(a,b) is given by  
$gcd(a,b) = p_1^{min(a1,b1)},p_2^{min(a2,b2)}, ... ,p_n^{min(an,bn)}$  
where $min(x,y)$ chooses the smaller of $x$ and $y$

## Least Common Multiple

Least Common Multiple LCM of positive int $a$ and $b$ is smallest possible int that is divisible by both $a$ and $b$  
denoted as $lcm(a.b)$

suppose prime factorisation for +ve int a and b

$a = p_1^{a1},p_2^{a2}, ... ,p_n^{an}$  
$b = p_1^{b1},p_2^{b2}, ... ,p_n^{bn}$  

then, lcm(a,b) is given by  
$gcd(a,b) = p_1^{max(a1,b1)},p_2^{max(a2,b2)}, ... ,p_n^{max(an,bn)}$  

where $max(x,y)$ chooses the larger of $x$ and $y$

$a,b$
$gcd(a,b) * lcm(a,b) = ab$

## Euclidian Algorithm

### Lemma

Let $a = dq+r$  
where $a$, $d$, $q$ and $r$ are int,  

Then, $$gcd(a,d) = gcd(d,r)$$  

lemma above gives us a more efficient method of finding the greatest common divisor,
called the Euclidean algorithm.  

To find gcd(287,91), divide 287 by 91

$$287 = 91 * 3 +14$$

Then lemma says

$$gcd(287,91) = gcd(91,14)$$

now divide 91 by 14

$$91 = 14 * 6 + 7$$

Then lemma says

$$gcd(91,14) = gcd(14,7)$$

now divide 14 by 7

$$14 = 7 * 2 + 0$$

Thus, $gcd(14,7) = 7$  

Therefore,

$$gcd(287,91) = gcd(91,14) = gcd(14,7) = 7$$

## Extended Euclidian Algorithm

Express $gcd(252,198)$ as $252s + 198t$, for some int $s$ and $t$

$$252 = 198*1+54\tag{1}$$

$$198 = 54*3 +36\tag{2}$$

$$54 = 36*1 +18\tag{3}$$

$$36 = 18*2\tag{4}$$

Hence, $gcd(252,198) = gcd(36,18)=18$  

Rearrange (3) so remainder is the subject

$$18 = 54+(-1)(36)$$

sub in the rearranged (2) into the correct pos at 36

$$= 54+(-1)(198+(-3)(54))$$

simplify

$$=(-1)(198)+4(54)$$

sub in the rearranged (1) into the correct pos at 54

$$=(-1)(198)+4(252+(-1)(198))$$

simplify

$$=4(252)+(-5)(198)$$

Hence,

$$s=4, t=-5$$

$$gcd(252,198) = 252(4) + 198(-5)$$


# Topic 3 Combinatronics

Counting and set theory  

## Important Formulas

$$n_1n_2$$

$$n_1 +n_2$$


$n_1 + n_2$ - (ways common to $n_1$ and $n_2$)

$$|A_1 \cup A_2 |= |A_1| + |A_2| - |A_1 \cap A_2|$$

$$\frac{n}{d}$$

$$_nP_r =\frac{n!}{(n-r)}$$

$\frac{N}{k}$, (round up to closest integer)

## Product Rule

Task1 got $n_1$ ways to do.  
For each way in $n_1$, there are $n_2$ ways to do task2.  
Thus, there are $n_1n_2$ ways to do task1 then task2

Use cases, when positions are limited and cannot repeat positions, e.g. offices/remove from limited pool

## Sum Rule

Task got $n_1$ ways of doing or $n_2$ ways of doing.  
None of $n_1$ is same as $n_2$, i.e. mutually exclusive  
Ways to do task = $n_1 +n_2$

Use case, when only 1 "victor" e.g. elect 1 president. 8 males, 5 females, total options 13

## Subtraction Rule

Task can be done in either $n_1$ or $n_2$ ways or both.  
Ways to do task = $n_1 + n_2$ - (ways common to $n_1$ and $n_2$)  
$$|A_1 \cup A_2 |= |A_1| + |A_2| - |A_1 \cap A_2|$$

use case, total 350, 220 in CS, 147 in business, 51 dual major in CS and business, find non-cs non-business

## Division Rule

Task can be done $n$ ways  
For evey way $w$, there are exactly $d$ ways in $n$ that correspond to way $w$ (basically copies due to conditions)  
Then, there are $\frac{n}{d}$ ways to do the task

use case, conditional sequence, e.g. seating next to specific neightbours at square table  
here you rotate clockwise is new arrangement but still same neighbour

## Permutation

define:  
a permutation of a set of distinct objects is an **ORDERED** arrangement of these objects.  
An ordered arrangement of r elements of a set is called an r-permutation (where $r < len(set)$)

e.g.:  
$S = \{1,2,3\}$

Ordered arrangement $(3,1,2)$ is a permutation of S  
Ordered arrangement $(3,2)$ is a 2-permutation of S  

number of $r$-permutations of a set with $n$ elements is denoted by $P(n,r),\ \ ^nP_r,\ \ _nP_r$
$$_nP_r = n(n-1)(n-2)...(n-r+1)$$
$$=\frac{n!}{(n-r)}$$

$_nP_0=1$ whenever n is a non-negative integer since only one way to order 0 elements

1st 2nd 3rd place, 100 contestants  
how many ways to choose winners  
(can be seen as product rule or as permutations)
$_{100}P_3 = 100*99*98 = 970\ 200$

## Combinations

An $r$-combination of a set is an **UNORDERED** selection of $r$ elements from the set.  
Thus, an $r$-
combination is simply a subset of the set, with the subset having $r$ elements.

$S=\{1,2,3,4\}$
$\{1,3,4\}$ is a 3-combination from $S$
$\{4,1,3\}$ is the **SAME** 3-combination, since unordered

Notation:  
$r$-combinations of a set with $n$ distinct elements is denoted by:  
$C(n,r),\ \ ^nC_r,\ \ _nC_r,\ \ (^n_r)$

Theorem:  
number of $r$-combinations of a set with $n$ elements, where $n$ is a non-negative integer and $r$ is an integer with $0\leq r\leq n$ is
$$_nC_r = \frac{n!}{r!(n-r)!}$$

Corollary  
let $n$ and $r$ be non-negative integers with $r\leq n$  
Then, $_nC_r = _nC_{n-r}$  
Thus,
$$_nC_r = \frac{n!}{r!(n-r)!}$$
$$= _nC_{n-r}$$

## Pigeonhole principle

Theorem:  
If $k+1$ or more objects are placed into $k$ boxes, then there is at least 1 box containing 2 or more objects  

E.g.  
Group of 367 people, must be at least 2 with same birthday, since only 366 possible birthdays  
In any group of 27 English words, must be at least 2 that begin with the same letter

## Generalised Pigeonhole principle

Theorem (generalised Pigeonhole principle):  

If $N$ objects placed into $k$ boxes, then there is at least 1 box containing at least $\lceil\frac{N}{k}\rceil$ objects  
$\lceil\rceil$ is ceiling round, round up to nearest integer

e.g. 6 computers in network, all connected to at least 1 other computer.  
Show there are at least 2 computers that have the same number of connections.  
"Holes" are num connections: 1,2,3,4,5  
"Pigeons" are computers  
$N=6,\ k=5$  
$\lceil\frac{6}{5}\rceil=2$

e.g. How many students in class to ensure 6 students get same grade out of (A,B,C,D or F)  
$\lceil\frac{N}{5}\rceil=6$  
$6\leq\lceil\frac{N}{5}\rceil<\frac{N}{5}+1$  
$6\leq\frac{N}{5}+1$  
$5\leq\frac{N}{5}$  
$25\leq\N$  
Ans: $26$


# Topic 4 : Propositional Logic

aka Propositional Calculus or Zeroth-Order Logic

dealing with true or false propositions and logical connectives 
forms compound propositions.

sentance must be a declaration. Even if declaration is wrong, it is still a proposition.  
E.g. 2+2 = 3

sentances that are not declarations cannot be propositions.  
E.g. How old are you?

--------------

## Notation

use letters to denote propositional variables or statement variables  
conventional letters used for propositional variables are $p, q, r, s, ...$

⊤ or T: proposition is true, (Known as a “tee”, “downtack”, or “verum” symbol.)

⊥ or F: proposition is false, (Known as an “up tack” or “falsum” symbol.)

¬ or -: negation, NOT gate

∧: called "wedge", conjuction, AND gate

∨: called "vee", disjuction, OR gate

⊻ or ⊕: Exclusive disjunction, XOR gate

→ or ⇒: Imply, Material Conditional

⇔: Material Biconditional, NOT XOR gates

Let $p$ and $q$ be propositions.  
The proposition $q → p$ is the **converse** of $p → q$.  
The proposition $¬q → ¬p$ is the **contrapositive** of $p → q$.  
The proposition $¬p → ¬q$ is the **inverse** of $p → q$.  

**Converse** : swap left and right hand sides
**Contrapositive** : swap left and right hand sides, NOT both sides
**Inverse** : NOT both sides

**Precedence of logical connectives**  
1. Rule 1: The negation operator (¬) is applied before all other logical operators.
   - So, $¬p ∧ q$ means $¬(p) ∧ q$.  
2. Rule 2: The conjunction operator (∧) takes precedence over the disjunction operator (∨).
   - So, $p ∧ q ∨ r$ means $(p ∧ q) ∨ r$, rather than $p ∧ (q ∨ r)$ .  
3. Rule 3: The material conditional and biconditional operators (→ and ⇔) have lower
precedence than the conjunction ∧ and disjunction ∨ operators.
   - So, $p → q ∨ r$ means $p → (q ∨ r)$ 

|Connective            |Operator|Precedence|
|:---------------------|:------:|:--------:|
|Paranthesis|||
|Quantifiers|||
|Negation              |   ¬    |     1    |
|Conjunction           |   ∧    |     2    |
|Disjunction           |   ∨    |     3    |
|Material Conditional  |   →    |     4    |
|Material Biconditional|   ⇔   |     5    |

XOR between 2 and 3, no universal standard  
if needed in exam, prof will write into the qn when to do XOR



OTHER USEFUL EQUIVALENCES

- Equivalences involving conditionals:
- - $$p → q ≡ ¬q → ¬p$$(Proposition–Contrapositive; or Converse–Inverse)
- - $$p ∨ q ≡ ¬p → q$$
- - $$p ∧ q ≡ ¬(p → ¬q)$$
- - $$¬(p → q) ≡ p ∧ ¬q$$
- Equivalences involving biconditionals:
- - $$p ⇔ q ≡ (p → q) ∧ (q → p) ≡ ¬p ⇔ ¬q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)$$
- - $$¬(p ⇔ q) ≡ p ⇔ ¬q ≡ p ⊕ q$$

---------------

## Propositions

aka Boolean Statements

proposition is a declarative sentence.
declares a fact that is either true or false, but not both.

--------------

### Negation:

Logic gate: NOT

Let $p$ be proposition.  
The negation of $p$, denoted by $-p$, is the statement that the proposition $p$ is false.  
read as "not p"

¬: special NOT symbol

be careful when interpreting propositions, dont over interpret
E.g.  
p = Vandana’s smartphone does not have at least 32 GB of memory.
¬p should be: Vandana’s smartphone **does** have at least 32 GB of memory.
It should not be: Vandana’s smartphone **does** have **more than** 32 GB of memory.

------------------

## Connectives

### Conjuction

Logic gate: AND

Let $p$ and $q$ be propositions.  
The conjunction of $p$ and $q$, denoted by $p ∧ q$, is the proposition “$p$ and $q$”.  
∧: called "wedge"

ways to say:
- and
- but, e.g. p but not r = p and not r
- nevertheless e.g. not p nevertheless, r = not p and r
------------------

### Disjunction

Logic gate: OR

Let $p$ and $q$ be propositions. 
The disjunction of $p$ and $q$, denoted by $p ∨ q$, is the
proposition “p or q”.  
∨: called "vee"

------------------

### Exclusive Disjunction

Logic gate: XOR

Let $p$ and $q$ be propositions. 
The disjunction of $p$ and $q$, denoted by $p ⊻ q$ or $p ⊕ q$ or $p ^ q$, is the
proposition “p exclusive or q”.

------------------

### Material Conditional

Logic gate: IMPLY

Let $p$ and $q$ be propositions.  
The material conditional or material implication, denoted as "$p → q$" or "$p ⇒ q$", is the proposition “if p, then q” or “p implies q”.  

asserts that $q$ is true on the condition that $p$ holds.
**Note**: when $p$ is false, then $p → q$ is true, regardless of the truth value of $q$.

if left hand side true (antecident true) but right hand side (consequence false)

| p | q |$p → q$|
|---|---|-------|
| F | F |   T   |
| F | T |   T   |
| T | F |   F   |
| T | T |   T   |

The Many ways to say $p → q$:
- “if $p$, then $q$”;
- “when/whenever $p$, $q$”;
- “$p$ implies $q$”;
- “$p$ only if $q$”;
- “a sufficient condition for $q$ is $p$”;
- “$q$ is necessary for $p$”;
- “a necessary condition for $p$ is $q$”;
- “$q$ unless not $p$”
- “unless not $p$, $q$”
- “$p$ is sufficient for $q$”;

NOT examples on how to say:
- “$q$ when/whenever $p$”;
- if $q$, will $p$
- if $q$, $p$ will happen

Material Conditional example:  

-----------------
Example 1:  
Consider the following statement: “If it rains, then I will remain indoors.”  
If indeed it rains, then you will expect to find me indoors.  
However, if it does not rain, it does not mean that I have to go outside. I have the option of
either remaining indoors or going outside, when it does not rain.

***Fr guys, just write out a whole truthtable***
"Me taking notes is necessary for me to score an A grade in the module."
Correct ans is :
$p$ = score an A grade
$q$ = took notes

"if $p$ then $q$" or "if $p$, it implies $q$"

WRONG ANS  
if $q$, i will $p$ -----> wrong since you can also score A and not take notes, smarty-pants

Truth Table:  

| got A Grade? | took notes? | if got A grade, implies took notes|
|:------------:|:-----------:|:----------------------------------------------:|
|      No      |      No     |Bum never study, maybe which we treat as true   |
|      No      |     Yes     |L very unfortunate, maybe which we treat as true|
|      Yes     |      No     |HUH HOW!? this guy cheating fr.  PROVES FALSE   |
|      Yes     |     Yes     |Proves proposition right, of course True lah    |

---------------------------

Example 2:  
Consider the conditional statement “If I perform well, I will not get a pay raise”.  
What are the converse, the contrapositive, and the inverse of this statement?  

Let $p$ be the proposition “I perform well”;  
Let $q$ be the proposition “I get a pay raise”.  
Thus $¬q$ is "I do not get a pay raise"

Better to do truth table  

| perform well? | didnt get a raise? |I perform well, I will not get a pay raise|
|:-------------:|:------------------:|:---------------------------------------:|
|       No      |         No         | Bum what you expect. Maybe i.e. true|
|       No      |        Yes         | Maybe you SAF encik and you hit timelimit. Maybe i.e. true|
|       Yes     |         No         |  OI IN WHAT UNIVERSE!? PLEASE ISEKAI ME THERE   |
|       Yes     |        Yes         | Proves proposition right, of course True lah|

------------------

### Material Biconditional

Logic Gate: XNOR

Let $p$ and $q$ be propositions.  
The material biconditional or material bi-implication, denotaed as "$p ⇔ q$" or "$p ↔ q$", is the proposition “$p$ if and only if $q$”.  
The material biconditional $p ⇔ q$ is true when p and q have the same truth values; and false otherwise.  

Note that $p ⇔ q$ is true when both the material conditionals $p → q$ and $q → p$ are true;
otherwise, it is false.

Thus, we can say "if and only if" for this connective.  
Other ways to say:  
- $p iff q$ (yes it is **iff**, not if)
- $p$ is a necessary and sufficient condition for $q$
- $q$ if and only if $p$ 

|$p$|$q$|$p ⇔ q$|
|---|---|--------|
| F | F |   T    |
| F | T |   F    |
| T | F |   F    |
| T | T |   T    |

Derivation of truth table above
| p | q |$p → q$|$q → p$|$(p → q) ∧ (q → p)$|
|---|---|-------|-------|-------------------|
| F | F |   T   |   T   |         T         |
| F | T |   T   |   F   |         F         |
| T | F |   F   |   T   |         F         |
| T | T |   T   |   T   |         T         |

-------------

### Converse, Contrapositive, Inverse

Let $p$ and $q$ be propositions.
The proposition $q → p$ is the **converse** of $p → q$.
The proposition $¬q → ¬p$ is the **contrapositive** of $p → q$.
The proposition $¬p → ¬q$ is the **inverse** of $p → q$.

**Converse** : swap left and right hand sides
**Contrapositive** : swap left and right hand sides, NOT both sides
**Inverse** : NOT both sides

Note:  
Only the **contrapositive** has the **same truth table** as $p → q$  
Truth tables of the **converse** and **inverse** are  the same.

REMINDER: Not all propositions are true. BUT they are still propositions nonetheless

Example:

----------------
This a bit tricky  
This is a Material conditional statement  
Consider the conditional statement “The home team wins whenever it is raining”.  
What are the converse, the contrapositive, and the inverse of this statement?  

Let $p$ be the proposition “it is raining”;  
Let $q$ be the proposition “the home team wins”.  

Better to do truth table  

| is raining | home team winning? |The home team wins whenever it is raining|
|:----------:|:------------------:|:---------------------------------------:|
|     No     |         No         |Does not prove or disprove this, basically maybe which we treat as true|
|     No     |        Yes         |Does not prove or disprove this, basically maybe which we treat as true|
|     Yes    |         No         |  PROVES THIS GUY LYING.  PROVES FALSE   |
|     Yes    |        Yes         | Proves proposition right, of course True lah|

Converse, $q$ implies $p$,  
thus, "if $q$ then $p$"
"if $q$ then $p$" is not same as "if $p$ then $q$"  
CONVERSE IS **NOT** THE SAME AS ORIGINAL

CONVERSE Truth table  
"if Home Team Winning, then it is raining"
| is raining | home team winning? |if Home Team Winning, then it is raining|
|:----------:|:------------------:|:---------------------------------------:|
|     No     |         No         |Does not prove or disprove this, basically maybe which we treat as true|
|     No     |        Yes         |Proved proposition false|
|     Yes    |         No         |Does not prove or disprove this, basically maybe which we treat as true|
|     Yes    |        Yes         | Proves proposition right, of course True lah|

Contrapositive, not $q$ implies not $p$,  
If the home team is not wining, then it is not raining.  
- Explanation
- If you see weather is rain, then you know home team win.  
- If you see home team lose, then you know it wasnt raining  
CONTRAPOSITIVE **IS** THE SAME AS ORIGINAL

CONTRAPOSITIVE Truth table  
| is raining | home team winning? |not is raining|not home team winning|If the home team is not wining, then it is not raining|
|:----------:|:------------------:|:-:|:-:|:---------------------------------------:|
|     No     |         No         |Yes|Yes|Proved true|
|     No     |        Yes         |Yes|No |lucky day? maybe|
|     Yes    |         No         |No |Yes|raining and not winning? Proved false|
|     Yes    |        Yes         |No |No |doesnt prove this, maybe i.e. true|

Inverse, not $p$ implies not $q$,
If it is not raining, then the home team does not win.
INVERSE IS **NOT** THE SAME AS ORIGINAL
INVERSE IS THE **SAME AS CONVERSE**

INVERSE Truth table  
| is raining | home team winning? |If it is not raining, then the home team does not win.|
|:----------:|:------------------:|:---------------------------------------:|
|     No     |         No         |Proved true|
|     No     |        Yes         |proved false|
|     Yes    |         No         |Maybe|
|     Yes    |        Yes         |Maybe|

--------------

example  
Classify an arbitrary object.
if shape is square, then shape is rectangle

let $p$ be "shape is square"  
let $q$ be "shape is rectangle"

|$p$|$q$|$p → q$|Reason|
|---|---|-------|------|
| F | F |   T   |arbitrary shape is neither (maybe)|
| F | T |   T   |arbitrary shape is rectangle (maybe)|
| T | F |   F   |arbitrary shape is square and not rectangle (false)|
| T | T |   T   |arbitrary shape is square and rectangle (always true)|

CONVERSE  
if shape is rectangle, then shape is square
|$p$|$q$|$q → p$|Reason|
|---|---|-------|------|
| F | F |   T   |arbitrary shape is neither (maybe)|
| F | T |   F   |arbitrary shape is rectangle but not square (false)|
| T | F |   T   |true because in this case p is true if q. Since q is F, does not matter what p is|
| T | T |   T   |arbitrary shape is square and rectangle (always true)|


## Precedence of logical connectives

1. Rule 1: The negation operator (¬) is applied before all other logical operators.
   - So, $¬p ∧ q$
means $¬(p) ∧ q$.  
2. Rule 2: The conjunction operator (∧) takes precedence over the disjunction operator (∨).
   - So, $p ∧ q ∨ r$ means $(p ∧ q) ∨ r$, rather than $p ∧ (q ∨ r)$ .  
3. Rule 3: The material conditional and biconditional operators (→ and ⇔) have lower
precedence than the conjunction ∧ and disjunction ∨ operators.
   - So, $p → q ∨ r$ means $p → (q ∨ r)$ 

|Connective            |Operator|Precedence|
|:---------------------|:------:|:--------:|
|Negation              |   ¬    |     1    |
|Conjunction           |   ∧    |     2    |
|Disjunction           |   ∨    |     3    |
|Material Conditional  |   →    |     4    |
|Material Biconditional|   ⇔   |     5    |

XOR between 2 and 3, no universal standard  
if needed in exam, prof will write into the qn when to do XOR

## Compound Proposition

compound proposition refers to an expression formed from atomic propositional variables ($p,q,r,s$) using logical connectives (operators).  
Examples representations:

--------
$¬r$
$p ∨ q$
$p ⇔ q$
$(p → q) ∧ (r → p)$
$(r ∧ q) → (r ⊕ p)$

-----------
Examples:

--------------
Construct Truth Table for: $(p ∨ ¬q) → (p ∧ q)$

|p|q|¬q|$p ∨ ¬q$|$p ∧ q$|$(p ∨ ¬q) → (p ∧ q)$|
|-|-|--|--------|-------|--------------------|
|F|F| T|    T   |   F   |         F          |
|F|T| F|    F   |   F   |         T          |
|T|F| T|    T   |   F   |         F          |
|T|T| F|    T   |   T   |         T          |

## Logical equivelence

Compound propositions $P$ and $Q$ are logically equivalent if $P ⇔ Q$ is a tautology (Has identical truth table).  
The notation $P ≡ Q$ denotes that $P$ and $Q$ are logically equivalent.

Example  

--------------
De Morgan laws
Show $¬(p ∧ q) ≡ ¬p ∨ ¬q$ (law 1)
|$p$|$q$|$p ∧ q$|$¬(p ∧ q)$|$¬p$|$¬q$|$¬p ∨ ¬q$|
|---|---|-------|----------|----|----|---------|
| F | F |   F   |    T     |  T |  T |    T    |
| F | T |   F   |    T     |  T |  F |    T    |
| T | F |   F   |    T     |  F |  T |    T    |
| T | T |   T   |    F     |  F |  F |    F    |

Show $¬(p ∨ q) ≡ ¬p ∧ ¬q$ (law 2)
|$p$|$q$|$p ∨ q$|$¬(p ∨ q)$|$¬p$|$¬q$|$¬p ∧ ¬q$|
|---|---|-------|----------|----|----|---------|
| F | F |   F   |    T     |  T |  T |    T    |
| F | T |   T   |    F     |  T |  F |    F    |
| T | F |   T   |    F     |  F |  T |    F    |
| T | T |   F   |    T     |  F |  F |    F    |

-----------

is $p → q ≡ ¬p ∨ q$?

|$p$|$q$|$¬p$|$p → q$|$¬p ∨ q$|
|---|---|----|-------|--------|
| F | F |  T |   T   |   T    |
| F | T |  T |   T   |   T    |
| T | F |  F |   F   |   F    |
| T | T |  F |   T   |   T    |

ans: yes since truth tables identical

-------------------

OTHER USEFUL EQUIVALENCES

- Equivalences involving conditionals:
- - $$p → q ≡ ¬q → ¬p$$ -(Proposition–Contrapositive; or Converse–Inverse)
- - $$p ∨ q ≡ ¬p → q$$
- - $$p ∧ q ≡ ¬(p → ¬q)$$
- - $$¬(p → q) ≡ p ∧ ¬q$$
- Equivalences involving biconditionals:
- - $$p ⇔ q ≡ (p → q) ∧ (q → p) ≡ ¬p ⇔ ¬q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)$$
- - $$¬(p ⇔ q) ≡ p ⇔ ¬q ≡ p ⊕ q$$

## Tautology, Contradiction, Contingency, Satifiability

### Tautology

A compound proposition that is always true, no matter what the truth values of its
propositional variables, is **called a tautology**.

**Always true for all inputs**

-------

### Contradiction

A compound proposition that is always false is called a contradiction.

**Always false for all inputs**

--------

### Contingency

A compound proposition that is neither a tautology nor a contradiction is called a
contingency.

**True for some inputs, False for other inputs**

--------

### Satifiability

A proposition is satisfiable if it is **true under some assignment of values** to its propositional variables.

Satisfied = Value is true (wether through combination of inputs or tautology)
Satisfiable = Value can be made to be true through combination of inputs

Tautologies are satisfiable.
- always satisfied.
- i.e always true for any assignment of values to input.

Contradictions are unsatisfiable.
- never satisfied.
- i.e. always false for any assignment of values to input.

Contingencies are satisfiable.
- can be either satisfied or not satisfied.
- i.e. either true or false depending on input.
- satisfied by some input, unsatisfied by others.
- *Note that contingencies, by definition, are neither tautologies nor contradictions.


Example

--------

𝑝 ∨ ¬𝑝 is a tautology.  
𝑝 ∧ ¬𝑝 is a contradiction.

---------

# Topic 5: Predicate Logic

Predicate Logic: enables concise and general expressions

Statements with variables may not be able to become a proposition.
e.g. $x>4$ or $x=y+3$ or "Every student in my class had submitted at least one assignmnet"

"Every student in my class had submitted at least one assignmnet"  
This sentance requires one proposition per student  
However, can say $P(x) =$ x has submitted an assignment

the subject: x  
the predicate (a property of x): had submitted an assignment

The predicate now represents the whole student set

once $x$ has a value, then can get a truth value

## Predicate / Propositional Fucntion

$$S(x): x\ is\ a\ student$$

x is the variable, represent objs from a group/set

S is a predicate, a property that is applied to x

S() is a propositional function, applying the predicate to the variable, itself is NOT a propositions

e.g. of usage  
S(Alice): Alice is a student, aka True
S(Abhishek): Ahbishek is NOT a student, aka False

variables come from a domain, likE a type in programming
e.g. All positive integers, all students in a class

Consider:  
"All students are hardworking"  
"Alice is a student"
Does it follow that: "Alice is hard-working"?

## Quantifiers

Quantifiers in Predicate logic
1. Universal Quantifier, $∀$
   - Truth Value using domain
   - Truth value using counter example
2. Existential Quantifier
   - Truth value using domain

Quantifier with restricted domain
Precedence of Quantifier
Negatin Quantified Expressions
Nested Quantifiers
   - Quantification of two variables

### Universal Quantifier, $∀$

$$∀x\ P(x)$$
$$∀x\ P(x) = P(x_1) ∧ P(x_2) ∧ P(x_3) {...}$$

read as "For all $x$, $P(x)$" or "For every $x$ , $P(x)$" or "Every x in [domain] [predicate]"

e.g.  
Every student in your class has taken a course in python  
Every x in set of positive integers fulfills x > 0

assert property is true for all values of x in particular domain (called domain of discourse / universe of discourse)

The Universal quantification of $P(x)$ for a particular domain is the proposition that asserts that $P(x)$ is true for all values of x in this domain.  
**BUT $∀x\ P(x)$ is NOT a proposition, it is a quantifier. BUT the quantifier can have a truth value**  
can be thought of as a conjunction of all values of x. I.e

$$∀x\ P(x) = P(1) ∧ P(2) ∧ P(3)$$

If one value of P(x) is false, then $∀x\ P(x)$ will be false  

truth value of $∀x\ P(x)$ will change when the domain changes.  
Thus, domain must be specified when universal quantifier is used, otherwise universal quantifier is not defined

![predicate-logic-domains](jacob-images/predicate-logic-domains.png)

### Universal Quantifier, Counter examples

A statement $∀x\ P(x)$ is false, where $P(x)$ is a propositional function, if and only if $P(x)$ is not always true when $x$ is in the domain

$$∀x\ P(x) ↔ P(x)\ for\ all\ x$$

### Existential Quantifier, $∃$

$$∃x\ P(x)$$
$$∃x\ P(x) = P(x_1) ∨ P(x_2) ∨ P(x_3) {...}$$

read as "There exists an $x$, such that $P(x)$" or "For some $x$, $P(x)$"  

**Same as $∀x\ P(x)$, $∃x\ P(x)$ is NOT a proposition, it is a quantifier. BUT the quantifier can have a truth value**  
"There exists an element $x$ in the domain, such that $P(x)$ 

truth value of $∃x\ P(x)$ will change when the domain changes.  
Thus, domain must be specified when Existential quantifier is used, otherwise Existential quantifier is not defined


## Quantifiers, Restricted Domains

in the domain of all real numbers
$$∀x < 0\ (x^2 > 0)$$
$$∀y \neq 0\ (y^3 \neq 0)$$
$$∃z > 0\ (z^2 = 2)$$

in $∀x < 0\ (x^2 > 0)$, the domain is all real numbers where $x < 0$ and the predicate is $(x^2 > 0)$

every non-zero real number y, y^3 is also a non-zero number

there exists a positive real number z such that z^2 = 2

## Logical Precedence of Quantifiers

Both quantifiers have higher precedence than all logical operators  
$$∀x P(x) ∨ Q(x)\ !\equiv ∀x (P(x) ∨ Q(x))$$
$$∀x P(x) ∨ Q(x)\ \equiv (∀x P(x)) ∨ Q(x)$$

## Negating Quantified Expressions

$$¬∀x\ P(x) \equiv ∃x(¬P(x))$$
$$¬∃x\ P(x) \equiv ∀x(¬P(x))$$

E.g.  
"Every student in your class has taken a course in Python."  
P(x) = x has taken a course in Python  
Domain = students in your class
$∀x\ P(x)$
Negate statement = $¬∀x\ P(x)$  
"NOT Every student in your class has taken a course in Python."  
AKA
"There is a student in your class who has not taken a course in Python"  
$∃x(¬P(x))$


"There is a student in your class who has taken a course in Python."  
P(x) = x has taken a course in Python  
Domain = students in your class
$∃x\ P(x)$
Negate statement = $¬∃x\ P(x)$  
"There is NOT student in your class who has taken a course in Python."  
AKA
"Every student in your class has NOT taken a course in Python"  
$∀x(¬P(x))$

$$¬∀x(x^2 > x) \equiv ∃x(x^2 \leq x)$$
$$¬∃x(x^2=2) \equiv ∀x(x^2 \neq 2)$$

## Nested Quantifiers

![table-of-nested-quatifiers](jacob-images/table-of-nested-quatifiers.png)


q1. domain is real numbers
$$∀x∃y(x + y = 0)$$
$$\equiv ∀x Q(x), Q(x) = ∃y(x + y = 0)$$

read as "for every real number x, thereis a real number y such that $x + y = 0$"  
i.e. for every real number x, there is an real number y that is the addative inverse of x

q2. domain is real numbers
$$∀x∀y(x + y = y + x)$$

read as "x + y = y + x, for all x and y real numbers"

q3. domain is real numbers
$$∀x∀y((x > 0) ∧ (y < 0) → (xy < 0))$$

read as "for every real number x and for every real number y, if $x > 0$ and $y < 0$, then $xy < 0$

q4.
let $Q(x,y)$ denote '$x + y = 0$'  
What are the truth values of the following:
$$∃y∀xQ(x,y)$$
$$∀x∃yQ(x,y)$$

$∃y∀xQ(x,y)$ = $∃y(∀xQ(x,y))$ = There is a real number $y$ such that for every real number $x$, $x + y = 0$.  
Cannot be true as there is no singular real number $y$ such that $x + y = 0$ every real number $x$

$∀x∃yQ(x,y)$ = $∀x(∃yQ(x,y))$ = For every real number $x$, there is a real number $y$ such that , $x + y = 0$.  
Can be true as tor a given real number $x$, we can choose a real number $y$ such that $x + y = 0$


-----------------------------------------------------------------

# Tutorial 1 
## q1
1a. $\displaystyle\sum_{k=1}^5(k+1)$
1. find num of terms, 
2. write out first few terms if have many
3. determine they type of sequence: in ths case: arithmetic

1b. $\displaystyle\sum_{j=0}^4(-2)^j$
1. mind the index
2. mind lower limit
3. determine if this is a special sequence
geometric

1c. $\displaystyle\sum_{i=0}^10-3$
1. mind the index
2. mind lower limit
3. determine if this is a special sequence
4. in this case is geometric or ????

1d. $\displaystyle\sum_{j=0}^8(2^{j+1}-2^j)$
1. Mind index
2. mind lower limit
3. simplify the summation terms in advance: $2*2^j-2^j = $  
OR  
break up into sum of 2 summations: $\displaystyle\sum_{j=0}^8(2^{j+1}) - \displaystyle\sum_{j=0}^8(-2^j)$
4. determine the secial sequence, in this case: geometric

## q2
1. generate terms one after another (recursive formula)
you can determin it is recusive since you see $a_{n-1}$

## q3
1. use heeuristic approach (list first few terms) for calculation or verification  
1 year: $1000 * (1+7\%)^1$  
2 year: $1000 * (1+7\%)^2$  
3 year: $1000 * (1+7\%)^3$  
4 year: $1000 * (1+7\%)^4$

Compund interest is a geometric sequence.  

## q4
Find the sum of the first n terms of an arithmetic series whose first term is 1 and whose common
difference is 5  
$a_n = a + (n-1)d$  
$a_1 = 1$, $d = 5$  
$S_n = \frac{n(2a + (n-1)d)}{2} = \frac{n(5n-3)}{2}$

## q5

application of general formula and summation equation of arithetic progression
only need know first term and common difference to determin an arithmetic progression

term 7 = 7,  
sum of first 10 terms is 60  
$a_7 = a+6d = 7 $  
$S_{10} = \frac{10(2a+9d)}{2} = 60$  
solve the linear equations with two variables, a=3, d=$\frac{2}{3}$

## q6
min the number of terms
find expression for $2(3) +2(3)^2 + ... +2(3)^n$
is geometric  
first term a = 2, common ratio r = 3
total n+1 terms
$$S_{n+1} = \frac{a(1-r^{n+1})}{1-r} = \frac{2(1-3^{n+1})}{1-3} = 3^{n+1}-1$$

$$S_{n+1} = S_n + a_{n+1} = \frac{a(1-r^n)}{1-r} + a_nr$$

## q7

7a. 
$\displaystyle\sum_{j=0}^8 3*2^j$

$j=0, 3*2^0 = 3$  
$j=1, 3*2^1 = 6$  
$j=2, 3*2^2 = 12$  
actually is geometric prograssion  
a = 3, r = 2

7b.
$\displaystyle\sum_{j=0}^8 (-3^j)$

$j=0, -3^0 = 9$  
$j=1, 3^1 = -27$  
$j=2, 3^2 = 81$  
actually is geometric prograssion  
a = 3, r = 2

7c.
$\displaystyle\sum_{j=4}^10 (2+3j)$  
mind lower limit  
mind number of terms  
$a_j=2*3j$  
$a_{j+1}=2*3{j+1}$  
$a_{j+2}=2*3{j+2}$

actually is arithmetic prograssion

## q8

Mind index  
can directly use summation euation for geometric progression when the number of terms is approching infinity

$a_0 = \frac{1}{2^{2n}} = \frac{1}{2^{2*0}} = 1$
$a_1 = \frac{1}{2^{2n}} = \frac{1}{2^{2*1}} = \frac{1}{4}$

geometric progression, a = 1, r = $\frac{1}{4}$

$$lim_{n->∞} S_n = lim_{n->∞} \frac{a(1-r^n)}{1-r} = lim_{n->∞} \frac{1(1-\frac{1}{4}^n)}{1-\frac{1}{4}} = \frac{4}{3}$$

## example exam qn:  
$$\displaystyle\sum_{j=0}^8 (3*2^j+(2+3j))$$
$$\displaystyle\sum_{j=0}^8(3*2^j) + \displaystyle\sum_{j=0}^8(2+3j)$$

# Tutorial 2

first few qn are about modulo ops  
middle few qn are about prime factorisationn
last few qn is euclidian and exxtended euclidian

## Q1

normal long division to find remainder  
or write out $a=qm+r$ into $r=a\mod{m}$

## Q2

$a≡b\mod{m}$ means
$a\mod{m} = b\mod{m}$
$a=qm+r$
q can be any integer. Thus a can be -42,-15,12,39 or onwards
since have constraint $0\leq a\leq26$

## Q3

Check remainder of both left and right portions of equation.
if remainders do not match, then not congruent

## Q4

Brute forcce each mod in the bracckets first then add the two remainders  
OR  
use modulo arithmetic property (Addition) formula

NOTE, following equation is incorrect application of the addition formula:  
$(-133\mod{23})+(26\mod{23})=(-133+26)\mod{23}$  

$(-133\mod{23})$, remainder is between 0 and 22  
$(26\mod{23})$, remainder is between 0 and 22  
BUT if add both remainders together, may result in value more than 23. so thats why need mod again

it should be:  
$(a+b)\mod{m} = ((a\mod{m})+(b\mod{m}))\mod{m}$

## Q5

Be careful of exponentiation and mutiplication property of modulo arithmetic

## Q6

any composite int will have at least 1 prime number divisor that is $\leq \sqrt{n}$

Can prove if prime by checking if number mod all primes less than $\sqrt{n}$ = 0

## Q7

rather than do normal prime factorisation, you can check for first prime by using the modulo method,  
e.g. 1001 mod 7 = 0  
hence, 1001 = 7 * 143  
then use the modulo method on 143 again to get 11 * 13  
Thus, 1001 = 7 * 11 * 13  

May need to prove all nums are prime  
e.g. 1111 = 11 * 101, need to prove 101 is prime

## Q8

find all **factors** (not prime factors) of each number $n$ from 1 to $n$  
This helps to prove GCD between 2 nums is 1

e.g.  
15: 1,3,5,15  
11: 1,11  
19: 1,19

## Q9

remember, GCD is min power of **common** prime factors  

if number has no prime facctor, can do power 0 to represent easier  
e.g.  
$(3^5 * 5^5)=(2^0 * 3^5 * 5^5)$

## Q10

Prime factorise both numbers  
find gcd and lcm.  
prove with basic math that $gcd(a,b) * lcm(a,b) = ab$

## Q11

normal euclidian algo, just practice application

## Q12

when applying extended euclidian, be careful when simplifying and when making remainder the subject of the equation

------------

# Tutorial 3 

product rule can be extended to more than 2 ways to do task

subtraction rule is more general form off sum rule

$C(n,r) = \frac{n!}{r!(n-r)!} = \frac{P(n,r)}{r!}$

^^ application of division rule, as order does not matter so items that have the same elements in different order are considered identical.

num pigeonholes always less than num pigeons for pigeonhole principle to work

## q1

a:  
subtask 1: find a position for the bride  
subtask 2: find ordered arrangement of 5-1=4 non-repetitive people out of pool of 10-1=9 people  
$P(9,4) = 3024$
$3024*5=15120$
ans: 15120

b: 
subtask1: find pos for brid  
subtask 2: find pos for groom  
subtask 3: find ordered arrangement of 5-2=3 non-repetittive people out of pool of 10-2=8  
$P(8,3) = 336$
$5*4*336 = 6720$
ans: 6720

c:
subtask 1: brid or groom pos  
subtask 2: dettermine iff bride or groom in pic  
subtask 3: find ordered arrangemenr of $5-1=4$ non-repetitive people out of pool of $10-2=8$  
$P(8,4) = 1680$
$5*2*1680=16800$
ans: 16800

Note: be careful of pool to choose from

## q2

a:
apply product rule, cannot use permutation as arrangement can include repetitive elements  
task determine all 8 bit  
eacch bit is subtask with 2 ways to choose  
num ways to do  is $2^8 = 256$
ans: 256

b:
task: determin positions of four 1's in string
find unordered arrangement off 4 non-repetitive positions out of 10
basically, choose from positions, not choose from 0 or 1  
use combination as the order of the 4 chosen positions does not matter  
$C(10,4)=\frac{10!}{4!(10-4)!}=210$
ans:210

c:
task find num strings that contain at most four 1's
same as b, choose from positions, use combination as order of chosen places does not matter  
set of strings with no 1's: $C(10,0) = 1$  
set of strings with one 1: $C(10,1) = 10$  
set of strings with two 1: $C(10,2) = 45$  
set of strings with three 1: $C(10,3) = 120$  
set of strings with four 1: $C(10,4) = 210$  
apply sum rule  
sum all sets: $1+10+45+120+210=386$  
ans: 386

d:
same idea as part c but for 4-10
set of strings with four 1's: $C(10,4) = 210$  
set of strings with five 1: $C(10,1) = 252$  
set of strings with six 1: $C(10,2) = 210$  
set of strings with seven 1: $C(10,3) = 120$  
set of strings with eight 1: $C(10,4) = 45$  
set of strings with nine 1: $C(10,4) = 10$  
set of strings with ten 1: $C(10,4) = 1$  
apply sum rule  
sum all sets: $210+252+210+45+10+1=386$  
ans: 848

## q3
about permutations

a:  
permutation containing string BCD  
let BCD be X  
number off permutation of letters AEFGX  
$P(5,5) = 5! = 120$

b:  
permutation containing string CFEA  
let CFEA be X
num permutations of BDGX  
$P(4,4) = 4! = 24$

c: 
permutation containing string BA and GF  
let BA = X, GF = Y  
num permutations of CEDXY  
$P(5,5) = 5! = 120$

d:  
permutation containing string ABC and DE  
let ABC = X, DE = Y  
num permutations of FGXY  
$P(4,4) = 4! = 24$  

e:  
permutation containing string ABC and CDEF  
string that contains ABC and CDEF must contain ABCDEF = X
num permutations of GX  
$P(2,2) = 2! = 2$ 

f:
permutation containing string CBA and BED  
string is impossible to simultaneously contain CBA and BED as will require both letter A and letter E to come right after B  
num permutations is 0

## q4

question turns into placing women in slots between men

task: form line with 13 people, 8 men 5 women, so that no woman stands next to another women  

subtask 1: find ordered arangement for 8 non-repetitive men out of pool of 8 men

subtask 2: find ordered arrangement of 5 non-repetitive women out of $8+1=9$ slots


num positions for men: 8  
num positions between men for women: 9
possible pos for men: $P(8,8) = 8! = 40,320$
possible pos for women: $P(9,5) = 15,120$
total num ways to arrange: $40,320 * 15,120 = 609,638,400$

## q5

order of chosen members does not matter, so use combination

subtask 1: find unordered arrangement of 4 non-repetitive men out of pool of 10 men
$C(10,4) = \frac{10!}{4!(10-4)!} = 210$


subtask 2: find unordered arrangement of 4 non-repetitive men out of pool of 15 women
$C(15,4) = \frac{15!}{4!(15-4)!} = 1365$
$210 * 1365 = 286650$

ans: 286650

## q6

find correspondance between question and piggeonholes  
$n$ pigeons placed in $k$ pigeon holes  
at least one **box** contains at least $\lceil\frac{n}{k}\rceil$ pigeons  
"*at least 7 students* get the same **score**"

pigeons: students n  
pigeonholes: possible scores k = 101  

$$\lceil\frac{n}{k}\rceil = \lceil\frac{n}{101}\rceil \geq 7$$
$$= \frac{n}{101} > 7-1$$
$$= n > 6*101 $$
$$= n \geq 607$$

ans: $n \geq 607$

## q7

a;
find correspondance between question and piggeonholes  
$n$ pigeons placed in $k$ pigeon holes  
at least one **box** contains at least $\lceil\frac{n}{k}\rceil$ pigeons 

pairs of int with sum 9 = (1,8), (2,7), (3,6), (4,5)

"there must be a pair on integers with a sum equal to 9" is equivalent to:  
"at least *two selected numbers* belong to **one of the four pairs** above"

pigeons: selected positive int in range [1,8], n=5  
pigeonholes: pairs of int that sum to 9, k=4  

$$\lceil\frac{n}{k}\rceil = \lceil\frac{5}{4}\rceil = 2$$

At least 2 int selected is from one of the four pairs with a sum of 9

b:  
pigeons: selected positive int in range [1,8], n=4  
pigeonholes: pairs of int that sum to 9, k=4  
$$\lceil\frac{n}{k}\rceil = \lceil\frac{4}{4}\rceil = 1$$
At least 1 int selected is from one of the four pairs with a sum of 9

## q8

better to make set of pairs rather than assume all even or all odd

pigeons: houses, n = 51  
pigeonholes: pairs of consecutive addresses, k = 50
$$\lceil\frac{n}{k}\rceil = \lceil\frac{51}{50}\rceil = 2$$

50 pairs of onseccutive addresses: (1000, 1001), (1002, 1003), ... , (1098,1099)
first 50 choose one of two addresses within unique pair
last house will be unable to choose from a unique pair

-----------

# Tutorial 4 
## q1

a. Missing the final exam implies you will not pass the course  
ans: if miss then fail  
b. Having Covid-19 or missing the final exam implies you will not pass the course  
ans: if have covid, then fail or if miss, then fail

|$p$|$q$|$r$|$¬r$|$p → ¬r$|$q → ¬r$|$(p → ¬r) ∨ (q→ ¬r)$|$(p ∨ q) → ¬r$ (wrong)|
|---|---|---|----|--------|--------|--------------------|--------------|
| F | F | F | T  |   T    |   T    |         T          |     T        |
| F | F | T | F  |   T    |   T    |         T          |     T        |
| F | T | F | T  |   T    |   T    |         T          |     T        |
| F | T | T | F  |   T    |   F    |         T          |     F        |
| T | F | F | T  |   T    |   T    |         T          |     T        |
| T | F | T | F  |   F    |   T    |         T          |     F        |
| T | T | F | T  |   T    |   T    |         T          |     T        |
| T | T | T | F  |   F    |   F    |         F          |     F        |

c. You will pass the course if you did not miss the exam or missed the exam due to having having COVID-19  
Ans: either have coccid and miss or do not miss and pass

|$p$|$q$|$r$|$¬q$|$p ∧ q$|$¬q ∧ r$|$(p ∧ q) ∨ (¬q ∧ r)$|
|---|---|---|----|-------|--------|--------------------|
| F | F | F | T  |   F   |   F    |         F          |
| F | F | T | T  |   F   |   T    |         T          |
| F | T | F | F  |   F   |   F    |         F          |
| F | T | T | F  |   F   |   F    |         F          |
| T | F | F | T  |   F   |   F    |         F          |
| T | F | T | T  |   F   |   T    |         T          |
| T | T | F | F  |   T   |   F    |         T          |
| T | T | T | F  |   T   |   F    |         T          |

## q2

'but not' is just 'and not'
'still' is just 'and'
'nevertheless' is just and

'is sufficent' is just 'implies'
'is necessary' is just 'implies'

p is sufficent for q
q is necessary for p

a. $r ∧ ¬q$  
ans: $r ∧ ¬q$  
b. $(p ∧ ¬q) ∧ r$  
ans: $(p ∧ ¬q) ∧ r$  

|$p$|$q$|$r$|$¬q$|$(p ∧ ¬q)$|$(p ∧ ¬q) → r$|
|---|---|---|----|----------|--------------|
| F | F | F | T  |     F    |      T       |
| F | F | T | T  |     F    |      T       |
| F | T | F | F  |     F    |      T       |
| F | T | T | F  |     F    |      T       |
| T | F | F | T  |     T    |      F       |
| T | F | T | T  |     T    |      T       |
| T | T | F | F  |     F    |      T       |
| T | T | T | F  |     F    |      T       |

c. $(p ∧ q) → r$  
ans: $(p ∧ q) → r$  

d. $r ⇔ (p ∨ q)$  
ans: $r ⇔ (q ∨ p)$  


## q3

a.  
p = get to top of Bukit Timah Hill  
q = need to hike 2km  
if you want to get to top of Bukit Timah Hill, then you need to hike 2km  
ans:
p = get to top of Bukit Timah Hill  
q = need to hike 2km  
If you get to the top of Bukit Timah Hill, then you must have hiked 2km

b.  
p = drive more than 650 km  
q = need to buy gasoline  
if you drive more than 650 km, then you will need to buy gasoline.
correct

c.  
Xiaoming will go swimming unless the water is too cold.  
p = water is not too cold  
q = Xiaoming will go swimming  
if the water is not too cold, then Xiaoming will go swimming  

alt ans:
If Xiaoming not swimming, water must be too cold

## q4

a. $(p → q) ⇔ (¬p → ¬q)$  

|$p$|$q$|$¬p$|$¬q$|$(p → q)$|$(¬p → ¬q)$|$(p → q) ⇔ (¬p → ¬q)$|
|:-:|:-:|:--:|:--:|:-------:|:----------:|:-------------------:|
| F | F | T  | T  |    T    |     T      |         T           |
| F | T | T  | F  |    T    |     F      |         F           |
| T | F | F  | T  |    F    |     T      |         F           |
| T | T | F  | F  |    T    |     T      |         T           |

ans$(p → q) ⇔ (¬q → ¬p)$ all true
|$p$|$q$|$¬p$|$¬q$|$(p → q)$|$(¬q → ¬p)$|$(p → q) ⇔ (¬q → ¬p)$|
|:-:|:-:|:--:|:--:|:-------:|:----------:|:-------------------:|
| F | F | T  | T  |    T    |     T      |         T           |
| F | T | T  | F  |    T    |     T      |         T           |
| T | F | F  | T  |    F    |     F      |         T           |
| T | T | F  | F  |    T    |     T      |         T           |

b. $(p ⊕ q) ∧ (p ⊕ ¬q)$  
correct
|$p$|$q$|$¬q$|$(p ⊕ q)$|$(p ⊕ ¬q)$|$(p ⊕ q) ∧ (p ⊕ ¬q)$|
|:-:|:-:|:--:|:--------:|:---------:|:--------------------:|
| F | F | T  |    F     |     T     |          F           |
| F | T | F  |    T     |     F     |          F           |
| T | F | T  |    T     |     F     |          F           |
| T | T | F  |    F     |     T     |          F           |


c. $(p ↔ q) ∨ (¬q ↔ r)$  
correct
|$p$|$q$|$r$|$¬q$|$(p ↔ q)$|$(¬q ↔ r)$|$(p ↔ q) ∨ (¬q ↔ r)$|
|:-:|:-:|:-:|:--:|:-------:|:--------:|:------------------:|
| F | F | F | T  |    T    |    F     |        T           |
| F | F | T | T  |    T    |    T     |        T           |
| F | T | F | F  |    F    |    T     |        T           |
| F | T | T | F  |    F    |    F     |        F           |
| T | F | F | T  |    F    |    F     |        F           |
| T | F | T | T  |    F    |    T     |        T           |
| T | T | F | F  |    T    |    T     |        T           |
| T | T | T | F  |    T    |    F     |        T           |


d. $((p → q) → r) → s$
ccorrect
|$p$|$q$|$r$|$s$|$(p → q)$|$(p → q) → r$|$((p → q) → r) → s$|
|:-:|:-:|:-:|:-:|:-------:|:-----------:|:-----------------:|
| F | F | F | F |    T    |      F      |        T          |
| F | F | F | T |    T    |      F      |        T          |
| F | F | T | F |    T    |      T      |        F          |
| F | F | T | T |    T    |      T      |        T          |
| F | T | F | F |    T    |      F      |        T          |
| F | T | F | T |    T    |      F      |        T          |
| F | T | T | F |    T    |      T      |        F          |
| F | T | T | T |    T    |      T      |        T          |
| T | F | F | F |    F    |      T      |        F          |
| T | F | F | T |    F    |      T      |        T          |
| T | F | T | F |    F    |      T      |        F          |
| T | F | T | T |    F    |      T      |        T          |
| T | T | F | F |    T    |      F      |        T          |
| T | T | F | T |    T    |      F      |        T          |
| T | T | T | F |    T    |      T      |        F          |
| T | T | T | T |    T    |      T      |        T          |

e. $(p ∧ r ∧ s) ↔ (p ∨ q)$
correct
|$p$|$q$|$r$|$s$|$(p ∧ r ∧ s)$|$(p ∨ q)$|$(p ∧ r ∧ s) ↔ (p ∨ q)$|
|:-:|:-:|:-:|:-:|:-----------:|:-------:|:----------------------:|
| F | F | F | F |      F      |    F    |            T           |
| F | F | F | T |      F      |    F    |            T           |
| F | F | T | F |      F      |    F    |            T           |
| F | F | T | T |      F      |    F    |            T           |
| F | T | F | F |      F      |    T    |            F           |
| F | T | F | T |      F      |    T    |            F           |
| F | T | T | F |      F      |    T    |            F           |
| F | T | T | T |      F      |    T    |            F           |
| T | F | F | F |      F      |    T    |            F           |
| T | F | F | T |      F      |    T    |            F           |
| T | F | T | F |      F      |    T    |            F           |
| T | F | T | T |      T      |    T    |            T           |
| T | T | F | F |      F      |    T    |            F           |
| T | T | F | T |      F      |    T    |            F           |
| T | T | T | F |      F      |    T    |            F           |
| T | T | T | T |      T      |    T    |            T           |

## q5

a. correct  
p = Smartphone B RAM > Smartphone A RAM  
q = Smartphone B RAM > Smartphone C RAM  
$p ∧ q = T$

b. correct  
p = Smartphone C ROM > Smartphone B ROM  
q = Smartphone C Camera Resolution > Smartphone B Camera Resolution  
$p ∨ q = T$

c. correct  
p = Smartphone B RAM > Smartphone A RAM   
q = Smartphone B ROM > Smartphone A ROM   
r = Smartphone B Camera Resolution > Smartphone A Camera Resolution  
$p ∧ q ∧ r = F$

d. correct  
p = Smartphone B RAM > Smartphone C RAM   
q = Smartphone B ROM > Smartphone C ROM   
r = Smartphone B Camera Resolution > Smartphone C Camera Resolution  
$(p ∧ q) → r = F$

e. correct  
p = Smartphone A Camera Resolution > Smartphone B Camera Resolution  
q = Smartphone A Camera Resolution > Smartphone C Camera Resolution  
r = Smartphone A RAM > Smartphone B RAM  
s = Smartphone A RAM > Smartphone C RAM  
$(p ∧ q) → (r ∧ s) = F$

## q6

a. correct, is an example of commutative law  
$p ∨ q ≡ q ∨ p$  
sentance is true as truth tables are identical  

|$p$|$q$|$p ∨ q$|$q ∨ p$|
|:-:|:-:|:-----:|:-----:|
| F | F |   F   |   F   |
| F | T |   T   |   T   |
| T | F |   T   |   T   |
| T | T |   T   |   T   |

b. correct. Cannot use laws since laws are for and or nto only  
$p ↔ q ≡ ¬(p → q) ∧ (¬q → p)$  
sentance is not correct. This is because the truth tables for $p ↔ q$ and $¬(p → q) ∧ (¬q → p)$ are not identical  

|$p$|$q$|$¬q$|$p ↔ q$|$¬(p → q)$|$(¬q → p)$|$¬(p → q) ∧ (¬q → p)$|
|:-:|:-:|:--:|:-----:|:--------:|:--------:|:-------------------:|
| F | F | T  |   T   |    F     |    T     |          F          |
| F | T | F  |   F   |    F     |    F     |          F          |
| T | F | T  |   F   |    T     |    T     |          T          |
| T | T | F  |   T   |    F     |    T     |          F          |


c. correct, no law as is implication  
$p ∨ q ≡ ¬p → q$  
sentance is true as truth tables are identical  

|$p$|$q$|$¬p$|$p ∨ q$|$¬p → q$|
|:-:|:-:|:--:|:-----:|:------:|
| F | F | T  |   F   |   F    |
| F | T | T  |   T   |   T    |
| T | F | F  |   T   |   T    |
| T | T | F  |   T   |   T    |

## q7

correct

p = customer’s insurance premium payment DOES arrive by the deadline  
q = email reminder is sent  

original sentance = when $¬p$, $q$  
= $¬p → q$  

**Converse** : swap left and right hand sides  
**Contrapositive** : swap left and right hand sides, NOT both sides  
**Inverse** : NOT both sides  

Therefore:  
Converse: $q → ¬p$  
When an email reminder is sent, customer’s insurance premium payment did not arrive by the deadline.  
Ans: if sent, then payment did not arrive on time

Contrapositive: $¬q → p$  
When an email reminder is not sent, customer’s insurance premium payment did arrive by the deadline.  
Ans: If not sent, payment arrive on time

Inverse: $p → ¬q$
When customer’s insurance premium payment DOES arrive by the deadline, an email reminder is not sent  
Ans: If payment arrives on time, then email not sent

## q8

correct

$¬q ∧ (p → q) → ¬p$  

|$p$|$q$|$¬p$|$¬q$|$(p → q)$|$¬q ∧ (p → q)$|$¬q ∧ (p → q) → ¬p$|
|:-:|:-:|:--:|:--:|:-------:|:------------:|:-----------------:|
| F | F | T  | T  |    T    |      T       |         T         |
| F | T | T  | F  |    T    |      F       |         T         |
| T | F | F  | T  |    F    |      F       |         T         |
| T | T | F  | F  |    T    |      F       |         T         |

Since the Truth Table of $¬q ∧ (p → q) → ¬p$ is all True, $¬q ∧ (p → q) → ¬p$ is a Tautology  

# Tutorial 5

## q1
|Predicate|True/False/Nether|Explanation|
|:-------:|:---------------:|:---------:|
|a. ¬𝑃𝑟𝑖𝑚𝑒(10) ∨ 𝐼𝑛(10,5,20)|True|¬𝑃𝑟𝑖𝑚𝑒(10) = True, True ∨ anything = True|
|b. ∃𝑛𝑃𝑟𝑖𝑚𝑒(𝑛)|True|Domain given and Prime(2) = True|
|c. ∃𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛)|True|Domain given and ¬Prime(4) = True|
|d. ∀𝑛𝑃𝑟𝑖𝑚𝑒(𝑛)|False|Domain given but Prime(4) = False|
|e. ∀𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛)|False|Domain given but ¬Prime(2) = False|
|f. ¬∀𝑛𝑃𝑟𝑖𝑚𝑒(𝑛)|True|Domain given and $¬∀n\ Prime(n) \equiv ∃n(¬Prime(n))$, ∃𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛) proven true in part c.|
|g. ∀𝑛(𝐼𝑛(𝑛, 1,3) → 𝑃𝑟𝑖𝑚𝑒(𝑛))|True|Domain Given, when n!=2, 𝐼𝑛(𝑛, 1,3) = false, 𝐼𝑛(𝑛, 1,3) → 𝑃𝑟𝑖𝑚𝑒(𝑛) = true. When n = 2, 𝐼𝑛(𝑛, 1,3) = true an 𝑃𝑟𝑖𝑚𝑒(𝑛) = true.|
|h. ∀𝑛(𝐼𝑛(𝑛, 8,10) → 𝑃𝑟𝑖𝑚𝑒(𝑛))|False|Domain given but when n=9, 𝐼𝑛(𝑛, 8,10) =True but 𝑃𝑟𝑖𝑚𝑒(𝑛) = False, thus 𝐼𝑛(𝑛, 8,10) → 𝑃𝑟𝑖𝑚𝑒(𝑛) = False|
|i. ∀𝑛(𝐼𝑛(𝑛, 𝑎, 𝑏) → ¬𝑃𝑟𝑖𝑚𝑒(𝑛)), Where 𝑎 and 𝑏 are integer smaller than 10|||
||||