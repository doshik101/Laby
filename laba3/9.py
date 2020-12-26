R="""The world being thus put under the mind for verb and noun, the poet is he who can articulate it. 
For though life is great, and fascinates, and absorbs; and though all men are intelligent of the symbols through which it is named; 
yet they cannot originally use them. We are symbols and inhabit symbols; 
workmen, work, and tools, words and things, birth and death, all are emblems; 
but we sympathize with the symbols, and being infatuated with the economical uses of things, we do not know that they are thoughts. 
The poet, by an ulterior intellectual perception, gives them a power which makes their old use forgotten, and puts eyes and a tongue into every dumb and inanimate object."""
R=R.split()
slovar={}
for i in R:
    for j in R:
        if i == j:
            count=count+1
            dict[i]=(count)
    count=0
print(dict)
print()
