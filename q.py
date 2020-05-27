from vpython import *
import time
import numpy as np
import math

##config
width = 1.27
length = 2.54
gravity = 9.81
size = 0.0525/2
mass = 0.17
dt = 1/60
time = 0
minlimit = 0.0000001
ball_coeff_of_restitution = 1
e = 0.8
uk = 0.08

#ball_recon config
ball_recon_size = 0.01

#hole_config
side_hole_size = 0.1143/2
middle_hole_size = 0.127/2

scene = canvas(title="Projectile", width=800, height=580, x=0, y=0,z = 0, center=vec(width/2, 0.1, length/2), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(width/2, -0.001, length/2), size=vec(width, 0.002, length), texture=textures.metal)

ball =  [sphere(pos=vec(0.45,size,0.4),         radius=size, color=color.white,     v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.09,size,2.1),            radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.3,size,0.6),          radius=size, color=color.red,       v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.1,size,length/2),      radius=size, color=color.green,     v=vec(0, 0,0),      a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.7,size,length/2+size), radius=size, color=color.purple,    v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.15,size,2.2),          radius=size, color=color.orange,    v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.19,size,2),            radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.69,size,2),            radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.89,size,2),            radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.9,size,0.8),           radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.99,size,2),            radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(1.09,size,2),            radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(1.0,size,0.08),          radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.05,size,0.87),         radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.09,size,0.6),          radius=size, color=color.blue,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0)),
        sphere(pos=vec(0.8,size,length/2-size), radius=size, color=color.cyan,      v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0))]

ball_recon = [sphere(pos=vec(ball[0].pos.x + size, 0.03, ball[0].pos.z),    radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[1].pos.x + size, 0.03, ball[1].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[2].pos.x + size, 0.03, ball[2].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[3].pos.x + size, 0.03, ball[3].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[4].pos.x + size, 0.03, ball[4].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[5].pos.x + size, 0.03, ball[5].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[6].pos.x + size, 0.03, ball[6].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[7].pos.x + size, 0.03, ball[7].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[8].pos.x + size, 0.03, ball[8].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[9].pos.x + size, 0.03, ball[9].pos.z),      radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[10].pos.x + size, 0.03, ball[10].pos.z),    radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[11].pos.x + size, 0.03, ball[11].pos.z),    radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[12].pos.x + size, 0.03, ball[12].pos.z),    radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[13].pos.x + size, 0.03, ball[13].pos.z),    radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[14].pos.x + size, 0.03, ball[14].pos.z),    radius=ball_recon_size, color=color.yellow),
            sphere(pos=vec(ball[15].pos.x + size, 0.03, ball[15].pos.z),    radius=ball_recon_size, color=color.yellow)]

er = sphere(pos=vec(0,0,0),         radius=size, color=color.white,     v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0))
wer = sphere(pos=vec(1,0,0),         radius=size, color=color.white,     v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0))
ser = sphere(pos=vec(0,0,1),         radius=size, color=color.white,     v=vec(0, 0, 0),     a=vec(0, 0, 0), vv=0, w = vec(0, 0, 0))

gd = graph(title="energy", width=800, height=450, x=0, y=600, xtitle="time(s)", ytitle="Q(J)")
xt = gcurve(graph=gd, color=color.red)

class start:
    def __init__(self):
        return

    def get_p(self):
        print("Please Input The Impulse of the firstball!!!")
        print("if p = (2, 0, 3), please input 2 0 3")
        q = input("p = ")
        num = q.split()
        p = vec(float(num[0]), float(num[1]), float(num[2]))
        ball[0].v = p / mass
        return
    
    def restart(self):
        for i in range(len(ball)):
            ball[i].v = vec(0, 0, 0)
            ball[i].w = vec(0, 0, 0)
        return

st = start() 

class rotation:
    def __init__(self):
        print("rotation start")

    def roll_ball(self, i, j):
        p1 = mass * ( dot((ball[i].v - ball[j].v), (ball[i].pos - ball[j].pos)) / (ball[i].pos - ball[j].pos).mag ) * (1 + e)
        r1 = (ball[i].pos + ball[j].pos) / 2 - ball[i].pos
        p2 = mass * ( dot((ball[i].v - ball[j].v), (ball[i].pos - ball[j].pos)) / (ball[i].pos - ball[j].pos).mag ) * (1 + e)
        r2 = (ball[i].pos + ball[j].pos) / 2 - ball[j].pos
        
        pfk1 = 0
        pfk2 = 0
        if ball[i].w.mag == 0 and ball[j].w.mag == 0:
            return

        elif dot(ball[i].w, ball[j].w) < 0 and ball[i].w.mag > ball[j].w.mag:
            pfk1 = p1 * -1 * (ball[i].w - ball[j].w) / (ball[i].w - ball[j].w).mag
            pfk2 = p2 * -1 * (ball[j].w - ball[i].w) / (ball[j].w - ball[i].w).mag

        elif dot(ball[i].w, ball[j].w) < 0 and ball[i].w.mag < ball[j].w.mag:
            pfk1 = p1 * -1 * (ball[i].w - ball[j].w) / (ball[i].w - ball[j].w).mag
            pfk2 = p2 * -1 * (ball[j].w - ball[i].w) / (ball[j].w - ball[i].w).mag

        elif dot(ball[i].w, ball[j].w) < 0 and ball[i].w.mag == ball[j].w.mag:
            pfk1 = p1 * -1 * (ball[i].w - ball[j].w) / (ball[i].w - ball[j].w).mag
            pfk2 = p2 * -1 * (ball[j].w - ball[i].w) / (ball[j].w - ball[i].w).mag

        elif dot(ball[i].w, ball[j].w) >= 0:
            pfk1 = p1 * -1 * (ball[i].w + ball[j].w) / (ball[i].w + ball[j].w).mag
            pfk2 = p2 * -1 * (ball[j].w + ball[i].w) / (ball[j].w + ball[i].w).mag

        w1 = ball[i].w + 5 * uk / (2 * mass * size * size) * cross(r1, pfk1)
        w2 = ball[j].w + 5 * uk / (2 * mass * size * size) * cross(r2, pfk2)

        ball[i].w = w1
        ball[j].w = w2

        return
    
    def line_ball_ro_update(self, i, wall):
        if wall == 1:
            r = vec(-1 * size, 0, 0)
            vv = vec(ball[i].v.x, 0, 0)   #|_ 90deg
            vp = vec(0, 0, ball[i].v.z)
            p = -1 * mass * vv.mag * (1 + e) * (vp + cross(r, ball[i].w)) / (vp + cross(r, ball[i].w)).mag
            w = ball[i].w + 5 * cross(r, p) * uk / (2 * mass * size * size)
            ball[i].w = w
            print(p)
            print(w)

        elif wall == 2:
            r = vec(0, 0, -1 * size)
            vv = vec(0, 0, ball[i].v.z)   #|_ 90deg
            vp = vec(ball[i].v.x, 0, 0)
            p = -1 * mass * vv.mag * (1 + e) * (vp + cross(r, ball[i].w)) / (vp + cross(r, ball[i].w)).mag
            w = ball[i].w + 5 * cross(r, p) * uk / (2 * mass * size * size)
            ball[i].w = w
            print(p)
            print(w)            

        elif wall == 3:
            r = vec(size, 0, 0)
            vv = vec(ball[i].v.x, 0, 0)   #|_ 90deg
            vp = vec(0, 0, ball[i].v.z)
            p = -1 * mass * vv.mag * (1 + e) * (vp + cross(r, ball[i].w)) / (vp + cross(r, ball[i].w)).mag
            w = ball[i].w + 5 * cross(r, p) * uk / (2 * mass * size * size)
            ball[i].w = w
            print(p)
            print(w) 

        elif wall == 4:
            r = vec(0, 0, size)
            vv = vec(0, 0, ball[i].v.z)   #|_ 90deg
            vp = vec(ball[i].v.x, 0, 0)
            p = -1 * mass * vv.mag * (1 + e) * (vp + cross(r, ball[i].w)) / (vp + cross(r, ball[i].w)).mag
            w = ball[i].w + 5 * cross(r, p) * uk / (2 * mass * size * size)
            ball[i].w = w
            print(p)
            print(w) 
        print("dkjfo")
        return

ro = rotation()

class collision:
    def __init__(self):
        print("collision start")

    def checkdeg(self, z, x):
        if abs(z) <= minlimit and x >=0:
            return 0
        elif abs(z) <= minlimit and x < 0:
            return math.pi
        elif abs(x) <= minlimit and z >= 0:
            return math.pi / 2
        elif abs(x) <= minlimit and z < 0:
            return math.pi * 3 / 2

        angle_cal = math.asin( abs( z ) / math.sqrt( z ** 2 + x ** 2 ) )

        if z > 0 and x > 0:
            return angle_cal
        elif z > 0 and x < 0:
            return math.pi - angle_cal
        elif z < 0 and x < 0:
            return math.pi + angle_cal
        elif z < 0 and x > 0:
            return 2 * math.pi - angle_cal
        return

    def separate(self, i,j):
        mid = (ball[i].pos + ball[j].pos) / 2
        vec1 = ball[i].pos - mid
        vec2 = ball[j].pos - mid
        angle1 = self.checkdeg(vec1.z,vec1.x)
        angle2 = self.checkdeg(vec2.z,vec2.x)
        ball[i].pos.x = mid.x + size * math.cos(angle1)
        ball[i].pos.z = mid.z + size * math.sin(angle1)
        ball[j].pos.x = mid.x + size * math.cos(angle2)
        ball[j].pos.z = mid.z + size * math.sin(angle2)
        return

    def line_separate(self, i, wall):
        if wall == 1:
            ball[i].pos = vec(size, ball[i].pos.y, ball[i].pos.z)
        if wall == 2:
            ball[i].pos = vec(ball[i].pos.x, ball[i].pos.y, size)
        if wall == 3:
            ball[i].pos = vec(width - size, ball[i].pos.y, ball[i].pos.z)
        if wall == 4:
            ball[i].pos = vec(ball[i].pos.x, ball[i].pos.y, length - size)

    def line_ball_collision(self, i, wall):
        if wall == 1:
            vp = vec(0, 0, ball[i].v.z)
            vv = vec(ball[i].v.x, 0, 0)    # |_ 90deg
            p = -1 * mass * vv * (1 + e)

            vp = vp - p.mag * uk / mass * vp / vp.mag
            ball[i].v.z = vp.z
            ball[i].v.x = (p / (1 + e) * e / mass).x
            return

        elif wall == 2:
            vp = vec(ball[i].v.x, 0, 0)
            vv = vec(0, 0, ball[i].v.z)    # |_ 90deg
            p = -1 * mass * vv * (1 + e)

            vp = vp - p.mag * uk / mass * vp / vp.mag
            ball[i].v.x = vp.x
            ball[i].v.z = (p / (1 + e) * e / mass).z
            return

        elif wall == 3:
            vp = vec(0, 0, ball[i].v.z)
            vv = vec(ball[i].v.x, 0, 0)    # |_ 90deg
            p = -1 * mass * vv * (1 + e)

            vp = vp - p.mag * uk / mass * vp / vp.mag
            ball[i].v.z = vp.z
            ball[i].v.x = (p / (1 + e) * e / mass).x
            return

        elif wall == 4:
            vp = vec(ball[i].v.x, 0, 0)
            vv = vec(0, 0, ball[i].v.z)    # |_ 90deg
            p = -1 * mass * vv * (1 + e)

            vp = vp - p.mag * uk / mass * vp / vp.mag
            ball[i].v.x = vp.x
            ball[i].v.z = (p / (1 + e) * e / mass).z

        return
    
    def line_ball_check(self, i):
        if ball[i].pos.x >= width - size:
            self.line_separate(i, 3)
            ro.line_ball_ro_update(i, 3)
            self.line_ball_collision(i, 3)

        if ball[i].pos.x <= size:
            self.line_separate(i, 1)
            ro.line_ball_ro_update(i, 1)
            self.line_ball_collision(i, 1)
            

        if ball[i].pos.z >= length - size:
            self.line_separate(i, 4)
            ro.line_ball_ro_update(i, 4)
            self.line_ball_collision(i, 4)
            

        if ball[i].pos.z <= size:
            self.line_separate(i, 2)
            ro.line_ball_ro_update(i, 2)
            self.line_ball_collision(i, 2)
            
        return

    def ball_collision(self, i, j):
        v1 = ball[i].v - dot((ball[i].v - ball[j].v), (ball[i].pos  - ball[j].pos)) / (ball[i].pos - ball[j].pos).mag2 * (ball[i].pos - ball[j].pos)
        v2 = ball[j].v - dot((ball[j].v - ball[i].v), (ball[j].pos  - ball[i].pos)) / (ball[j].pos - ball[i].pos).mag2 * (ball[j].pos - ball[i].pos)
        ball[i].v = v1
        ball[j].v = v2
        return

    def ball_collision_check(self, i, j):
        if(dot((ball[i].pos - ball[j].pos),(ball[i].v - ball[j].v))<=0 and mag(ball[i].pos - ball[j].pos) <= 2 * size):
            self.separate(i, j)
            ro.roll_ball(i, j)
            self.ball_collision(i, j)
        return
 
col = collision()

class vgraph:
    def __init__(self):
        xt.plot(pos = (time, 0))

    def energytol(self):
        q=0
        for i in range(16):
            ball[i].pos += ball[i].v * dt
            q += 1/2 * mass * ball[i].v.mag2
        xt.plot(pos = (time, q))

    def position(self):
        for i in range(16):
            ball[i].pos += ball[i].v * dt
            ball_recon[i].pos = ball[i].pos + vec( size * math.sin(ball[i].w.y * time ), 0, size * math.cos(ball[i].w.y * time))
            
#col = collision()
gra = vgraph()
#ro = rotation()

class onetime():
    def __init__(self):
        return

    def v_check(self):
        allstop = True
        for i in range(len(ball)):
            if ball[i].v.mag < 0.0001:
                ball[i].v = vec(0, 0, 0)
            else:
                allstop = False

        return allstop

    def check_stop(self):
        if self.v_check() == True:
            return True
        else:
            return False

    def one_start(self):
        st.get_p()
        while True:
            rate(1/dt)

            global time 
            time += dt

            for i in range(16):
                
                col.line_ball_check(i)

                for j in range(i,16):
                    if i==j:
                        continue

                    col.ball_collision_check(i, j)

            gra.energytol()
            gra.position()
            if self.check_stop() == True:
                st.restart()
                break
        
        return
one = onetime()

while True:
    one.one_start()
