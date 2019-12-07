def water_plants(plants, capacity):
    n_plants = len(plants)
    n = 0
    def water_next(plants_left, n, n_plants, capacity, current_water):
        # debug
        print('plants left: {}, current_water: {}, n_steps: {}'.format(str(plants_left), current_water, n)) 
        # base return
        if plants_left == []:
            return n
        # reload water?
        if plants_left[0] > current_water:
            current_water = capacity
            n += (n_plants - len(plants_left))*2
        # base case
        current_water -= plants_left.pop(0)
        # ah shit... here we go again
        return water_next(plants_left, n+1, n_plants, capacity, current_water)
    n = water_next(plants, n, n_plants, capacity, capacity)
    return n

# test
plants = [2, 4, 5, 1, 2]
capacity = 6
print('test with plants: {} and capacity {}'.format(plants, capacity))
print('TOTAL STEPS: {}'.format(water_plants(plants,capacity)))
