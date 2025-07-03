
N= int(input())
info= []
for i in range(N):
  train= input().strip()
  name,other= train.split(" will departure for ")
  destiny,time=other.split(" at ")
  info.append([name,destiny,time])

for i in range(1,N):
  current= info[i]
  current_name= current[0]
  current_time= current[2]
  current_hours, current_minutes = map(int, current_time.split(':'))
  current_depart= current_hours * 60 + current_minutes

  j= i-1
  while j>=0:
    prev= info[j]
    prev_name= prev[0]
    prev_time= prev[2]
    prev_hours, prev_minutes= map(int, prev_time.split(':'))
    prev_depart= prev_hours * 60 + prev_minutes

    if (current_name < prev_name) or (current_name == prev_name and current_depart > prev_depart):
      info[j+1]= info[j]
      j-=1
    else:
      break

  info[j + 1] = current


for i in info:
    print(f"{i[0]} will departure for {i[1]} at {i[2]}")