Shakespeare="""Even or odd, of all days in the year,
Come Lammas Eve at night shall she be fourteen.
Susan and she,—God rest all Christian souls!—
Were of an age. Well, Susan is with God;
She was too good for me. But as I said,
On Lammas Eve at night shall she be fourteen;
That shall she, marry; I remember it well.
’Tis since the earthquake now eleven years;"""

Ralph="""The world being thus put under the mind for verb and noun, the poet is he who can articulate it. 
For though life is great, and fascinates, and absorbs; and though all men are intelligent of the symbols through which it is named; 
yet they cannot originally use them. We are symbols and inhabit symbols; 
workmen, work, and tools, words and things, birth and death, all are emblems; 
but we sympathize with the symbols, and being infatuated with the economical uses of things, we do not know that they are thoughts. 
The poet, by an ulterior intellectual perception, gives them a power which makes their old use forgotten, and puts eyes and a tongue into every dumb and inanimate object."""

Shakespeare_list=Shakespeare.split()
Ralph_list=Ralph.split()

for i in Ralph_list:
    if i in Shakespear_list:
        print("общее слово = ",i)
    else:
        print("уникальное слово ",i)
