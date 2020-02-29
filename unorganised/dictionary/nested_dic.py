fb_data = {
    40029:{
        "name":"punit",
        "Likes":500,
        "friend_list":600,
        "commments":1500
        }
    ,
    40030:{
        "name":"chinmay",
        "Likes":200,
        "friend_list":900,
        "commments":100,
        "hobbies":["Indoor Game","Reading","Treking"]
        }
    ,
    40031:{
        "name":"steve",
        "Likes":200,
        "friend_list":900,
        "commments":100,
        "hobbies":["Computer gaming","Reading","Treking"]
        }
    }

fb_data[40031].setdefault("color","black")

print(fb_data[40031])
