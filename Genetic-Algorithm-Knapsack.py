import random

weights=[1,2,1,9]
values=[5,4,7,2]

#ظرفیت کوله پشتی
capacity=15

#تعداد کرومزم های جمعیت
populatin_size=6
 #ایجاد جعیت اولیه
population=[]

for i in range(populatin_size):
   chromosome =[]

   for j in range(4):
  
        gene=random.randint(0,1)
        chromosome.append(gene)
        
   population.append(chromosome)

print("جمعیت اولیه:")
for chromosome in population:
  print(chromosome)

#فیتنس
def fitness(chromosome):
   total_weight=0
   total_value=0

   for i in range(4):
      if chromosome[i]==1:
          total_weight+=weights[i]
          total_value+=values[i]

   if total_weight <= capacity:
      return total_value
   else:
      return 0
         
for chromosome in population:
   print(chromosome,"fitness:",fitness(chromosome))

#انتخاب والد با روش تورنومنت
def tornoment():
   parent1=random.sample(population,2)
   fit1=fitness(parent1[0])
   fit2=fitness(parent1[1])

   if fit1>fit2:
      return parent1[0]
   elif fit1<fit2:
      return parent1[1]
   else:
      return random.choice(parent1)   
   

#انتخاب دو والد
parent1=tornoment()
parent2=tornoment()

print("والد اول:",parent1)
print("والد دوم:",parent2)


#ترکیب دو والد
def crossover(parent1,parent2):
   point=2

   child1=parent1[:point]+parent2[point:]
   child2=parent2[:point]+parent1[point:]

   return child1,child2

#تولید دو فرزند
child1,child2=crossover(parent1,parent2)
print("فرزنداول:",child1)
print("فرزند دوم:",child2)

#جهش
def jahesh(child):
     index=random.randint(0,3)
     if child[index]==0:
        child[index]=1
     else:
       child[index]=0

     return child
child1=jahesh(child1)
child2=jahesh(child2)


print("جهش فرزند اول:",child1)
print("جهش فرزند دوم:",child2)

#تعداد نسل ها 
generation=50

for generation in range(generation):
   new_population=[]

   #پیدا کردن بهترین کروموزوم نسل فعلی
   best=max(population,key=fitness)
   #انتقال بهارین کروموزوم به نسل بعد
   new_population.append(best.copy())

   
   while len(new_population)<populatin_size:
      parent1=tornoment()
      parent2=tornoment()

      child1,child2=crossover(parent1,parent2)
      child1=jahesh(child1)
      child2=jahesh(child2)

      new_population.append(child1)
      new_population.append(child2)

   population=new_population[:populatin_size]
   best=max(population,key=fitness)

   print("",generation+1)
   print("",best)
   print("",fitness(best))

   #پیدا کردن بهترین جواب نهایی
   best=max(population,key=fitness)

   total_weight=0
   total_value=0

   for i in range(4):
      if best[i]==1:
         total_weight+=weights[i]
         total_value+=values[i]

print("\nبهترین جواب نهایی:")
print("کروموزوم:", best)
print("وزن کل:", total_weight)
print("ارزش کل:", total_value)
print("Fitness:", fitness(best))        