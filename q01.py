from pkg.modu import triangle_zhonxin

print("請輸入三角形的 3 個頂點坐標")
print("-"*30)
no1 = input("請輸入頂點 a 的座標 : ")
no2 = input("請輸入頂點 b 的座標 : ")
no3 = input("請輸入頂點 c 的座標 : ")

a = tuple(map(int, no1.split(',')))
b = tuple(map(int, no2.split(',')))
c = tuple(map(int, no3.split(',')))
print("-"*30)
print(f"此三角形的重心為：{triangle_zhonxin(a, b, c)}")
