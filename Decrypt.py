filee = input("Enter File to Decrypt: ")
mess = print("Enter the corresponding for each letter.")
a = input("a: ")
b = input("b: ")
c = input("c: ")
d = input("d: ")
e = input("e: ")
f = input("f: ")
g = input("g: ")
h = input("h: ")
i = input("i: ")
j = input("j: ")
k = input("k: ")
l = input("l: ")
m = input("m: ")
n = input("n: ")
o = input("o: ")
p = input("p: ")
q = input("q: ")
r = input("r: ")
s = input("s: ")
t = input("t: ")
u = input("u: ")
v = input("v: ")
w = input("w: ")
x = input("x: ")
y = input("y: ")
z = input("z: ")
print("Your key is:")
print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
cont = input("Your file will now be decrypted, continue? ")
enc = False
if cont.lower() == "no":
    enc = False
else:
    enc = True
if enc:
    with open(filee,"r") as thefile:
        foo = thefile.read()
    foo = foo.replace(u,"1")
    foo = foo.replace(y,"2")
    foo = foo.replace(t,"3")
    foo = foo.replace(b,"4")
    foo = foo.replace(d,"5")
    foo = foo.replace(i,"6")
    foo = foo.replace(c,"7")
    foo = foo.replace(l,"8")
    foo = foo.replace(a,"9")
    foo = foo.replace(a.upper(),"a")
    foo = foo.replace(b.upper(),"b")
    foo = foo.replace(c.upper(),"c")
    foo = foo.replace(d.upper(),"d")
    foo = foo.replace(e.upper(),"e")
    foo = foo.replace(f.upper(),"f")
    foo = foo.replace(g.upper(),"g")
    foo = foo.replace(h.upper(),"h")
    foo = foo.replace(i.upper(),"i")
    foo = foo.replace(j.upper(),"j")
    foo = foo.replace(k.upper(),"k")
    foo = foo.replace(l.upper(),"l")
    foo = foo.replace(m.upper(),"m")
    foo = foo.replace(n.upper(),"n")
    foo = foo.replace(o.upper(),"o")
    foo = foo.replace(p.upper(),"p")
    foo = foo.replace(q.upper(),"q")
    foo = foo.replace(r.upper(),"r")
    foo = foo.replace(s.upper(),"s")
    foo = foo.replace(t.upper(),"t")
    foo = foo.replace(u.upper(),"u")
    foo = foo.replace(v.upper(),"v")
    foo = foo.replace(w.upper(),"w")
    foo = foo.replace(x.upper(),"x")
    foo = foo.replace(y.upper(),"y")
    foo = foo.replace(z.upper(),"z")
    foo = foo.replace("8","0")
    foo = foo.replace("+","!")
    foo = foo.replace("&","?")
    foo = foo.replace("*",".")
    foo = foo.replace("#",":")
    foo = foo.replace("}",";")
    foo = foo.replace("=","-")
    foo = foo.replace("!","@")
    with open(filee,"w") as thefile:
        thefile.write(foo)
