# tut1

2's complement trick
find last instance of 1, all 0 right of last instance of 1 remain as 0, flip all bits left of last instance 1 except MSB

e.g.:
|-|-|-|-|-|-|-|-|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|0|0|1|0|0|
|[1]|0|1|0|0|[1]|0|0|
|[1]|1|0|1|1|[1]|0|0| -- end

q1a

$\frac{2v}{8}$ step cus $2^3$

0, 0.5, 1.5, 1.75, 1.75

never hits max 2v.  
because need to keep 000 for 0V, no choice have to give up 2v  
considered boundary case

error
0.001, 0.011, 0.068, 0.053, 0.146

standard choice: $\frac{Vmax}{2^n}$  
if req to include Vmax: $\frac{Vmax}{(2^n -1)}$  
other possibility: 000 = midpoint of step between (0 and 0.25)

q1b

sum all absolute / num samples

max error is $\frac{(v/2^n)}{2}$ as max error is when voltage is exactly in middle of diff between step values

q1c

$\frac{(Vmax/2^10)}{2} = \frac{(2/2^10)}{2} = 0.97mV$

q1d  
increase ADC bits increase resolution but also increase overall file size


q2a  
120(dec) = 1000 0000  
NOTE need to delcare somehow that is a positive number. since by default is 2's complement  
e.g. 0 1000 0000 or 1000 000 (unsigned)

q2b  
by default is 2's complement  
neg representation 1010 1011 0001 0010 1110 1111 (bin)  
2's complement pos num: 1101 0100 1110 1101 0001 0001 (bin)

-5 565 713 (dec)

q2c  
164 (unsigned), -36 (sign magnitude), -91(1's complement), -92(2's complement)  (all dec)  
need declare which is which

q2d  
11 1011(sign-magnitude), 10 0100(1's complement), 10 0101(2's complement)  (all bin)  
need declare which is which

q2e  
9.375 

q2f  
0001 0100 0100.1111 (unsigned bin)

q2g  
0101 0011 1001. 0101 0111 (BCD)

q2h    
0 1000 0101 000 0000 0100 0000 0000 0000 (bin floating point)  
word ver: 42804000 (hex)


q2i  
C46A 0840(hex) = 1100 0100 0110 1010 0000 1000 0100 0000 (bin)  
[1][100 0100 0][110 1010 0000 1000 0100 0000]

[100 0100 0] = 136 raw value  
exponent bias: -127 = 9  
mantissa = 1.[110 1010 0000 1000 0100 0000]  
shift bits **right** (since is decoding) by exponent times  
1.110 1010 0000 1000 0100 0000 -> 1110 1010 00.00 1000 0100 0000  
936.12890625 (dec)  
rmbr add neg sign because sign bit is 1  
-936.12890625 (dec)

q3a  
89  = 0101 1001

27  = 0001 1011  
-27 = 1110 0100 +1 = 1110 0101

89-(27)
| | |     |$^2 ->^1$|$^2$|$^2$  |$^2 ->^1$|$^2$| |
|-|-|-----|:-------:|-----|-----|:-------:|----|-|
| |0|~~1~~|    0    |~~1~~|~~1~~|    0    |  0 |1|
|-|0|  0  |    0    |  1  |  1  |    0    |  1 |1|
| |0|  0  |    1    |  1  |  1  |    1    |  1 |0|
    
^^^ result ok

89+(-27)

|$^1$|$^1$| | | | | |$^1$| |
|----|----|-|-|-|-|-|----|-|
|    | 0  |1|0|1|1|0| 0  |1|
|  + | 1  |1|1|0|0|1| 0  |1|
| [1]| 0  |0|1|1|1|1| 1  |0|

^^^ incorrect as carry not shown

q3b
44 = 0010 1100  
-44 = 1101 0011 +1 = 1101 0100  
99 = 0110 0011  
-99 = 1001 1100 +1 = 1001 1101

-44 - (+99)
| |     |$^2$ |$^2$| | |     |$^2 ->^1$|$^2$|
|-|-----|-----|----|-|-|-----|:-------:|----|
| |~~1~~|~~1~~|  0 |1|0|~~1~~|    0    |  0 |
|-|  0  |  1  |  1 |0|0|  0  |    1    |  1 |
| |  0  |  1  |  1 |1|0|  0  |    0    |  1 |

^^^incorrect as is positive, overflow

-44 + (-99)
|$^1$| | |$^1$|$^1$| $^1$| | | |
|----|-|-|----|----|-----|-|-|-|
|    |1|1|  0 |  1 |  0  |1|0|0|
|  + |1|0|  0 |  1 |  1  |1|0|1|
| [1]|0|1|  1 |  1 |  0  |0|0|1|

^^^added extra 1, carry and overflow

q4
decimal x: 86, 126, 6, 0, -128
decimal y: 86, 3, -6, -8, -1
binary z: 1010 1100, 1000 0001, 0000 0000, 1111 1000, 0111 1111
decimal z: -86,-127, 0, -8, 127
overflow: yes,yes,no,no,yes