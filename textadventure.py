start = '''
One day the main character is at her job, working as a barista,
and she collapses from overworking. She wakes up in this weird
dark room and all she sees is a mystical blue cat standing next
to her. The cat explains that she is currently in this “world” and
in order to escape, she has to help others in this world and find
her purpose of life. The cat asks MC if she is ready to embark on
this journey and MC must choose Yes or No. (types MC’s name in
this part)
'''

left_hallway = '''
MC sees an old farmer frowning about something, Curious, MC goes
over to the farmer and asks him what happened. The farmer explains
that his plants are currently sick because of this slime disease
(the slimes are the virus) and the harvest is about to come soon.
MC is faced with 3 choices:
'''
right_hallway = '''
MC finally sees a pond in the distance and goes over there to rest
for a while. She hears a cry and looks over to find a horse with
very moody, dark and dirty colored hair. The horse says that he
hates himself because he isn’t as pretty as other horses and
everyone teases him. MC is faced with three choices to help the
horse.
'''

common_point = '''
Night has began to come, and MC decides to take another break
where there is nothing except for the rocks . Before MC settles
down on a huge rock, a tiny voice scream “STOPPPP!!” Surprisingly,
MC stood up and saw a tiny rock looking back at her, pouting.
The little rock says “You big people keeps on bullying me. I may
be small but I can beat you up as well.” Behind MC, the big rocks
start laughing loud and mock this poor little rock. The little
rock seems to be scared, her eyes are teary but she is still
trying to fight back. MC shouts “you big immature kids stop it!!”. The big rocks are now laughing at both of them. MC now has 3 choices:
'''
common_point = '''
MC walks for a long time as everything gets darker and darker,
MC gets a little chill. “Do you miss me?” the cat popped out of
nowhere and smiles at MC. I’m surprised you are finally here, can you believe it??” MC is still confuse, the cat continues “Now, I think you have enough clues to summon the little fairy back” MC quickly takes out all of the pieces of quotes and put them together. But somehow nothing happened. “What are you doing, MC??” It’s her mom’s voice!! But still, with a not so good tone, she spats at MC “why do leave me all alone in that house? Are you dumping your mom just like your useless dad as well. You r nothing to me. You either go to me or get out of my house
and live with your terrible dad” (and more insults :D ) MC has 2
choices:
'''

common_point = '''
As her mom vanishes, all the pieces formed into an old drawing
that MC did back when she was still very small, when her parents
were still together, when her family is still a happy family
that is only in her little fairy tale. And the fairy appears,
“I’ve seen that you love and loved by your family. Because of
that, I shall grant you a wish, MC. Do you wish to exit this
world with that old drawing of yours where your reality stays
there. Or will you rather take back your lucky charm and go
to a brand new world where your parents are still together ?
You can only choose once, dear” 
'''


print(start)
done = False
while not done:
    user_input = input("Type 'yes' to go left or 'right' to go right: ")
    if user_input == "left":
        print(left_hallway)
        print(common_point)
        done = True
    elif user_input == "right":
        print(right_hallway)
        print(common_point)
        done = True
    else:
        print("Please type 'left' or 'right'");




red_doorway = '''
You walk into the darkness through the red doorway and immediately get the sensation
that you are falling. You try to scream but can't even hear your own voice. Then
you start to see your things fly past you. Your phone, you favorite pair of shoes,
your favorite toy, pictures from your childhood. You see memories, but you can't
feel them. They are all happening to this other person that looks like you but is
a stranger. You hear your mother's voice, "Why?". Then you hit something.
'''

white_doorway = '''
You walk into the darkness through the white doorway and feel yourself pulled up
like you're in a vacuum, but gently. A soft breeze that smells of vanilla seems
to envelope you and you sense two large hands underneath pushing you up. You weren't
being sucked up but carried up. You hear your mothers voice again, "Why?". Then
you stop.
'''
end_of_story = '''
You're in bed. You stand up in bed and turn off your alarm. It's time to
to start your day. You put on your pair of mismatched slippers, red and white, and
go to the bathroom.
'''

done = False
while not done:
    user_input = input("Type 'red' to go into the red doorway or 'white' to into the white doorway: ")
    if user_input == "red":
        print(red_doorway)
        print(end_of_story)
        done = True
    elif user_input == "white":
        print(white_doorway)
        print(end_of_story)
        done = True
    else:
        print("Please type 'red' or 'white'");
