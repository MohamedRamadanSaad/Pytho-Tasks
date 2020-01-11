__author__ = 'Mohamed_Ramadan_PC'
f1 =open('E:\\healthy.txt','r+')
f2 =open('E:\\unhealthy.txt','r+')
f3=open('E:\\NoOfHealthy.txt','r+')
f4=open('E:\\NoOfUnHealthy.txt','r+')

def learn(food,sort):
      TheMeal=food.split(" ")

      for meal in TheMeal:
         if sort==1:
            f1.write(meal+" ")
            x=+1
         else :
            f2.write(meal+" ")



def predict(meal,laplace):
  f1 =open('E:\\healthy.txt','r+')
  f2 =open('E:\\unhealthy.txt','r+')
  t1=f1.read()
  healthy_length=t1.split(" ")
  t2=f2.read()
  unhealthy_length=t2.split(" ")
  f3.write('{}'.format(len(healthy_length)-1))
  f4.write('{}'.format(len(unhealthy_length)-1))
  healthy_counter=len(healthy_length)-1
  unhealthy_counter=len(unhealthy_length)-1
  all_food=healthy_counter + unhealthy_counter
  p_h=(healthy_counter+laplace)/(all_food*1.0+laplace*2)
  p_unh=(unhealthy_counter+laplace)/(all_food*1.0+laplace*2)
  print("total foods= {}".format(all_food))
  print("Healthy foods= {}".format(healthy_counter))
  print("Un-Healthy foods= {}".format(unhealthy_counter))
  print("p_h= {}".format(p_h))
  print("p_unh= {}".format(p_unh))
  print("Healthy words= {}".format(healthy_length))
  print("Un-healthy words= {}".format(unhealthy_length))
  meals=meal.split(" ")
  p_f_h=0.1
  p_f_unh=0.1

  for food in meals:
    if food in healthy_length:
       p_f_unh*=(1*1.0+laplace)/(unhealthy_counter+laplace*all_food)
    else :

       p_f_h*=(1*1.0+laplace)/(healthy_counter+laplace*all_food)
  print("p_f_h= {}".format(p_f_h))
  print("p_f_unh= {}".format(p_f_unh))

  p_h_f=(p_h*p_f_h)/(p_f_h*p_h+p_f_unh*p_unh)
  p_unh_f=(p_unh*p_f_unh)/(p_f_h*p_h+p_f_unh*p_unh)
  print("p_h_f= {}".format(p_h_f))
  print("p_unh_f= {}".format(p_unh_f))

  if(p_h_f>p_unh_f):
      print("This meal is  Classified as Healthy meal ")
  else :
       print("This meal is  Classified as Un-Healthy meal ")




learn("tomato",1)
learn("vegetable",1)
learn("Bread rice macaron cream_chante",0)
learn("tost",1)

f1.close()
f2.close()
predict("rice vegetable tomato",1)
