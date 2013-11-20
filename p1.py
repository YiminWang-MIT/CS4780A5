import os
tp=[[0.05,0.1,0.15,0.7],[0.1,0.05,0.25,0.6],[0.45,0.15,0.05,0.35],[0.35,0.2,0.15,0.3]]
st=[0.1,0.4,0.2,0.3]
ep=[[0.4,0.2,0.1,0.2,0.1],[0.3,0.1,0.4,0.1,0.1],[0.1,0.1,0.1,0.2,0.5],[0.1,0.4,0.1,0.3,0.1]]

x=raw_input("Please enter the Greek word:")

dp=[[] for i in range(len(st))]
dpi=[[] for i in range(len(st))]

for i in range(len(x)):
  for j in range(len(st)):
    if i==0:
      dp[j].append(st[j]*ep[j][int(x[i])])
      dpi[j].append(-1)
    else:
      argmax=0
      index=-1
      for k in range(len(st)):
        tmppro=dp[k][i-1]*tp[k][j]*ep[j][int(x[i])]
        if tmppro>argmax: 
          argmax=tmppro
          index=k
      dp[j].append(argmax)
      dpi[j].append(index)

f=file("p1latex.out","w");
f.write("\\begin{tabular}{l | c r}\n")
f.write("  $\\delta$")
for k in range(len(x)):
  f.write(" & t=%d"%(k+1))
f.write(" \\\\\n  \\hline\n")
for j in range(len(st)):
  f.write("  s=%d"%(j+1))
  for k in range(len(x)):
    f.write(" & %0.5f, %d"%(dp[j][k],dpi[j][k]))
  f.write(" \\\\\n")
f.write("\\end{tabular}\n")
