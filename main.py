import datetime


class Game:
    def __init__(self):
        self.index = {1: 2, 2: 4, 3: 6, 4: 10, 5: 12, 6: 14, 7: 18, 8: 20, 9: 22}
        self.busy_index = []
        self.board = ['+---+---+---+\n',
                      '+', ' 1 ', "+", ' 2 ', "+", ' 3 ', "+\n",
                      '+---+---+---+\n',
                      '+', ' 4 ', '+', ' 5 ', '+', ' 6 ', '+\n',
                      '+---+---+---+\n',
                      '+', ' 7 ', '+', ' 8 ', '+', ' 9 ', '+\n',
                      '+---+---+---+\n']
        self.log = []

    def clearboard(self):
        self.board = ['+---+---+---+\n',
                      '+', ' 1 ', "+", ' 2 ', "+", ' 3 ', "+\n",
                      '+---+---+---+\n',
                      '+', ' 4 ', '+', ' 5 ', '+', ' 6 ', '+\n',
                      '+---+---+---+\n',
                      '+', ' 7 ', '+', ' 8 ', '+', ' 9 ', '+\n',
                      '+---+---+---+\n']
        self.busy_index.clear()

    def checkwin(self, playername1, playername2, counter):
        if self.board[2] == self.board[4] == self.board[6] == ' x ' or \
                self.board[2] == self.board[10] == self.board[18] == ' x ' or \
                self.board[2] == self.board[12] == self.board[22] == ' x ' or \
                self.board[4] == self.board[12] == self.board[20] == ' x ' or \
                self.board[6] == self.board[12] == self.board[18] == ' x ' or \
                self.board[6] == self.board[14] == self.board[22] == ' x ' or \
                self.board[10] == self.board[12] == self.board[14] == ' x ' or \
                self.board[18] == self.board[20] == self.board[22] == ' x ':
            print(f'{playername1} win!')
            print(''.join(self.board))

            self.log.append(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}; {playername1}  vs  {playername2}; {playername1} win! Game - {counter}')
            return "Player1 win"
        elif self.board[2] == self.board[4] == self.board[6] == ' 0 ' or \
                self.board[2] == self.board[10] == self.board[18] == ' 0 ' or \
                self.board[2] == self.board[12] == self.board[22] == ' 0 ' or \
                self.board[4] == self.board[12] == self.board[20] == ' 0 ' or \
                self.board[6] == self.board[12] == self.board[18] == ' 0 ' or \
                self.board[6] == self.board[14] == self.board[22] == ' 0 ' or \
                self.board[10] == self.board[12] == self.board[14] == ' 0 ' or \
                self.board[18] == self.board[20] == self.board[22] == ' 0 ':
            print(f'{playername2} win!')
            print(''.join(self.board))
            self.log.append(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")};   {playername1}  vs  {playername2}; {playername2} win!')
            return "Player2 win"

    def play(self):
        game = True
        counter = 0
        winning = {"Player 1": 0, "Player 2": 0}
        while True:
            print('Menu\n'
                  '1. Play;\n'
                  '2. View log;\n'
                  '3. Exit.\n')
            action = input('Choose action from 1 - 3: ')
            if action == '1':
                playername1 = input('Player 1 please enter your name: ')
                playername2 = input('Player 2 please enter your name: ')
                print(f'{playername1}  vs  {playername2}')
                print('Game start')
                counter += 1
                print(''.join(self.board))
                while game:
                    player1choice = int(input(f'{playername1} choose from 1 - 9: '))
                    if player1choice in range(1, 10) and player1choice not in self.busy_index:
                        self.board[self.index[player1choice]] = ' x '
                        self.busy_index.append(player1choice)
                    if self.checkwin(playername1, playername2, counter) == "Player1 win" or \
                            self.checkwin(playername1, playername2, counter) == "Player2 win":
                        winning["Player 1"] += 1
                        self.clearboard()
                        again = input("Do you want to play again?\n"
                                      "1. Play again\n"
                                      "2. Exit\n")
                        if counter > 1:
                            self.log[-1] += f"[{winning['Player 1']} - {winning['Player 2']}]"
                        if again == "1":
                            print(''.join(self.board))
                            counter += 1
                            continue
                        elif again == "2":
                            counter = 0
                            break
                        else:
                            counter = 0
                            break
                    if len(self.busy_index) == 9:
                        print(f'Draw!')
                        print(''.join(self.board))
                        self.log.append(f'{datetime.datetime.now}; {playername1}  vs  {playername2}; Draw!')

                        self.clearboard()
                        again = input("Do you want to play again?\n"
                                      "1. Play again\n"
                                      "2. Exit\n")
                        if counter > 1:
                            self.log[-1] += f"[{winning['Player 1']} - {winning['Player 2']}]"
                        if again == "1":
                            print(''.join(self.board))
                            counter += 1
                            continue
                        elif again == "2":
                            counter = 0
                            break
                        else:
                            counter = 0
                            break
                    print(''.join(self.board))
                    player2choice = int(input(f'{playername2} choose from 1 - 9: '))
                    if player2choice in range(1, 10) and player2choice not in self.busy_index:
                        self.board[self.index[player2choice]] = ' 0 '
                        self.busy_index.append(player2choice)
                    if self.checkwin(playername1, playername2, counter) == "Player1 win" or \
                            self.checkwin(playername1, playername2, counter) == "Player2 win":
                        winning["Player 2"] += 1

                        self.clearboard()
                        again = input("Do you want to play again?\n"
                                      "1. Play again\n"
                                      "2. Exit\n")
                        if counter > 1:
                            self.log[-1] += f"[{winning['Player 1']} - {winning['Player 2']}]"
                        if again == "1":
                            print(''.join(self.board))
                            counter += 1
                            continue
                        elif again == "2":
                            counter = 0
                            winning["Player 2"] = 0
                            winning["Player 1"] = 0
                            break
                        else:
                            counter = 0
                            break
                    print(''.join(self.board))
            elif action == '2':
                for i in self.log:
                    print(i + '\n')
            elif action == '3':
                break



game = Game()
game.play()

#
# if __name__ == '__main__':
