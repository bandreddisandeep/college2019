s=input()
l=len(s)
i=1
wl=int(((l*3)-3)/2)
wr=wl
w=".|."
while i!=l:
    print("-"*wl  +  w*i  +  "-"*wr)
    wl=wl-3
    wr=wr-3
    i=i+2
if(i==l):
    print("-"*i  +  s  +  "-"*i)
    wl=wl+3
    wr=wr+3
    i=i-2
    while(i>0):
        print("-"*wl  +  w*i  +  "-"*wr)
        wl=wl+3
        wr=wr+3
        i=i-2