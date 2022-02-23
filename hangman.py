class Hangman:      
    
    def __init__(self):
        self.n_wrong = 0 #number of incorrect guesses
        self.secret_word = ''
        self.current_word = [' ']
        self.wrong_dict = {0:(0,0,' '), 1:(1,3,'O'), 2:(2,3,'|'), 3:(2,2,'/'), 4:(2,4,'\\'), 5:(3,2,'/'), 6:(3,4,'\\')} #stick figure limbs for guessing
        self.display_arr = [list('   +---+')] + [[' ' for j in range(7)] + ['| '] for i in range(4)] + [list('     ===')] #stick figure for display
        self.guess_list = [False] * 26 #26 letters for eng lang
        self.hint_flag = 0 #flag for hint summoning (1 means called, 0 means not called)


    #generate secret word
    def secret(self):
        from wonderwords import RandomWord
        R_word_obj = RandomWord() #word_min_length=5, word_max_length=10, -- hasDictionaryDef = True??
        self.secret_word = R_word_obj.word()
        self.current_word = [' '] * len(self.secret_word)
    
    
    #note error (incorrect guess)
    def change_error(self):
        self.n_wrong += 1
        val = self.wrong_dict[self.n_wrong]
        self.display_arr[val[0]][val[1]] = val[2]
                

    #generate index array where guess occurs in secret word        
    def find_all(self,s, c):
        idx = s.find(c)
        arr = []
        while idx != -1:
            arr.append(idx)
            idx = s.find(c, idx + 1)
        return arr
    
    #displays current word and stick figure 
    def display(self):
        print("Your current word", '_'.join(self.current_word),"\n")
        for i in range(5):
            for j in range(8):
                print(self.display_arr[i][j], end = '')
            print()
        print("\n")

        
    #update current word to accomodate guess (from index array)         
    def change_word(self, idx_arr, guess):
        for val in idx_arr:
            self.current_word[val] = guess


    #driver function that generates index array and updates current word/notes error
    def set_choice(self, guess):
        idx_arr = self.find_all(self.secret_word, guess)
        if(idx_arr == []):
            self.change_error()
        else:
            self.change_word(idx_arr, guess)

        self.display()
        
        
    #check if game is over (win/lose)            
    def check(self):
        if(self.n_wrong >= 6):
            print("\nGame over!")
            print("\nSecret word is: ",self.secret_word)
            
            from PyDictionary import PyDictionary
            dictionary=PyDictionary()
            print("Which means,",dictionary.meaning(self.secret_word))
            
            return False
        
        elif(self.secret_word == ''.join(self.current_word)):
            print("\nYou win!")
            return False
        
        return True #game not over yet
        
        
    #check for repeat guesses
    def guess_check(self, guess_char):
        char_num = ord(guess_char) - 96
        if self.guess_list[char_num] == False:
            self.guess_list[char_num] = True
            return True #new letter
        return False #letter has been repeated
    

    #note that hint has been called - utility function for timer
    def hint_timer(self):
        print("\nDo you need a hint? [y/n]")
        self.hint_flag = 1
        

    #generate hint        
    def hint(self):
        from random import choice
        not_guessed = list(set(self.secret_word) - set(self.current_word))
        letter = choice(not_guessed)
        
        idx_arr = self.find_all(self.secret_word, letter)
        self.change_word(idx_arr, letter)
        
        print("Hint --> ",'_'.join(self.current_word),"\n")
        
   
    
        


if __name__ == '__main__':

    run = True
    obj = Hangman() #initialise object
    obj.secret() #generate secert word
    from threading import Timer


    while(run):


        timeout = 2 #time(seconds) before 'need hint?' prompt
        t = Timer(timeout, obj.hint_timer, args = ())

        t.start() #start timer thread
         
        guess = input("Make a choice: ")
        while not(len(guess)==1 and guess.isalpha()):
            guess = input("Choose a letter: ") #store first user input
        guess = guess.lower()

        if(obj.hint_flag == 1): #if timer elapsed and hint was summoned
            obj.hint_flag = 0

            while not(len(guess)==1 and guess.isalpha() and (guess == 'y' or guess == 'n')): #guess validation
                guess = input("Choose [y/n]: ")

            if(guess == 'y' or guess == 'Y'):
                obj.hint()
                if not(obj.check()): #check if word was completed (for hints asked on the last letter)
                    break


            guess = input("Make a choice: ") #reset guess value for input
            while not(len(guess)==1 and guess.isalpha()):
                guess = input("Choose a letter: ") #main guess after hint prompt
            guess = guess.lower()
            
        t.cancel() #stop timer thread
        

        while not obj.guess_check(guess): #new guess validation
            guess = input("Make a new choice: ")
            while not(len(guess)==1 and guess.isalpha()):
                guess = input("Choose a new letter: ")
        
        obj.set_choice(guess)
        
        run = obj.check()

