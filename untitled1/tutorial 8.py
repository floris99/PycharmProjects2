def allowed_dating_age(my_age):
    girls_age = my_age/2+7
    return girls_age

floris_limit = allowed_dating_age(17)
print("floris can date girls" , floris_limit, 'or older')
