import random

NUM_DOORS=3

def get_goat_door(doors, first_choice):
    for ind, door in enumerate(doors):
        if door != 1 and ind != first_choice:
            return ind
    raise "Failed to find door with no car"

# Note: This func kinda only works with 3 doors since if there were more it should randomly pick the remaining doors
def get_switched_ind(doors,goat_door,first_choice):
    for ind, door in enumerate(doors):
        if ind!= goat_door and ind != first_choice:
            return ind
    raise "Failed to get switched choice"

# returns first outcome (0 for fail 1 for success) and second outcome (0 for fail 1 for success) 
def test():
    car_pos=random.randint(0,NUM_DOORS-1)
    doors=[0]*3
    doors[car_pos]=1
    first_choice=random.randint(0,NUM_DOORS-1)
    goat_door = get_goat_door(doors, first_choice)
    switched_choice = get_switched_ind(doors, goat_door, first_choice)
    first_score=1 if first_choice==car_pos else 0
    switched_score=1 if switched_choice==car_pos else 0
    print(f"doors:{doors} first choice:{first_choice}, goat door:{goat_door},  switched choice:{switched_choice}, first score:{first_score}, switched_score:{switched_score}")
    return first_score, switched_score

def main():
    stay_wins=0
    switch_wins=0
    for i in range(0,1000):
        first_score, switched_score = test()
        stay_wins+=first_score
        switch_wins+= switched_score
        print(f"stay: {stay_wins}, switch: {switch_wins}")

if __name__ == "__main__":
    main()
