import os

# Get PWD and create list
current_dir = os.getcwd()
diagrams = []
# Add diagrams
for item in os.listdir( current_dir ):
    if '.mp' in item:
        diagrams.append(item)
# User info    
print('Will process following diagrams:')
print( diagrams )   
for diagram in diagrams:
    os.system( 'mpost {}'.format( diagram ) )     
