import random
import pandas as pd
import numpy as np
# グラフ可視化
import plotly.graph_objects as go
#~.iat[列,行]


def GA(party, evaluation_value):
    #初期化
    battle_point_me_sum0 = 0
    battle_point_me_sum1 = 0
    battle_point_me_sum2 = 0
    battle_point_me_sum3 = 0
    battle_point_me_sum4 = 0
    battle_point_me_sum5 = 0
    battle_point_me_sum6 = 0
    battle_point_me_sum7 = 0
    battle_point_me_sum8 = 0
    battle_point_me_sum9 = 0
    #評価関数
    for i in range(10):
        for j in range(9):
            if i==j:
                pass
            elif i!=j:
                print("\n")
                print("battle simulater")
                print(f"{i} vs {j}")
                me = party.iloc[i]
                enemy = party.iloc[j]
                print("[me party]")
                print(me)
                print(f"me.pokemon01: {me.pokemon01}")
                print(f"me.pokemon02: {me.pokemon02}")
                print(f"me.pokemon03: {me.pokemon03}")
                print("[enemy party]")
                print(enemy)
                print(f"enemy.pokemon01: {enemy.pokemon01}")
                print(f"enemy.pokemon02: {enemy.pokemon02}")
                print(f"enemy.pokemon03: {enemy.pokemon03}")
                #Battle Simulater
                #evaluation_value <-これを参照して点数の総和を代入
                #変数命名規則 number(me_pokemon_number)(enemy_pokemon_number)
                number11 = evaluation_value.iat[enemy.pokemon01, me.pokemon01]
                number12 = evaluation_value.iat[enemy.pokemon02, me.pokemon01]
                number13 = evaluation_value.iat[enemy.pokemon03, me.pokemon01]
                number1 = number11 + number12 + number13
                print(f"number11: {number11}, number12: {number12}, number13: {number13}")
                print(f"pokemon1_number_of_wins: {number1}")
                number21 = evaluation_value.iat[enemy.pokemon01, me.pokemon02]
                number22 = evaluation_value.iat[enemy.pokemon02, me.pokemon02]
                number23 = evaluation_value.iat[enemy.pokemon03, me.pokemon02]
                number2 = number21 + number22 + number23
                print(f"number21: {number21}, number22: {number22}, number23: {number23}")
                print(f"pokemon2_number_of_wins: {number2}")
                number31 = evaluation_value.iat[enemy.pokemon01, me.pokemon03]
                number32 = evaluation_value.iat[enemy.pokemon02, me.pokemon03]
                number33 = evaluation_value.iat[enemy.pokemon03, me.pokemon03]
                number3 = number31 + number32 + number33
                print(f"number31: {number31}, number32: {number32}, number33: {number33}")
                print(f"pokemon3_number_of_wins: {number3}")
                battle_point_me = number1 + number2 + number3
                print(f"me_number_of_wins: {battle_point_me}")

                if i==0:
                    battle_point_me_sum0 =  battle_point_me_sum0 + battle_point_me
                elif i==1:
                    battle_point_me_sum1 =  battle_point_me_sum1 + battle_point_me
                elif i==2:
                    battle_point_me_sum2 =  battle_point_me_sum2 + battle_point_me
                elif i==3:
                    battle_point_me_sum3 =  battle_point_me_sum3 + battle_point_me
                elif i==4:
                    battle_point_me_sum4 =  battle_point_me_sum4 + battle_point_me
                elif i==5:
                    battle_point_me_sum5 =  battle_point_me_sum5 + battle_point_me
                elif i==6:
                    battle_point_me_sum6 =  battle_point_me_sum6 + battle_point_me
                elif i==7:
                    battle_point_me_sum7 =  battle_point_me_sum7 + battle_point_me
                elif i==8:
                    battle_point_me_sum8 =  battle_point_me_sum8 + battle_point_me
                elif i==9:
                    battle_point_me_sum9 =  battle_point_me_sum9 + battle_point_me

                battle_point_me_sum0_molded = [battle_point_me_sum0, 0]
                battle_point_me_sum1_molded = [battle_point_me_sum1, 1]
                battle_point_me_sum2_molded = [battle_point_me_sum2, 2]
                battle_point_me_sum3_molded = [battle_point_me_sum3, 3]
                battle_point_me_sum4_molded = [battle_point_me_sum4, 4]
                battle_point_me_sum5_molded = [battle_point_me_sum5, 5]
                battle_point_me_sum6_molded = [battle_point_me_sum6, 6]
                battle_point_me_sum7_molded = [battle_point_me_sum7, 7]
                battle_point_me_sum8_molded = [battle_point_me_sum8, 8]
                battle_point_me_sum9_molded = [battle_point_me_sum9, 9]

    #集計
    battle_point_me_sum_molded = [
        battle_point_me_sum0_molded,
        battle_point_me_sum1_molded,
        battle_point_me_sum2_molded,
        battle_point_me_sum3_molded,
        battle_point_me_sum4_molded,
        battle_point_me_sum5_molded,
        battle_point_me_sum6_molded,
        battle_point_me_sum7_molded,
        battle_point_me_sum8_molded,
        battle_point_me_sum9_molded
    ]
    print("\n")
    print("This is a battle point of ten party.")
    print(battle_point_me_sum_molded)

    sorted_data = sorted(battle_point_me_sum_molded, reverse=True)

    print("\n")
    print("This is a battle point of ten sorted party.")
    print(sorted_data)

    #選択
    selected_data = sorted_data[:5]
    print("\n")
    print("This is five selcted parties.")
    print(selected_data)

    #交叉
    #勝ち抜いた5つのパーティを各変数に代入
    ranking_1_party = party.iloc[selected_data[0][1]]
    ranking_2_party = party.iloc[selected_data[1][1]]
    ranking_3_party = party.iloc[selected_data[2][1]]
    ranking_4_party = party.iloc[selected_data[3][1]]
    ranking_5_party = party.iloc[selected_data[4][1]]

    print("This is five selcted detail parties.")
    print(ranking_1_party)
    print(ranking_2_party)
    print(ranking_3_party)
    print(ranking_4_party)
    print(ranking_5_party)

    ranking_party_list = [
        [ranking_1_party.pokemon01, ranking_1_party.pokemon02, ranking_1_party.pokemon03],
        [ranking_2_party.pokemon01, ranking_2_party.pokemon02, ranking_2_party.pokemon03],
        [ranking_3_party.pokemon01, ranking_3_party.pokemon02, ranking_3_party.pokemon03],
        [ranking_4_party.pokemon01, ranking_4_party.pokemon02, ranking_4_party.pokemon03],
        [ranking_5_party.pokemon01, ranking_5_party.pokemon02, ranking_5_party.pokemon03]
    ]
    print("This is five selcted detail parties listed.")
    print(ranking_party_list)

    #初期化
    crossover_list_append = []
    #ループ
    for i in range(5):
        cross1 = random.randint(0,4)
        cross2 = random.randint(0,4)
        cross1_list = ranking_party_list[cross1]
        cross2_list = ranking_party_list[cross2]
        print(cross1_list)
        print(cross2_list)
        cross1_element1 = 0
        cross1_element2 = random.randint(1,2)
        cross2_element1 = random.randint(0,2)
        cross1_element1_list = cross1_list[cross1_element1]
        cross1_element2_list = cross1_list[cross1_element2]
        cross2_element1_list = cross2_list[cross2_element1]
        crossover_list = [cross1_element1_list, cross1_element2_list, cross2_element1_list]
        crossover_list_append.append(crossover_list)

    print(crossover_list_append)

    crossover_list_append.extend(ranking_party_list)
    print("\n")
    print("This is a list of ten parties crossovered.")
    print(crossover_list_append)


    #突然変異
    probability = 0.5
    rest_of_probability = 1 - probability
    for i in range(10):
        mutation_party = crossover_list_append[i]
        flag = np.random.choice([0,1], p=[probability, rest_of_probability])
        if flag==0:
            change_element = random.randint(0,2)
            choice_element = random.randint(0,5)
            mutation_party[change_element] = choice_element
        elif flag==1:
            pass

    print("This is a list of ten parties mutated.")
    print(crossover_list_append)

    #初期化
    pokemon1 = []
    pokemon2 = []
    pokemon3 = []

    for i in range(10):
        pokemon1_element = crossover_list_append[i][0]
        pokemon1.append(pokemon1_element)
    for i in range(10):
        pokemon2_element = crossover_list_append[i][1]
        pokemon2.append(pokemon2_element)
    for i in range(10):
        pokemon3_element = crossover_list_append[i][2]
        pokemon3.append(pokemon3_element)

    print("pokemon1 list")
    print(pokemon1)
    print("pokemon2 list")
    print(pokemon2)
    print("pokemon3 list")
    print(pokemon3)

    result = pd.DataFrame(
        data={'party_id': np.array([0,1,2,3,4,5,6,7,8,9]),
                'pokemon01': np.array(pokemon1), 
                'pokemon02': np.array(pokemon2),
                'pokemon03': np.array(pokemon3)
            }
    )

    #完成
    print("complete")
    print(result)

    return result


#初期集団の生成
#[x_1, x_2, x_3]
print("This is a dataframe of ten party.")
party = pd.DataFrame(
    data={'party_id': np.array([0,1,2,3,4,5,6,7,8,9]),
            'pokemon01': np.array([random.randint(0,5) for _ in range(10)]), 
            'pokemon02': np.array([random.randint(0,5) for _ in range(10)]),
            'pokemon03': np.array([random.randint(0,5) for _ in range(10)])
        }
)


#評価表
print("This is a dataframe of evaluation value.")
evaluation_value = pd.DataFrame(
    data={'0': np.array([0,-2,1,0,0,1]), 
            '1': np.array([1,-1,-1,1,0,0]),
            '2': np.array([-1,1,-1,0,1,0]),
            '3': np.array([0,0,1,0,-2,1]),
            '4': np.array([0,1,0,1,-1,-1]),
            '5': np.array([1,0,0,-1,1,-1]),
        }
)

gen = 1
while gen <=1000:
    party = GA(party, evaluation_value)
    gen = gen + 1

print(party)