import math
nodemem=128
nodecpu=8
nodenum=3
sysmem=(nodemem-6)*nodenum
syscpu=(nodecpu-1)*nodenum
podmem=2
podcpu=0.4
podnum=min(sysmem//podmem,syscpu//podcpu)
print("本集群支持最大pod数量为：",podnum)