#Calculate the best shipping method based on preset values 
def cost_ground_shipping(weight):
  flat_charge=20
  if weight<=2:
    return 1.50*weight+flat_charge
  elif weight>2 and weight<=6:
    return 3.00*weight+flat_charge
  elif weight>6 and weight<=10:
    return 4.00*weight+flat_charge
  elif weight>10:
    return 4.75*weight+flat_charge

premium_ground_shipping=125

def cost_drone_shipping(weight):
  if weight<=2:
    return 4.50*weight
  elif weight>2 and weight<=6:
    return 9.00*weight
  elif weight>6 and weight<=10:
    return 12.00*weight
  elif weight>10:
    return 14.25*weight

def best_method(weight):
  if cost_ground_shipping(weight)<premium_ground_shipping and cost_ground_shipping(weight)<cost_drone_shipping(weight):
    return "Ground Shipping is the cheapest method. The total cost would be " +str(cost_ground_shipping(weight))+"."
  elif premium_ground_shipping<cost_ground_shipping(weight) and premium_ground_shipping<cost_drone_shipping(weight):
    return "Premium Ground Shipping is the cheapest method. The cost would be "+str(premium_ground_shipping)+"."
  elif cost_drone_shipping(weight)<cost_ground_shipping(weight) and cost_drone_shipping(weight)<premium_ground_shipping:
    return "Drone Shipping is the cheapest method. The cost would be "+str(cost_drone_shipping(weight))+"."

print(best_method(4.8))
print(best_method(41.5))
print(best_method(3))
