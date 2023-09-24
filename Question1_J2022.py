#part 1(a) 
FileData = [["", ""] for i in range(11)]



#part 1(b)
def ReadHighScores():
    File = open("HighScore.txt", "r")
    for i in range(0,11):
        FileData[i][0]=File.readline() [:3]
        FileData[i][1]=File.readline()
        File.close

#part 1 (c)
def OutputHighScores():
    for x in range(0,11):
        print(FileData[x][0], FileData[x][1])



        
ReadHighScores()
OutputHighScores()