from cmath import pi
import os,sys,random

N = 10
NombresPairs = ()
NombresImpairs = ()

for k in range (N):
    nb = random.randint(0,15)
    if nb%2 ==0:
        NombresPairs +=(nb,)
    else:
        NombresImpairs +=(nb,)

print(sum(NombresImpairs)+sum(NombresPairs))

(dfr_p,dfw_p)=os.pipe()
(dfr_ip,dfw_ip)=os.pipe()
(dfr_rp,dfw_rp)=os.pipe()
(dfr_rip,dfw_rip)=os.pipe()

pid = os.fork()
pipe = ()
lenlst = len(NombresPairs)
pipe += (dfr_p,dfw_p)+(dfr_rp,dfw_rp)
if pid != 0:
    pid = os.fork()
    lenlst =len(NombresImpairs)
    pipe =()
    pipe += (dfr_ip,dfw_ip)+(dfr_rip,dfw_rip)

if pid ==0:
    os.close(pipe[1])
    lst = os.read(pipe[0],4*lenlst)
    os.close(pipe[0])
    lst = tuple(lst)
    s =sum(lst)
    os.close(pipe[2])
    os.write(pipe[3],bytes([s]))
    os.close(pipe[3])

else:
    os.close(dfr_p)
    os.write(dfw_p,bytes(NombresPairs))
    os.close(dfw_p)

    os.close(dfr_ip)
    os.write(dfw_ip,bytes(NombresImpairs))
    os.close(dfw_ip)

    os.close(dfw_rp)
    R1 = os.read(dfr_rp,4)
    os.close(dfr_rp)

    os.close(dfw_rip)
    R2 = os.read(dfr_rip,4)
    os.close(dfr_rip)

    res = list(R2)[0] + list(R1)[0]
    print(res)
sys.exit(0)