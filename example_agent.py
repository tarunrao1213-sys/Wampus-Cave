

def agent_function(request_dict, _info):

    # TOOD: Implement this function in a better way
    
    #print("Request: ",request_dict )

    observation = request_dict.get("observation", {})
    map_str = request_dict.get("map") or observation.get("map")
    current_cell = request_dict.get("observations", {}).get("current-cell")
    
    print("\n\nOG_Current cell type:", current_cell)

    if current_cell == 'B':
        current_cell = 'C'or'B'
    elif current_cell == 'M':
        current_cell = 'M'
    elif current_cell == 'C':
        current_cell = 'C'
    elif current_cell == 'S':
        current_cell = 'S'
    

    print("\nObservation: ",request_dict)
    print("Current cell type:", current_cell)


    if not map_str:
        print("No map found in request.")
    else:
        map_lines = map_str.strip().split('\n')
        game_map = [list(row) for row in map_lines]
        rows, cols = len(game_map), len(game_map[0])

        #position=None
    
        print("game_map: ",game_map)
        print("rows , cols: ", rows,cols)

        #print("The 1st Cell Row 0,col 0: ",game_map[0][0])
        
        Expected_Time = 0
        Success_chance = 0


        Cell_count = 0
        Cell_coordinates=[]

        Active_cell = 0
        Time_count = 0

        W_count = 0
        W_coordinates=[]

        S__count = 0
        S_coordinates = []

        # Find total numbers of Possible Cell with its Coordinates
    
        for x in range(rows):
            for y in range(cols):
                if game_map[x][y] == current_cell:
                    Cell_count += 1
                    Cell_coordinates.append((x,y))

        
        for x in range(rows):
            for y in range(cols):
                if game_map[x][y] == "W":
                    W_count += 1
                    W_coordinates.append((x,y))
        
        for x in range(rows):
            for y in range(cols):
                if game_map[x][y] == "S":
                    S__count += 1
                    S_coordinates.append((x,y))
       

                                
        print("\nTotal number of 'Posible Cell':", Cell_count)
        print("Coordinates of 'Posible Cell':", Cell_coordinates)
       


        # Individual Probability of the Possible Cell
        Prob_PCell = 1/Cell_count
        print("Individual Probability of 'Possible Cell':", Prob_PCell)

        #directions = {"GO north": (-1, 0), "GO south": (1, 0),"GO east": (0, 1), "GO west": (0, -1)}
        
        

        def select_1_dirct(coordinates):

            #South
            time_count_S = 0
            active_cell_S =0
            temp_co_S = []
            temp_co_S_S = []

            #North
            time_count_N = 0
            active_cell_N=0
            temp_co_N = []
            temp_co_N_N = []

            #East
            time_count_E = 0
            active_cell_E = 0
            temp_co_E = []
            temp_co_E_E = []

            #West
            time_count_W = 0
            active_cell_W=0
            temp_co_W = []
            temp_co_W_W = []

            print("\n \n loop action coordinate :",coordinates)

            for x,y in coordinates:
                if x+1<rows  and y<cols:
                    
                    if  game_map[x + 1][y] == 'W': #Driction = South 
                        print(f"South Current Cell at ({x}, {y}) is: W")
                    
                        active_cell_S +=1
                        time_count_S +=0.5

                        print("Time S=", time_count_S)
                        print("Active S cells =", active_cell_S)
                        temp_co_S.append((x,y))
                    
                    elif  game_map[x + 1][y] != 'W': #Driction != South     
                            temp_co_S_S.append((x+1,y))


                    else:
                        print(f"No direction for Current Cell ({x}, {y})")
                        print("No Direction fround")


            for x,y in coordinates:
                if rows>x-1>-1 and y<cols :
                    if  game_map[x - 1][y] == 'W':  #Direction : North
                        print(f"North Current Cell at ({x}, {y}) is: W")
            
                        active_cell_N +=1
                        time_count_N +=0.5

                        print("Time N =", time_count_N)
                        print("Active N cells =", active_cell_N)
                        temp_co_N.append((x,y))
                        #temp_co_N_N.append((x+1,y))
                    
                    elif game_map[x - 1][y] != 'W':  #Direction !: North
                        temp_co_N_N.append((x-1,y))

                    else:
                        print(f"No direction for Current Cell ({x}, {y})")
                        print("No Direction fround")


            for x,y in coordinates:
                if -1<x<rows and y+1<cols :

                    if  game_map[x][y+1] == 'W':  #Direction = East
                        print(f"East Current Cell at ({x}, {y}) is: W")
                    
                        active_cell_E +=1
                        time_count_E +=0.5

                        print("Time E =", time_count_E)
                        print("Active E cells =", active_cell_E)
                        temp_co_E.append((x,y))

                    elif  game_map[x][y+1] != 'W':  #Direction != East    
                        temp_co_E_E.append((x,y+1))

                    else:
                        print(f"No direction for Current Cell ({x}, {y})")
                        print("No Direction fround")


            for x,y in coordinates:
                if -1<x<rows  and cols>y-1>-1:
                    if  game_map[x][y-1] == 'W':  #Direction = West
                        print(f"West Current Cell at ({x}, {y}) is: W")
                    
                        active_cell_W +=1
                        time_count_W +=0.5

                        print("Time W =", time_count_W)
                        print("Active W cells =", active_cell_W)
                        temp_co_W.append((x,y))
                    
                    elif  game_map[x][y-1] != 'W':  #Direction != West
                        temp_co_W_W.append((x,y-1))
                    
                    else:
                        print(f"No direction for Current Cell ({x}, {y})")
                        print("No Direction fround")

            
            values = {"GO south": (active_cell_S,time_count_S,temp_co_S,temp_co_S_S), "GO north": (active_cell_N,time_count_N,temp_co_N,temp_co_N_N), 
                        "GO east": (active_cell_E,time_count_E,temp_co_E,temp_co_E_E), "GO west": (active_cell_W,time_count_W,temp_co_W,temp_co_W_W)}
            
            print(values)

            max_var = max(values, key=lambda k: values[k][0])
            max_value = values[max_var]

            print(f"\nMaximum W cells {max_value[0]} and time is {max_value[1]} , from Direction '{max_var}'")

            return max_var,max_value[0],max_value[1],max_value[2],max_value[3]


        
        def select_2_dirct(First__action,co_ordinates):
            
            print("\n \n loop 2nd action coordinate :",co_ordinates)

            if First__action == "GO south":

               
                co_ordinates = list(set(co_ordinates))
                co_ordinates.sort()                
                print("South of cell :",co_ordinates)

                Action = select_1_dirct(co_ordinates)
                

            elif First__action == "GO north":
                
                co_ordinates = list(set(co_ordinates))
                co_ordinates.sort()                
                print("North of cell :",co_ordinates)

                
                Action = select_1_dirct(co_ordinates)
                #return Action[0],Action[1],Action[2],Action[3],Action[4]


            elif First__action == "GO east":
                
                
                co_ordinates = list(set(co_ordinates))
                co_ordinates.sort()                
                print("East of cell :",co_ordinates)

                
                Action = select_1_dirct(co_ordinates)
                #return Action[0],Action[1],Action[2],Action[3],Action[4]



            elif First__action == "GO west":

                
                co_ordinates = list(set(co_ordinates))
                co_ordinates.sort()                
                print("West of cell :",co_ordinates)

                
                Action = select_1_dirct(co_ordinates)
                #return Action[0],Action[1],Action[2],Action[3],Action[4]


            else:
                print("No 2nd Direction")

                    
        
            return Action[0],Action[1],Action[2],Action[3],Action[4]

        



        


       
        #1st Action 
        # Search the value from Current_Cell coordinates

        First_Action = select_1_dirct(Cell_coordinates)

        #W_Result = [item for item in W_coordinates if item not in First_Action[4]]
        #print(result)


        Active_cell = First_Action[1]
        Time_count = First_Action[1] * 0.5 


        print("\nFirst Action :",First_Action[0])
        
        #2nd Action
        result = [item for item in First_Action[4] if item not in S_coordinates]
        Second_Action = select_2_dirct(First_Action[0],result)        

        if current_cell == 'S':
            print("No 2nd Direction for S cell allowed")
            Active_cell = First_Action[1]
            Time_count = First_Action[1] 

            
        else:
            
            Active_cell += Second_Action[1]
            Time_count = Time_count + (Second_Action[1] * 1.5)
            print("\nSecond Action :",Second_Action[0])

        

        
        if Active_cell == 0:
            print("\n Wrong Directions")
            Active_cell =1

            Expected_Time = 2

            Success_chance = 0

        else:
            Expected_Time = Time_count / Active_cell

            Success_chance = Prob_PCell * Active_cell
        print('\n  Next Call: \n')
        
        return {"actions": [First_Action[0] ,Second_Action[0]], "success-chance": Success_chance, "expected-time": Expected_Time}



if __name__ == '__main__':
    try:
        from client import run
    except ImportError:
        raise ImportError('You need to have the client.py file in the same directory as this file')

    import logging
    logging.basicConfig(level=logging.INFO)

    import sys
    config_file = sys.argv[1]

    run(
        config_file,        # path to config file for the environment (in your personal repository)
        agent_function,
        processes=1,        # higher values will call the agent function on multiple requests in parallel
        run_limit=10,     # stop after 1000 runs (then the rating is "complete")
        parallel_runs=False  # multiple requests are bundled in one server interaction (more efficient)
    )



