start = '''
It's 4 AM and my alarm rings as usual, as it does every day. I wish I could sleep in like every other teenager, but I have to get to work. My parents refuse to pay my college tuition, so I have to work two jobs and attend my classes, all within 24 hours! Tired and sleep-deprived, I get up out of my bed, get dressed and go to work. It feels like a normal day as I take the customers' orders and make them their drinks, when all of a sudden I find myself on the ground and all I can see is darkness...
'''

world = '''
My eyes adjust and the room I'm in comes into focus. I find myself all alone in this room and I have no idea where I am. Suddenly I hear a voice behind me say, "Hi there! Do you know why you're here?" I turn around and see this small, blue cat talking to me. A cat is talking to me. I definitely don't know where I am. He continues, "Do you want to know why you're here? Are you ready to embark on this journey? YES or NO?
'''


firstyes = '''
The cat guides me out of the room, and I find myself in this dark, sad, mysterious world filled my strange fantasy creatures. It looks like my worst nightmare. All of sudden, a butterfly zooms in front of me and steals my necklace. "Hey, that's mine! Give it back to me!" The butterfly turns into a fairy and tells me, "Calm down. I'll give it back, you just need to do something for me. I have this precious item that was broken up into pieces and spread throughout this world. I need you to find those pieces and put them back together. I'll be back when you have completed the task." She disappears, and I turn over to the cat with a bewildered look on my face. The cat, such a helpful creature, disappears, saying, "It's nap time." They both leave me alone on this long, winding path.
'''

firstno = '''
How dare this cat tell me what to do? I need to get out of here and go back to work. Ooh there's a door in the corner, let me leave this weird room. I walk to the door and leave, but find myself in the exact same room with the cat laughing in my face. He asks, "Are you ready to embark on this journey? Let me give you a hint... the correct answer is YES."
'''
print (start)

print (world)
done = False
while not done:
    user_input = input("Type 'yes' to go on the journey or 'no' to ignore the cat: ")
    if user_input == "yes":
        print (firstyes)
        done = True
    elif user_input == "no":
        print(firstno)
    else:
        print("Please type 'yes' or 'no'");

farmer = '''
All by myself, I walk along the path when I see an old farmer frowning about something. Since I have nothing better to do I go over and ask him what happened. He explains to me, "My plants are under attack from the vicious slime viruses and the harvest is about to come soon. If I don't save my plants I won't have any food to give my family. Can you help me?"
'''

secondyes = '''
I'm panicking because I don't know what to do, but I really want to help this farmer. I start singing because that's what I do when I'm stressed. Fortunately, the slimes seem to enjoy my song and start to melt and disappear. Thrilled, the farmer thanks me and gives me two things: a 'fruit-like' object that can change color and a little seashell. I walk back to the path when I find a piece of paper underneath one of the burned plants. I pick it up and I read, "Having a soft heart in a cruel world is courage, not weakness." I scoff and ignore the quote and keep walking.
'''

secondokay = '''
Proud of my amazing idea, I set fire to the slimes. The good thing is, the slime is gone (which is what it was supposed to do), but I kind of, accidentally, not on purpose, killed all of the farmer's plants as well. Oops! The farmer, outraged, strikes me and I black out
and end up in the dark room I was in at the beginning. The cat makes an appearance and says, "It seems like you made the wrong choice, let's give you another try!"
'''

secondno = '''
I walk away from the farmer, feeling a little bad, but in no mood to help this farmer. All of a sudden, a bright light flashes over my eyes and I find myself in the dark room with the cat. He says, "It seems like you made the wrong choice, let's give you another try!"
'''
print (farmer)
done = False
while not done:
    user_input = input("Type 'yes' to help the farmer or 'okay' to set fire on the slime or 'no' to ignore him: ")
    if user_input == "yes":
        print (secondyes)
        done = True
    elif user_input =="okay":
        print (secondokay)
    elif user_input == "no":
        print(secondno)
    else:
        print("Please type 'yes' or 'okay' or 'no'");

unicorn = '''I see a pond in the distance and goes over there to rest for a while. I hear a cry behind me and looks over to find a horse. I think to myself, "Wow, this is one interesting horse. He isn't very... Hmm... what's the word... nice to look at." I ask him what's wrong and he says, "I so sad, and I don't like how I look because I'm not as pretty as the other horses, and everyone teases me." I feel bad about what I thought, and realize that what's inside is more important than how someone looks. Still, the horse is quite sad and I need to help him somehow.
'''

firstbad = '''
I compliment the horse and tell him there's nothing wrong with being alone. Society is never nice to anyone anyways. The horse gets angry and says, "the same goes for you." I think to myself, "Wow he's mean, no wonder he doesn't have any friends." Funnily enough, I soon find myself back in the room with the cat is back in the dark room again.
'''
secondbad = '''
I give the horse the fruit from the farmer and tell him that it will make him look prettier (at least I hope it will). The horse is allergic to it and has a reaction. Well, how was I supposed to know. He gets mad at me and beats me up. I black out and find myself back in the room with the cat.
'''
good = '''
I give him the seashell I got from the farmer since I ave no other idea. When I was giving him the seashell I accidentally drop it into the pond. The shell grows into a beautiful long horn. I take it and put it on top of the horse's head, turning him into a majestic unicorn. Grateful, the unicorn thanks me and gives me three things:  a hammer, a flute, and a book. I also find another piece of paper near the water saying "let love for yourself set you free of them." I sigh and put the paper in my back pocket along with the first paper and continue along.
'''

print (unicorn)
done = False
while not done:
    user_input = input("Type 'society' to tell the unicorn that society or 'fruit' to give him the color-changing fruit or 'seashell' to give him the seashell: ")
    if user_input == "society":
        print (firstbad)
    elif user_input =="fruit":
        print (secondbad)
    elif user_input == "seashell":
        print(good)
        done = True
    else:
        print("Please type 'society' or 'fruit' or 'seashell'");

rock = '''
Night has begins to fall, and I decide to take another break. I'm super tired and sit down on a rock when a tiny voice screams "STOPPPP!!" Surprised, I stand up and see a tiny rock looking back at me, pouting, "You big people keep on bullying me. I may be small but I can beat you up as well." Behind me, the bigger rocks start laughing and mocking this poor little rock. The little rock seems scared, her eyes are teary but she is still trying to fight back. Feeling bad for this rock, I ask the bigger rocks to stop their teasing. They don't stop and start teasing both of us. Now annoyed, I think of what to do to help the rock.
'''

rockbad = '''
I use the hammer the unicorn gave me to break the big rocks into smaller rocks and all the rocks get mad and start attacking me as little pieces, surrounding and crushing me. I wake up back in the dark room with the cat and he gives me another chance.
'''

secondrockbad = '''
I use the flute the unicorn gave me to play music:  The flute plays a super squeaky sound which irritates the rocks even more. They get mad and attack me by crushing me really tightly. I wake up back in the dark room with the cat and he gives me another chance.
'''

rockgood = '''
I use the book the unicorn gave me, but I soon realize that the book is blank, and I don't know what to do. Panicking, I quickly make up a story to tell the rocks. I tell them a story of a beautiful garden, one my mom used to tell me. The rocks thank me for bringing them joy and something to think of instead of picking on the big rocks. I walk away satisfied that I helped solve that dispute. Out of the corner of my eye, I see a little piece of paper in a cave between the big rocks. I pick it up it up and it reads, " there is no love without forgiveness and there is no forgiveness without love". I don't understand and I keep walking on my path.
'''

print (rock)
done = False
while not done:
    user_input = input("Type 'hammer' to break the big rocks or 'flute' to play music or 'book' read the book: ")
    if user_input == "hammer":
        print (rockbad)
    elif user_input =="flute":
        print (secondrockbad)
    elif user_input == "book":
        print(rockgood)
        done = True
    else:
        print("Please type 'hammer' or 'flute' or 'book'");

mom = '''
I walk for a long time as everything gets darker and darker, and I get a little chill. "Did you miss me?" The annoying cat pops out of nowhere and smiles at me. "I'm surprised you're finally here, can you believe it?" I'm confused, but of course the cat continues, "Now, I think you have enough clues to summon the little fairy back" Wanting my bracelet back, I quickly take out all of the pieces of quotes and put them together. I wait for a few seconds but nothing happens. I glare, dryly, at the talking cat. "What are you doing)?" My heart almost jumps out of my chest. It's Mom's voice! I turn around to face her and explain my whole situation but she spats, "Why did you leave me all alone in that house?" Fear creeps into my chest as she continues. "Are you dumping your mom just like your useless dad? Who do you think you are? You are nothing to me. You were nothing but a hinderance to me and that useless father of yours. However, I won't just abandon you. I can give you a choice. You either come live with me or get out of my house and live with your terrible Dad."
'''
badmom = '''
I want to live with both of you guys! I love both of you." I shout out, leaving her mom surprised, "I love you Mom and I love Dad, please don't think of me that way. We're a family, remember! And you know Dad loves you more than I do, so you shouldn't be saying such mean things about him." Mom becomes furious and shouts "So you are on your Dad's side. I took care of you for so many years and this is how you treat me. You have disappointed me. I should have just dumped you to those nuns in the church nearby." Mom runs over to me and chokes me. "Mom..." I gasped and I wake up again with the dark room. The cat is back saying, "You made the wrong choice! Let's start again!"
'''
goodmom = '''
"I love both of you, so I decide to live alone." I stand there crying but smiling at the same time to Mom. "Mom, I know Dad has done many bad things to you, but he still loves you a lot, as much as I do. I know both of you had made  mistakes, and I forgive you. You don't have to worry so much about me anymore. I'll take care of myself." I smile at Mom and she slowly disappear. As she fades away, she mouths, "We are proud of you."
'''

print (mom)
done = False
while not done:
    user_input = input("Type 'live together' to live with both parents or 'live alone' to live by yourself: ")
    if user_input == "live together":
        print (badmom)
    elif user_input =="live alone":
        print (goodmom)
        done = True
    else:
        print("Please type 'live together' or 'live alone'");


finalpuzzle = '''
As Mom vanishes, the final piece of the puzzle appears. All the pieces form into an old drawing that I did back when I was very small, when I was the happiest, when Mom and Dad were still together, when we were a happy family. The fairy appears, and states, "You have had many hardships with your family, yet you contained a kind and unique heart throughout the journey. Because of that, I shall grant you a wish. To get home, you have to choose between the drawing and the bracelet. Choose the drawing, you will go back to the reality of an unloved daughter, but a stronger heart. Choose the bracelet, you will go to another universe where you have different parents, but you will be loved. You can only choose one, Dear."
'''

drawing = '''
 I open my eyes and blink several times. I rub my eyes and realize I'm in a hospital bed. "Was that a dream?" I muse. As I get up slowly, I hear a loud commotion outside the door. "Madam, you cannot go in yet," a female voice, a nurse I presume, says. "What do you mean I can't go in? That is my daughter in there!" Daughter? I look around but it's only me. Could it be? A male voice cut into my thoughts. "Your daughter? She's my daughter too!" The door was then forced opened by Mom and Dad. "Mom...Dad...why are you both here?" I was flabbergast. They both cry out, seeing how I was alright and run over to hug me. "We're sorry to make you this sick. We should have been better as parents." I smile happily and forgive them, "I'm just glad we can be back together as a family." Without talking, we know that we will be together from now on.
'''

charm = '''
I open my eyes and see I'm in a dungeon. I try to get out but my hands are chained. The door opens up and a woman, who I know in my mind is my mother, comes in. She throws me a dress and orders me to dress up. "Time to act like a loving family," my "mother" smiles with an evil grin. Realization dawns on me. Indeed, I did have new parents, and I was "loved".
'''

print (finalpuzzle)
done = False
while not done:
    user_input = input("Type 'drawing' to go back to reality or 'necklace,' to get new parents: ")
    if user_input == "drawing":
        print (drawing)
        done = True
    elif user_input =="necklace":
        print (charm)
        done = True
    else:
        print("Please type 'drawing' or 'necklace'");

print ('The End!!!')
