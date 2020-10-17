# AS39

import random

Ed_Sheeran = ["Lego House", "Give Me Love", "Kiss Me", "One", "Sing", "Thinking Out Loud", "Eraser",
              "Castle on the Hill", "Dive", "Happier"]
Drake = ["Nice For What", "Worst Behaviour", "Hotline Bling", "Marvin's Room", "Work", "Hold On, We're Going Home",
         "Know Yourself", "Feel No Ways", "I'm On One", "0 to 100 / The Catch Up"]
Ariana_Grande = ["Seven Rings", "Rain On Me", "Stuck With U", "God is a woman", "Problem", "Bang Bang",
                 "No Tears Left to Cry", "Break Free", "Into You", "Dangerous Woman"]
Post_Malone = ["Circles", "Sunflower", "Goodbyes", "Better Now", "Wow.", "Take What You Want", "White Iverson",
               "I Fall Apart", "Psycho", "Saint-Tropez"]
Billie_Eilish = ["Bury A Friend", "Bad Guy", "When I Was Older", "Bellyache", "When The Party's Over", "&Burn",
                 "Everything I wanted", "You Should See Me In A Crown", "Copycat", "My Future"]
Taylor_Swift = ["ME!", "Blank Space", "Look What You Made Me Do", "Teardrops On My Guitar", "You Belong With Me",
                "You Need To Clam Down", "We Are Never Ever Getting Back Together", "22", "Delicate",
                "I Don’t Wanna Live Forever"]
Shawn_Mendes = ["There's Nothing Holdin' Me Back", "Treat You Better", "Life Of The Party", "Something Big",
                "If I Can't Have You", "In My Blood", "Lost In Japan", "I Know What You Did Last Summer", "Mercy",
                "Stitches"]
The_Chainsmokers = ["Closer", "Don't Let Me Down", "Something Just Like This", "Takeaway", "Paris", "Roses",
                    "This Feeling", "All We Know", "Call You Mine", "Sick Boy"]
Justin_Bieber = ["Yummy", "Intentions", "Holy", "Love Yourself", "I Don't Care", "What Do You Mean?", "Sorry",
                 "10,000 Hours", "As Long as You Love Me", "Beauty and the Beat"]
The_Weeknd = ["Blinding Lights", "Starboy", "In Your Eyes", "I Feel It Coming", "Call My Name", "I Can't Feel My Face",
              "Earned It", "Save Your Tears", "Heartless", "Pray For Me"]
artistlist = [Ed_Sheeran, Drake, Ariana_Grande, Post_Malone, Billie_Eilish, Taylor_Swift, Shawn_Mendes,
              The_Chainsmokers, Justin_Bieber, The_Weeknd]


def play(artistlist):
    songlist = []
    artlist = ["a", "a"]
    for i in range(20):
        a = random.choice(artistlist)
        while a == artlist[-1] or a == artlist[-2]:
            a = random.choice(artistlist)
        artlist.append(a)
        songlist.append(random.choice(a))
    return songlist


print("\n".join(play(artistlist)))
