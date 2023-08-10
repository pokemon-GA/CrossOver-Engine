import random
import pandas as pd
import numpy as np
# グラフ可視化
import plotly.graph_objects as go
#~.iat[列,行]

#パーティ数(偶数のみ)
number_of_party = 30

def GA(party, evaluation_value):
#初期化
    battle_point_me_sum_molded = []
    #評価関数
    for i in range(number_of_party):
        battle_point_me_sum = 0
        for j in range(number_of_party):
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
    select = int(number_of_party / 2)
    selected_data = sorted_data[:select]
    print("\n")
    print("This is five selcted parties.")
    print(selected_data)

    #交叉
    #勝ち抜いた5つのパーティを各変数に代入
    ranking_party_list = []
    for i in range (select):
        ranking_party = [
            party.iloc[selected_data[i][1]].pokemon01,
            party.iloc[selected_data[i][1]].pokemon02,
            party.iloc[selected_data[i][1]].pokemon03
        ]
        ranking_party_list.append(ranking_party)

    print("This is five selcted detail parties listed.")
    print(ranking_party_list)

    #初期化
    crossover_list_append = []
    rand_select = int(select - 1)
    #ループ
    for i in range(select):
        cross1 = random.randint(0,rand_select)
        cross2 = random.randint(0,rand_select)
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
    for i in range(select):
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

    for i in range(number_of_party):
        pokemon1_element = ranking_party_list[i][0]
        pokemon1.append(pokemon1_element)
    for i in range(number_of_party):
        pokemon2_element = ranking_party_list[i][1]
        pokemon2.append(pokemon2_element)
    for i in range(number_of_party):
        pokemon3_element = ranking_party_list[i][2]
        pokemon3.append(pokemon3_element)

    result = pd.DataFrame(
        data={'party_id': np.array([_ for _ in range(number_of_party)]),
                'pokemon01': np.array(pokemon1),
                'pokemon02': np.array(pokemon2),
                'pokemon03': np.array(pokemon3)
            }
    )

    #グラフ生成
    #初期化
    pokemon_graph = []
    for i in range(select):
        pokemon1_element_graph = ranking_party_list[i][0]
        pokemon_graph.append(pokemon1_element_graph)
    for i in range(select):
        pokemon2_element_graph = ranking_party_list[i][1]
        pokemon_graph.append(pokemon2_element_graph)
    for i in range(select):
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

    print(f"element_0_sum: {element_0_sum}")
    print(f"element_1_sum: {element_1_sum}")
    print(f"element_2_sum: {element_2_sum}")
    print(f"element_3_sum: {element_3_sum}")
    print(f"element_4_sum: {element_4_sum}")
    print(f"element_5_sum: {element_5_sum}")

    #完成
    print("complete")
    print(result)
    return result, element_0_sum, element_1_sum, element_2_sum, element_3_sum, element_4_sum, element_5_sum



























#初期集団の生成
#[x_1, x_2, x_3]
party = pd.DataFrame(
    data={'party_id': np.array([_ for _ in range(number_of_party)]),
            'pokemon01': np.array([random.randint(0,5) for _ in range(number_of_party)]), 
            'pokemon02': np.array([random.randint(0,5) for _ in range(number_of_party)]),
            'pokemon03': np.array([random.randint(0,5) for _ in range(number_of_party)])
        }
)


#評価表
evaluation_value = pd.DataFrame(
    data={'0': np.array([0,-2,1,0,0,1]), 
            '1': np.array([1,-1,-1,1,0,0]),
            '2': np.array([-1,1,-1,0,1,0]),
            '3': np.array([0,0,1,0,-2,1]),
            '4': np.array([0,1,0,1,-1,-1]),
            '5': np.array([1,0,0,-1,1,-1]),
        }
)

#main関数
element_0_list = []
element_1_list = []
element_2_list = []
element_3_list = []
element_4_list = []
element_5_list = []
gen = 1
while gen <=500:
    party, element_0, element_1, element_2, element_3, element_4, element_5 = GA(party, evaluation_value)
    gen = gen + 1
    element_0_list.append(element_0)
    element_1_list.append(element_1)
    element_2_list.append(element_2)
    element_3_list.append(element_3)
    element_4_list.append(element_4)
    element_5_list.append(element_5)

print(party)


gen_number = list(range(1,501,1))

fig = go.Figure()

fig.add_trace(
    go.Scatter(x = gen_number, #X_label
               y = element_0_list, #y_label
              text = "No.0 ポケモン", #
              mode = 'lines', #折れ線グラフ
              name = 'No.0', #line_name
              line=dict(color='rgb(239, 85, 59)', width=1, dash='solid') #line_type_detail      
    )
)
fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_1_list,
              text = "No.1 ポケモン",
              mode = 'lines',
              name = 'No.1',
              line=dict(color='rgb(25, 211, 243)', width=1, dash='solid')  
              
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_2_list,
              text = "No.2 ポケモン",
              mode = 'lines',
              line=dict(color='rgb(188, 189, 34)', width=1, dash='solid'),
              name = 'No.2'
              
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_3_list,
              text = "No.3 ポケモン",
              mode = 'lines',
              line=dict(color='firebrick', width=1, dash='solid'),
              name = 'No.3'
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_4_list,
              text = "No.4 ポケモン",
              mode = 'lines',
              line=dict(color='rgb(48, 73, 125)', width=1, dash='solid'),
              name = 'No.4'
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_5_list,
              text = "No.5 ポケモン",
              mode = 'lines',
              line=dict(color='rgb(255, 185, 0)', width=1, dash='solid'),
              name = 'No.5'
    )
)

fig.update_layout(
    xaxis_title = 'Generation',
    yaxis_title = 'Number of each pokemons'
)

    
fig.show()