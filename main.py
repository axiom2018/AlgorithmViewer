from tkinter import *
from tkinter import font
import time
from Bfs import Bfs
from Dfs import Dfs

class AlgorithmView:
    def __init__(self, rows, columns):
        # Initialize the window and set the name and size.
        self.m_window = Tk()
        self.m_window.title("My Screen")
        self.m_window.geometry("800x800")
        self.m_window.configure(bg='gray')


        # A label for the title of the program.
        self.m_title = Label(self.m_window, text="Algorithm View", font=("Arial", 15, "underline"))
        self.m_title.configure(bg='gray')
        self.m_title.place(x=330, y=10)


        # Initialize the grid and it's dimenstions.
        self.m_grid = []
        self.m_y = rows
        self.m_x = columns


        ''' m_algorithmToRun - The string that will hold the choice from the drop down menu.
            m_algorithmRunning - While an algorithm is currently running we cannot allow the user to click any square at ALL.
            .set - Setting a default choice when the code is run.
            m_dropdown - The actual menu with the options to choose from. 
            .place - Selecting where to put it. 
            m_ddButton - The drop down button to run the algorithm selected in the drop down box. 
            m_currentSteps - For each algorithm we can choose to show the steps. '''
        self.m_algorithmToRun = StringVar()
        self.m_algorithmToRun.set("Breadth First Search")   
        self.m_algorithmRunning = False             
        self.m_dropdown = OptionMenu(self.m_window, self.m_algorithmToRun, "Breadth First Search", "Depth First Search", "A Star")
        self.m_dropdown.place(x=90, y=400)
        self.m_ddButton = Button(self.m_window, text="Run Algorithm", command=self.RunAlgorithm)
        self.m_ddButton.place(x=265, y=403)
        self.m_currentSteps = Bfs(self.m_window)

        # The following variables help with spacing between squares, and positioning them on screen.
        self.m_spacingX = 20
        self.m_spacingY = 30
        self.m_startX = 190
        self.m_startY = 50
        self.m_currentX = self.m_startX
        self.m_currentY = self.m_startY

        ''' The colors to shade the buttons. 
            m_defaultColor - The regular default color of almost everysquare.
            m_startColor - The color button where the algorithm will START from.
            m_goalColor - The color button that the algorithm is trying to go TO.
            m_clickedColor - The color on buttons after you click one of them trying to make a barrier/blockade.
            m_algorithmColor - The color of using an algorithm to tell you what nodes have been explored and give 
                more visuals for the user to see. 
            m_landedOnGoalColor - '''
        self.m_defaultColor = '#737373'
        self.m_startColor = '#FFA500'
        self.m_goalColor = '#FF0000'
        self.m_clickedColor = '#7FFFD4'
        self.m_algorithmColor = '#D2B48C'
        self.m_landedOnGoalColor = '#63B8FF'

        ''' For managing the start position. 
            m_startPos - The starting position that all algorithms will begin from, changable. 
            m_changeStartPosButton - A button that when pressed, let's the user click around for a new start position. 
                                    But does not allow the start and end position to be the same.
            m_saveStartPosButton - When the user is done selecting a new start pos, they will press this button to 
                                    continue.
        '''
        self.m_startPos = [0, 0]
        self.m_changeStartPosButton = Button(self.m_window, text="Change Starting Position", command=self.ChangeStartingPosition)
        self.m_changeStartPosButton.place(x=390, y=403)
        self.m_saveStartPosButton = Button(self.m_window, text="Finish Changing Start Pos", command=self.FinishChangingStartPos)
        self.m_saveStartPosButton.place(x=390, y=440)
        self.m_saveStartPosButton.place_forget()


        ''' For managing the end position. 
            m_endPos - Get the end position manually.
            m_changeEndPosButton - The button to change the position.
        '''
        self.m_endPos = [self.m_y - 1, self.m_x - 1]
        self.m_changeEndPosButton = Button(self.m_window, text="Change Ending Position", command=self.ChangeEndPosition)
        self.m_changeEndPosButton.place(x=550, y=403)
        self.m_saveEndPosButton = Button(self.m_window, text="Finish Changing End Pos", command=self.FinishChangingEndPos)
        self.m_saveEndPosButton.place(x=550, y=440)
        self.m_saveEndPosButton.place_forget()


        ''' When we run an algorithm, we DON'T want the user to continue to click buttons 
        until the algorithm is done. So collect buttons in a list to cycle through them in
        the DisableAllButtons function. 
        
        Also the string is to determine which change button was clicked and how to proceed. '''
        self.m_buttons = []
        self.m_buttons.append(self.m_ddButton)
        self.m_buttons.append(self.m_changeStartPosButton)
        self.m_buttons.append(self.m_changeEndPosButton)
        self.m_changeButtonStr = ''

        ''' The following is for the process of resetting the grid once we ran an algorithm. 
            m_resetButton - The button to be pressed to reset the grid, initially hidden of course.
            m_hitResetButton - The boolean value that will be used in a loop in the ResetGrid function.
        '''
        self.m_resetButton = Button(self.m_window, text="Reset Grid", command=self.ClickResetButton)
        self.m_resetButtonPosX = 90
        self.m_resetButtonPosY = 450
        self.m_resetButton.place(x=self.m_resetButtonPosX, y=self.m_resetButtonPosY)
        self.m_resetButton.place_forget()
        self.m_hitResetButton = False

        # Neighbors are for calculating new positions so doing this step is VERY important.
        self.m_neighbors = [[-1,0], [1,0], [0,-1], [0,1]]




        ''' These labels are indicators for the buttons to help the user. 
            m_textFont - The font to go with the labels.
            m_dropDownText - The text for the drop down box.
        '''
        self.m_dropDownText = Label(self.m_window, text="Algorithms to Choose From", font=("Arial", 9, "underline"))
        self.m_dropDownText.place(x=87, y=375)
        self.m_dropDownText.configure(bg='gray')






        # self.m_text = Text(self.m_window, width=30, height=10, font=("Helvetica", 16))
        # self.m_text.place(x=370, y=400)

        # self.m_text = Label(self.m_window, text="Tacos are Good.")
        # self.m_text.place(x=370, y=400)
        # self.m_text.configure(bg='gray')


        # Iterate through grid initializing each entry.
        for y in range(self.m_y):
            # Place a list of course in the current y index.
            self.m_grid.append([])
            for x in range(self.m_x):
                ''' We have to color based on positions. 
                    Top left = Our starting point, unless the user changes it. 
                    Bottom right = The goal point, unless the user changes it. 
                    Everything else - The regular buttons. '''
                if y == self.m_startPos[0] and x == self.m_startPos[1]:
                    self.m_grid[y].append(Button(self.m_window, padx=4, pady=0.2, 
                        command=lambda yPos=y, xPos=x: self.ButtonClick(yPos, xPos), bg=self.m_startColor))

                elif y == self.m_endPos[0] and x == self.m_endPos[1]:
                    self.m_grid[y].append(Button(self.m_window, padx=4, pady=0.2, 
                        command=lambda yPos=y, xPos=x: self.ButtonClick(yPos, xPos), bg=self.m_goalColor))
                else:
                    self.m_grid[y].append(Button(self.m_window, padx=4, pady=0.2, 
                        command=lambda yPos=y, xPos=x: self.ButtonClick(yPos, xPos), bg=self.m_defaultColor))

                # Set position to for placement.
                self.m_grid[y][x].place(x=self.m_currentX, y=self.m_currentY)

                # Increment the x position for the next label.
                self.m_currentX = self.m_currentX + self.m_spacingX

            # Once we're done with the current row, we'll work on the next by incrementing the y for a new row position.
            self.m_currentY = self.m_currentY + self.m_spacingY

            # And of course restart the x.
            self.m_currentX = self.m_startX


    # A simple function that will return true to indicate the reset grid button has been pressed.
    def ClickResetButton(self):
        self.m_hitResetButton = True








    ''' When we want to change a position, starting or end, we must do a few things first.
        ToggleButtons - Disable the RunAlgorithm, ChangeStartPos, and ChangeEndPos buttons, and also disables the drop down menu.
                        Why? While we're in the middle of Changing the start position for example, don't allow the user to click
                        any other buttons until that task is done.
        
        m_changeButtonStr - In order for the ButtonClick function to properly do it's task, it needs to know which of the ChangePosition
                        functions were pressed, if any at all. 
        
        m_saveStartPosButton.place - After they click the ChangeStartingPosition button, it'll be done once they click the save button, 
                        and this button puts it back on the screen. It starts out hidden. 

    '''
    def ChangeStartingPosition(self):
        self.ToggleButtons(True)
        self.m_changeButtonStr = "Start"
        self.m_saveStartPosButton.place(x=390, y=440)

    # Make the change end pos button unclickable, and that is checked in the ButtonClick func. If unclickable, we want a new start pos.
    def ChangeEndPosition(self):
        self.ToggleButtons(True)
        self.m_changeButtonStr = "End"
        self.m_saveEndPosButton.place(x=550, y=440)

    # When we're done selecting a new start position, this button will confirm it by changing the buttons state to normal.
    def FinishChangingStartPos(self):
        self.ToggleButtons(False)
        self.m_changeButtonStr = ""
        self.m_saveStartPosButton.place_forget()

    def FinishChangingEndPos(self):
        self.ToggleButtons(False)
        self.m_changeButtonStr = ""
        self.m_saveEndPosButton.place_forget()


    ''' When any algorithm is done, reset everything so that the start & end positions are the same, as well as removing blockades. 
        1) Reset the start and end positions to the top left and bottom right. 
                This is where they start, unless changed by the user.
        
        2) Loop over the entire grid and check if a position is NOT the default color. 
                If it's not the default color that means it's either the start pos color, end pos color, or a blockade/clicked on color.
                So we have to 
    '''
    def ResetGrid(self):
        # Make the reset grid button visible and others still disabled.
        self.m_resetButton.place(x=self.m_resetButtonPosX, y=self.m_resetButtonPosY)

        # Update window to show change.
        self.m_window.update()

        # Use a boolean, and keep running a loop while it's false.
        while not self.m_hitResetButton:
            # The reset buttons command will call a function to make that boolean true, breaking the loop.
            self.m_window.update()
            continue

        # Reset the default positions again.
        self.m_startPos = [0, 0]
        self.m_endPos = [self.m_y - 1, self.m_x - 1]

        for y in range(self.m_y):
            for x in range(self.m_x):
                self.m_grid[y][x].configure(bg=self.m_defaultColor)
                
        self.m_grid[self.m_startPos[0]][self.m_startPos[1]].configure(bg=self.m_startColor)
        self.m_grid[self.m_endPos[0]][self.m_endPos[1]].configure(bg=self.m_goalColor)

        # Make sure to set the buttons up to be clicked again. 
        self.ToggleButtons(False)

        # Hide the reset button since it has done its job.
        self.m_resetButton.place_forget()

        # Reset the boolean to finish.
        self.m_hitResetButton = False

        # Finally allow clicking again.
        self.ToggleClicking(False)



    def ButtonClick(self, y, x):
        # Only process clicking if an algorithm isn't running.
        if self.CanClick():
            return

        # If disabled, we're currently in the process of changing the start position.
        if self.m_changeButtonStr == "Start":
            if y == self.m_endPos[0] and x == self.m_endPos[1]:
                return

            # Get the old start position button, make it gray.
            self.m_grid[self.m_startPos[1]][self.m_startPos[0]].configure(bg=self.m_defaultColor)

            # Set the new start position.
            self.m_startPos = [x, y]

            # Now apply the new start position to be the start position COLOR.
            self.m_grid[self.m_startPos[1]][self.m_startPos[0]].configure(bg=self.m_startColor)

        elif self.m_changeButtonStr == "End":
            if y == self.m_startPos[1] and x == self.m_startPos[0]:
                return

            self.m_grid[self.m_endPos[0]][self.m_endPos[1]].configure(bg=self.m_defaultColor)
            self.m_endPos = [y, x]
            self.m_grid[self.m_endPos[0]][self.m_endPos[1]].configure(bg=self.m_goalColor)

        elif self.m_grid[y][x].cget('bg') == self.m_defaultColor:
            self.m_grid[y][x].configure(bg=self.m_clickedColor)



    # When algorithm runs, do not allow user to repeatedly click buttons. Toggle them off and on once algorithm is done.
    def ToggleButtons(self, disableButtons):
        if disableButtons:
            for btn in self.m_buttons:
                btn['state'] = DISABLED
            
            # Also disable the drop down menu.
            self.m_dropdown.configure(state='disabled')

        
        elif not disableButtons:
            for btn in self.m_buttons:
                btn['state'] = NORMAL

            # And enable the drop down menu as well.
            self.m_dropdown.configure(state='normal')

    
    # Can't have the user clicking around WHILE the algorithm is running. If true, clicking will be temporarily blocked. If so, clicking is fine. 
    def ToggleClicking(self, disableClicking):
        if disableClicking:
            self.m_algorithmRunning = True
        
        elif not disableClicking:
            self.m_algorithmRunning = False

    
    # Helper function to control when user can click.
    def CanClick(self):
        if self.m_algorithmRunning:
            return True
        
        return False


    def RunAlgorithm(self):
        # Set the buttons to be disabled before the algorithm runs.
        self.ToggleButtons(True)

        # Disable clicking here.
        self.ToggleClicking(True)

        # Call the appropriate algorithm.
        if self.m_algorithmToRun.get() == "Breadth First Search":
            self.BreadthFirstSearch()

        elif self.m_algorithmToRun.get() == "Depth First Search":
            self.DepthFirstSearch()



    def BreadthFirstSearch(self):
        # Need a list of positions that will be the visited positions, add the start to it.
        visitedPositions = []
        visitedPositions.append([self.m_startPos[1], self.m_startPos[0]])

        # Also need a way to keep track of the ones we've visited with this 2d list.
        visited = []
        for y in range(self.m_y):
            visited.append([])
            for x in range(self.m_x):
                visited[y].append(False)

        for y in range(self.m_y):
            visited.append([])
            for x in range(self.m_x):
                print(visited[y][x], end=' ')
            print("\n")

        # We visited the starting pos already so set that.
        visited[self.m_startPos[1]][self.m_startPos[0]] = True

        # Begin the loop, while the visited positions are not empty.
        while visitedPositions:
            # Get the position to start, always index 0.
            y, x = visitedPositions.pop(0)
            
            ''' switching x and y below causes issues. '''
            # Explore the neighbors and we'll potentially reach the goal.
            if self.ExploreNeighbors(y, x, visitedPositions, visited):
                print("Made it to the goal!")
                self.m_window.update()
                self.ResetGrid()
                self.m_window.update()
                return True

            self.m_window.update()

            # Sleep to see the results better.
            time.sleep(0.1)

        # Toggle the button to be on again.
        self.ToggleButtons(False)

        print("Could not reach the goal!")
        self.ResetGrid()
        return False

    
    def DepthFirstSearch(self):
        # Also need a way to keep track of the ones we've visited with this 2d list.
        visited = []
        for y in range(self.m_y):
            visited.append([])
            for x in range(self.m_x):
                visited[y].append(False)

        # Need a list of positions that will be the visited positions, add the start to it.
        stack = []
        stack.append([self.m_startPos[1], self.m_startPos[0]])

        # Mark the starting position.
        visited[self.m_startPos[1]][self.m_startPos[0]] = True

        # Begin the loop
        while stack:
            # Get the top of the stack and remove it.
            y, x = stack.pop(-1)

            # Explore the neighbors and we'll potentially reach the goal.
            if self.ExploreNeighbors(y, x, stack, visited):
                print("Made it to the goal!")
                self.m_window.update()
                self.ResetGrid()
                self.m_window.update()
                return True

            # Update the screen.
            self.m_window.update()

            # Sleep to see the results better.
            time.sleep(0.1)


    def ExploreNeighbors(self, y, x, visitedPositions, visited):
        # Go over every neighbor and calculate positions in y/x format.
        for position in self.m_neighbors:
            # Calculate which spot to check thanks to the current position. Works in up, down, left, and right format.
            currentY = y + position[0]
            currentX = x + position[1]

            # First check up, down, left, and right.
            if currentY < 0:
                continue

            elif currentY > self.m_y - 1:
                continue

            elif currentX < 0:
                continue

            elif currentX > self.m_x - 1:
                continue

            # If we already visited, just continue.
            if visited[currentY][currentX] == True:
                continue
            
            # If this is blocked off, just continue.
            if self.m_grid[currentY][currentX].cget('bg') == self.m_clickedColor:
                continue

            # All the obstacles gone, we can now put this position into visited so we don't revisit.
            visitedPositions.append([currentY, currentX])
            visited[currentY][currentX] = True

            # If this position IS the end position return true, we're done. Also change the color to signify we have made it.
            if currentY == self.m_endPos[0] and currentX == self.m_endPos[1]:
                self.m_grid[currentY][currentX].configure(bg=self.m_landedOnGoalColor)
                return True
            # If not, just change the color of the button.
            else:
                self.m_grid[currentY][currentX].configure(bg=self.m_algorithmColor)
        
        return False


    
    def Update(self):
        self.m_window.mainloop()


# Initialize the class and begin updating. 
ag = AlgorithmView(4, 6) # 10, 20
ag.Update()