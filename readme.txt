Assignment 2

An instance of Py_Agent stores the following information:
- orientation (string which can be accessed by calling the get_orientation method) Possible values: 'RIGHT','UP','LEFT','DOWN'
- location (list which can be accessed by calling the get_location method). The location is is only updated until the agent dies. Thus, if an agent dies in a certain square, the location of that agent will be the square in which they were previously in before dying by the wumpus, or falling down a pit. Possible values: (x,y) where x and y are integers. The agent begins in (1,1). Moving up increases y by 1, moving down decreases y by 1, moving right increases x by 1, moving left decreases x by 1.
- if agent has gold (boolean which can be accessed by calling the has_gold method)
- if the agent has an arrow (boolean which can be accessed by calling the has_arrow method)