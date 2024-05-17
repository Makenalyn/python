#!/usr/bin/python3
import cmd

class my_cmd(cmd.Cmd):
    
    def do_greet(self, line):
        print ("hello")

if __name__ == '__main__':
    my_cmd().cmdloop()
