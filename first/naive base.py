
data_struct= {
    "total_healthy_foods":0,      "total_unhealthy_foods":0,
    "total_healthy_meals":0,      "total_unhealthy_meals":0,
                     "meals_of_food":{}}

def learn (food,type):

    meals_of_food=data_struct['meals_of_food']
    meals=food.split(" ")

    for meal in meals:
        try:
            meals_of_food[meal][type]+=1
        except KeyError:
            meals_of_food[meal]=[1-type,type]

        data_struct["total_healthy_meals"]+=type
        data_struct["total_unhealthy_meals"]+=(1-type)

    data_struct["total_healthy_foods"]+=type
    data_struct["total_unhealthy_foods"]+=(1-type)

# K is laplacian smoother

def predict (food,K):

    meals_of_food=data_struct['meals_of_food']

    total_foods=data_struct["total_healthy_foods"]+data_struct["total_unhealthy_foods"]

    # A prior probability of Spam
    p_h=(data_struct["total_healthy_foods"]+K)/(total_foods*1.0+K*2)
    print("total foods= {}".format(total_foods))
    # A prior probability of ham

    p_unh=(data_struct["total_unhealthy_foods"]+K)/(total_foods*1.0+K*2)

    print("p_h= {}".format(p_h))
    print("p_unh= {}".format(p_unh))
    meals=food.split(" ")

    p_f_h=0.5
    p_f_unh=0.5

    for meal in meals:
        p_f_h*=(meals_of_food[meal][1]*1.0+K)/(data_struct["total_healthy_meals"]+K*len(meals_of_food))
        print(len(meals_of_food))
        print("total_healthy_meals= {}".format(data_struct["total_healthy_meals"]))


        p_f_unh*=(meals_of_food[meal][0]*1.0+K)/(data_struct["total_unhealthy_meals"]+K*len(meals_of_food))
        print("total_unhealthy_meals= {}".format(data_struct["total_unhealthy_meals"]))
    print("p_f_h= {}".format(p_f_h))
    print("p_f_unh= {}".format(p_f_unh))
    p_h_f=p_h*p_f_h/(p_f_h*p_h+p_f_unh*p_unh)
    p_unh_f=p_unh*p_f_unh/(p_f_h*p_h+p_f_unh*p_unh)

    if(p_h_f>p_unh_f):
        print("this food is classified as healthy food")
    else:
        print("this food is classified as unhealthy food")

learn("Fructose",1)
learn("vegetable",1)
learn("Bread rice pasta roasted_grain",0)



predict("Bread rice pasta vegetable Fructose ",1)






