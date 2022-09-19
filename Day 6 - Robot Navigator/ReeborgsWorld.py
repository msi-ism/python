# Hurdle 1
# def turn_around():
#     turn_left()
#     turn_left()
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for number in range(0, 6):
#     # jump()

# while not at_goal() == True:
#     if wall_in_front() == True:
#         jump()
#     else:
#         move()


# def long_jump():
#     turn_left()
#     while front_is_clear() == True:
#         while wall_in_front() == False:
#             while right_is_clear() == False
#                 move()
#         if wall_on_right() == False:
#            hurdle()
#         else:
#            long_jump()


# ***Hurdle 4*** Winning code
# def long_jump():
#     turn_left()
#     if front_is_clear() == True:
#         while is_facing_north() == True:
#             if right_is_clear() == False:
#                 move()
#             else:
#                 hurdle()      
# def hurdle():
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear() == True:
#         move()
#     turn_left()

# while not at_goal() == True:
#     while front_is_clear() == True:
#         move()
#     long_jump()
     
        

# from turtle import update


# def move_forward():
#     while wall_in_front() == False:
#         move()
# while not at_goal() == True:
#     if right_is_clear() == True:
#         turn_right()
#         move_forward()
#     elif wall_in_front() == True:
#         turn_left()
#     else:
#         turn_left()
#     move_forward()
    
    
#     Bottom solution
    
# def move_forward():
#     if right_is_clear() == True:
#         turn_right()
#         move()
#     while wall_in_front() == False:
#         move()
        
# while not at_goal() == True:
#     if right_is_clear() == True:
#         turn_right()
#         move()
#         move_forward()
#     elif front_is_clear() == True:
#         move_forward()
#     elif wall_in_front() == True:
#         turn_left()
#         move_forward()
#     else:
#         turn_left()
        
        
# Winning Solution

# def move_forward():
#     while wall_in_front() == False:
#         if right_is_clear() == True:
#             turn_right()
#         move()
        
# while not at_goal() == True:
#     if right_is_clear() == True:
#         turn_right()
#         move()
#     elif front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         turn_left()
#         move_forward()
#     else:
#         turn_left()
#     move_forward()
 
#  Problem World One update
# def move_forward():
#     while not at_goal() == True:
#         while wall_in_front() == False:
#             move()
#         if right_is_clear() == True:
#             turn_right()
#             move()
#         else:
#             turn_left()
#             move()
            
# while not at_goal() == True:
#     if right_is_clear() == True:
#         turn_right()
#         move()
#         move_forward()
#     elif front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         turn_left()
#         move_forward()
#     else:
#         turn_left()
#     move_forward()
    
# Problem Two update
# def turn_around():
#     turn_left()
#     turn_left()
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# def move_forward():
#     while not at_goal() == True:
#         while wall_in_front() == False:
#             move()
#         if right_is_clear() == True:
#             turn_right()
#             move_forward()
#         elif front_is_clear() == True:
#             move_forward()
#         elif wall_in_front() == True:
#             turn_left()
#         else:
#             turn_left()
            
# move_forward()

# Winning Solution Final

# def move_forward():
#     if front_is_clear() == True:
#         move()
    
# while not at_goal() == True:
#     while wall_in_front() == False:
#         move_forward()
#     if right_is_clear() == True:
#         turn_right()
#     elif wall_in_front() == False:
#             move_forward()
#     else:
#         turn_left()
# if right_is_clear() == True:
#     turn_right()
# else:
#     turn_left()
    