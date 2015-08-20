# Bingo-Kata
Kata to achieve a Bingo with python and using TDD

You can find the link to the Kata here: <a href="http://agilekatas.co.uk/katas/Bingo-Kata">BingoKata</a>

Here are the description of the kata:

<blockquote>
<p>Bingo is a game of chance played using cards with numbers printed on them, which are marked off of the card as the caller reads out some manner of random numbers. Play usually ceases once a certain pattern is achieved on a card, where the winner will shout out "Bingo!" in order to let the caller and the room know that there may be a winner.

There are lots of different variations of Bingo, each with their own specific rules. Classic US Bingo is perhaps the most well known, where the game is played using a 5x5 grid of numbers between 1 and 75, with a FREE space in the middle. There is also a UK version of Bingo, which uses a 9x3 grid of spaces containing numbers between 1 and 90, of which five spaces on each row are filled in.
</p>
<br/>
    <ul>
        <li>Feature 1: Playing Bingo
            To get the best reach for our Bingo game, we are going to model it on the US version to begin with. To make this work, we are going to need to be able to call out numbers, generate Bingo cards for people to play with, and check their cards when someone calls Bingo. Once we have got these basics in place, we can then start to add new features or tweak the way it works.
        </li>
    </ul>
</blockquote>

# Considerations

I must admit that I have never played Bingo in an oficial way, so I have checked Wikipedia description about the US Bingo ( https://en.wikipedia.org/wiki/Bingo_(U.S.)#The_business_of_bingo ).
Im going to use this approach:
<blockquote>
The range of printed numbers that can appear on the card is normally restricted by column, with the 'B' column only containing numbers between 1 and 15 inclusive, the 'I' column containing only 16 through 30, 'N' containing 31 through 45, 'G' containing 46 through 60, and 'O' containing 61 through 75.
</blockquote>

<blockquote>
The number of all possible Bingo cards with these standard features is P(15,5) × P(15,5) × P(15,5) × P(15,5) × P(15,4)
</blockquote>

I don't know if the numbers in a card can be repeated, but Im going to assume that they cannot be repeated (seems more logical).