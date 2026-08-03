A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
i = 9
J = 10
K = 11
L = 12
M = 13
N = 14
o = 15
P = 16
Q = 17
R = 18
S = 19
T = 20
U = 21
V = 22
W = 23
X = 24
Y = 25
Z = 26
x1 = 1
x2 = 2
x3 = 3
W1 = 1
W2 = 2
W3 = 3
W4 = 4
W5 = 5
W6 = 6
W7 = 7
W8 = 8
W9 = 9
t1 = 50
t2 = 50
t3 = 50
def yW1(x1,W1):
    return x1 * W1
def yW4(x2,W4):
    return x2 * W4
def yW7(x3,W7):
    return x3 * W7
yW1_val = yW1(x1,W1)
yW4_val = yW4(x2,W4)
yW7_val = yW7(x3,W7)
def y1(yW1_val,yW4_val,yW7_val):
    return yW1_val + yW4_val + yW7_val
y1_val = y1(yW1_val,yW4_val,yW7_val)
def yW2(x1,W2):
    return x1 * W2
def yW5(x2,W5):
    return x2 * W5
def yW8(x3,W8):
    return x3 * W8
yW2_val = yW2(x1,W2)
yW5_val = yW5(x2,W5)
yW8_val = yW8(x3,W8)
def y2(yW2_val,yW5_val,yW8_val):
    return yW2_val + yW5_val + yW8_val
y2_val = y2(yW2_val,yW5_val,yW8_val)
def yW3(x1,W3):
    return x1 * W3
def yW6(x2,W6):
    return x2 * W6
def yW9(x3,W9):
    return x3 * W9
yW3_val = yW3(x1,W3)
yW6_val = yW6(x2,W6)
yW9_val = yW9(x3,W9)
def y3(yW3_val,yW6_val,yW9_val):
    return yW3_val + yW6_val + yW9_val
y3_val = y3(yW3_val,yW6_val,yW9_val)
LR = 0.05
def L11(yW1_val,t1):
    return yW1_val - t1
L11_val = L11(yW1_val,t1)
def L21(L11_val,x1):
    return L11_val * x1
L21_val = L21(L11_val,x1)
def NW1(W1,LR,L21_val):
    return W1 - (LR * L21_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L11_val = L11(yW1_val,t1)
    L21_val = L21(L11_val,x1)
    NW1_val = NW1(W1,LR,L21_val)
    print('NW1=',NW1_val)
    W1 = NW1_val
   
def L12(yW2_val,t2):
    return yW2_val - t2
L12_val = L12(yW2_val,t2)
def L22(L12_val,x1):
    return L12_val * x1
L22_val = L22(L12_val,x1)
def NW2(W2,LR,L22_val):
    return W2 - (LR * L22_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L12_val = L12(yW2_val,t2)
    L22_val = L22(L12_val,x1)
    NW2_val = NW2(W2,LR,L22_val)
    print('NW2=',NW2_val)
    W2 = NW2_val
def L13(yW3_val,t3):
    return yW3_val - t3
L13_val = L13(yW3_val,t3)
def L23(L13_val,x1):
    return L13_val * x1
L23_val = L23(L13_val,x1)
def NW3(W3,LR,L23_val):
    return W3 - (LR * L23_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L13_val = L13(yW3_val,t3)
    L23_val = L23(L13_val,x1)
    NW3_val = NW3(W3,LR,L23_val)
    print('NW3=',NW3_val)
    W3 = NW3_val
   
def L14(yW4_val,t1):
    return yW4_val - t1
L14_val = L14(yW4_val,t1)
def L24(L14_val,x2):
    return L14_val * x2
L24_val = L24(L14_val,x2)
def NW4(W4,LR,L24_val):
    return W4 - (LR * L24_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L14_val = L14(yW4_val,t1)
    L24_val = L24(L14_val,x2)
    NW4_val = NW4(W4,LR,L24_val)
    print('NW4',NW4_val)
    W4 = NW4_val
def L15(yW5_val,t2):
    return yW5_val - t2
L15_val = L15(yW5_val,t2)
def L25(L15_val,x2):
    return L15_val * x2
L25_val = L25(L15_val,x2)
def NW5(W5,LR,L25_val):
    return W5 - (LR * L25_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L15_val = L15(yW5_val,t2)
    L25_val = L25(L15_val,x2)
    NW5_val = NW5(W5,LR,L25_val)
    print('NW5=',NW5_val)
    W5 = NW5_val
def L16(yW6_val,t3):
    return yW6_val - t3
L16_val = L16(yW6_val,t3)
def L26(L16_val,x2):
    return L16_val * x2
L26_val = L26(L16_val,x2)
def NW6(W6,LR,L26_val):
    return W6 - (LR * L26_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L16_val = L16(yW6_val,t3)
    L26_val = L26(L16_val,x2)
    NW6_val = NW6(W6,LR,L26_val)
    print('NW6=',NW6_val)
    W6 = NW6_val
def L17(yW7_val,t1):
    return yW7_val - t1
L17_val = L17(yW7_val,t1)
def L27(L17_val,x3):
    return L17_val * x3
L27_val = L27(L17_val,x3)
def NW7(W7,LR,L27_val):
    return W7 - (LR * L27_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L17_val = L17(yW7_val,t1)
    L27_val = L27(L17_val,x3)
    NW7_val = NW7(W7,LR,L27_val)
    print('NW7=',NW7_val)
    W7 = NW7_val
   
def L18(yW8_val,t2):
    return yW8_val - t2
L18_val = L18(yW8_val,t2)
def L28(L18_val,x3):
    return L18_val * x3
L28_val = L28(L18_val,x3)
def NW8(W8,LR,L28_val):
    return W8 - (LR * L28_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L18_val = L18(yW8_val,t2)
    L28_val = L28(L18_val,x3)
    NW8_val = NW8(W8,LR,L28_val)
    print('NW8=',NW8_val)
    W8 = NW8_val
   
def L19(yW9_val,t3):
    return yW9_val - t3
L19_val = L19(yW9_val,t3)
def L29(L19_val,x3):
    return L19_val * x3
L29_val = L29(L19_val,x3)
def NW9(W9,LR,L29_val):
    return W9 - (LR * L29_val)
for i in range(100):
    yW1_val = yW1(x1,W1)
    yW4_val = yW4(x2,W4)
    yW7_val = yW7(x3,W7)
    y1_val = y1(yW1_val,yW4_val,yW7_val)
    yW2_val = yW2(x1,W2)
    yW5_val = yW5(x2,W5)
    yW8_val = yW8(x3,W8)
    y2_val = y2(yW2_val,yW5_val,yW8_val)
    yW3_val = yW3(x1,W3)
    yW6_val = yW6(x2,W6)
    yW9_val = yW9(x3,W9)
    y3_val = y3(yW3_val,yW6_val,yW9_val)
    L19_val = L19(yW9_val,t3)
    L29_val = L29(L19_val,x3)
    NW9_val = NW9(W9,LR,L29_val)
    print('NW9=',NW9_val)
    W9 = NW9_val
    print('y1=',y1_val/3)
    print('y2=',y2_val/3)
    print('y3=',y3_val/3)
