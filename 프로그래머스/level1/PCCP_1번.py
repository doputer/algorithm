def solution(bandage, health, attacks):
    time = 0
    hp = health
    heal_time = 0
    turn = 0

    while time <= attacks[-1][0]:
        if time == attacks[turn][0]:
            heal_time = 0
            hp -= attacks[turn][1]
            turn += 1

            if hp <= 0:
                return -1
        else:
            hp += bandage[1]
            heal_time += 1

            if heal_time == bandage[0]:
                hp += bandage[2]
                heal_time = 0

            if hp > health:
                hp = health

        time += 1

    return hp
