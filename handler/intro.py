import os
import sys


class Banner:
    def __init__(self):
        self.version = 1.0

    def banner(self):
        os.system('color 0A')
        print('''
                        - - - - - - - - - - - - - - - - - - - 

                               ###                       ##
         #####                  ##                   #   ##
        ##   #                  ##                  ##
        ##      ### #  ###    ####  ### ##   ###   #### ###   ####  #####
        ##       #### ## ##  ## ##   ## ##  ## ##   ##   ##  ## ###  ## ##
        ##  ###  ##    ####  ## ##   ## ##   ####   ##   ##  ##  ##  ## ##
        ##  ##   ##   ## ##  ## ##   ## ##  ## ##   ##   ##  ### ##  ## ##
         #####  ####   #####  #####   #####  #####   ## ####  ####  ### ###



                             ##
        #####                ##               #    ###  ## ## ## ##
         ## ##                               ##   ## ## ## ## ## ##
         ## ## ### #  ####  ###  ###   ###  ####     ## ## ## ## ##
         ####   #### ## ###  ## ## ## ## ##  ##     ##  ## ## ## ##
         ##     ##   ##  ##  ## ##### ##     ##    ##
         ##     ##   ### ##  ## ##    ###    ##   ##### ## ## ## ##
        ####   ####   ####   ##  ####  ####   ##  ##### ## ## ## ##
                             ##
                            ##

                        - - - - - - - - - - - - - - - - - - - 
                             H A M Z A
                                        v{}
                        - - - - - - - - - - - - - - - - - - -


            '''.format(self.version))

