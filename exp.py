import random
import pandas as pd
import numpy as np
# グラフ可視化
import plotly.graph_objects as go
#~.iat[列,行]




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

#初期化
battle_point_me_sum_molded = []
#評価関数
for i in range(10):
    battle_point_me_sum = 0
    for j in range(10):
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
            all_list = [number1, number2, number3]
            top_second_list = sorted(all_list ,reverse=True)
            battle_point_me = top_second_list[0] + top_second_list[1]
            print(f"This is a battle_point: {battle_point_me}")
            battle_point_me_sum = battle_point_me_sum + battle_point_me
    battle_point_me_sum_molded.append([battle_point_me_sum, i])

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

print("This is five selcted parties detail.")
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
    cross1_element1 = 0
    cross1_element2 = random.randint(1,2)
    cross2_element1 = random.randint(0,2)
    cross1_element1_list = cross1_list[cross1_element1]
    cross1_element2_list = cross1_list[cross1_element2]
    cross2_element1_list = cross2_list[cross2_element1]
    crossover_list = [cross1_element1_list, cross1_element2_list, cross2_element1_list]
    crossover_list_append.append(crossover_list)

print("\n")
print("new crossovered five parties.")
print(crossover_list_append)

ranking_party_list.extend(crossover_list_append)
print("\n")
print("This is a list of ten parties crossovered.")
print(ranking_party_list)


#突然変異
probability = 0.5
rest_of_probability = 1 - probability
for i in range(5):
    change_i = 5 + i
    mutation_party = ranking_party_list[change_i]
    flag = np.random.choice([0,1], p=[probability, rest_of_probability])
    if flag==0:
        change_element = random.randint(0,2)
        choice_element = random.randint(0,5)
        mutation_party[change_element] = choice_element
    elif flag==1:
        pass

print("This is a list of ten parties mutated.")
print(ranking_party_list)

#結果のdf化
#初期化
pokemon1 = []
pokemon2 = []
pokemon3 = []

for i in range(10):
    pokemon1_element = ranking_party_list[i][0]
    pokemon1.append(pokemon1_element)
for i in range(10):
    pokemon2_element = ranking_party_list[i][1]
    pokemon2.append(pokemon2_element)
for i in range(10):
    pokemon3_element = ranking_party_list[i][2]
    pokemon3.append(pokemon3_element)

result = pd.DataFrame(
    data={'party_id': np.array([0,1,2,3,4,5,6,7,8,9]),
            'pokemon01': np.array(pokemon1), 
            'pokemon02': np.array(pokemon2),
            'pokemon03': np.array(pokemon3)
        }
)

#初期化
pokemon_graph = []
for i in range(5):
    pokemon1_element_graph = ranking_party_list[i][0]
    pokemon_graph.append(pokemon1_element_graph)
for i in range(5):
    pokemon2_element_graph = ranking_party_list[i][1]
    pokemon_graph.append(pokemon2_element_graph)
for i in range(5):
    pokemon3_element_graph = ranking_party_list[i][2]
    pokemon_graph.append(pokemon3_element_graph)

print("\n")
print(pokemon_graph)

#初期化
element_0_sum = 0
element_1_sum = 0
element_2_sum = 0
element_3_sum = 0
element_4_sum = 0
element_5_sum = 0
for i in range(15):
    element = pokemon_graph[i]
    if element==0:
        element_0_sum = element_0_sum + 1
    elif element==1:
        element_1_sum = element_1_sum + 1
    elif element==2:
        element_2_sum = element_2_sum + 1
    elif element==3:
        element_3_sum = element_3_sum + 1
    elif element==4:
        element_4_sum = element_4_sum + 1
    elif element==5:
        element_5_sum = element_5_sum + 1

graph_list = [element_0_sum, element_1_sum, element_3_sum, element_4_sum, element_5_sum]

print(f"element_0_sum: {element_0_sum}")
print(f"element_1_sum: {element_1_sum}")
print(f"element_2_sum: {element_2_sum}")
print(f"element_3_sum: {element_3_sum}")
print(f"element_4_sum: {element_4_sum}")
print(f"element_5_sum: {element_5_sum}")

#完成
print("complete")
print(result)