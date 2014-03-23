Hack Yak
========

My work on reverse engineering Yik Yak's protocol.

This is for everybody to utilize.

1. I am not responsible for what happens on this API.  Don't come crying to me.
2. I don't give a single fuck what happens.

Enjoy.

What is this?
=============

[Yik Yak](http://yikyakapp.com), a geographic based chatting application that allows users to anonymously (not really, all geolocation coordinates are available) post anything for their area. The goal (to my perspective) was to only have college students post bulletins for their college. But, it's actually a terrible service because it's being used for the wrong purpose: high school students cyberbullying.  Ironically, I am a high school student myself and I've already reverse engineered the API.

I documented & posted this API because the creators can't seem to actually go the extra mile to perform college email verification (you, developers, are idiots).

What could I do with this API?
==============================

Good question.

You can do anything the Yik Yak app can do.  You can post messages, upvote messages as well as downvote them.  I must note that there's really no true verification that happens here, it's all crappy PHP scripts all hidden behind SSL.

I'm sure you can figure out if I've used the API or not already, but I will say this is really abusable and can be used to do just about anything as well.  

Want a username on Yik Yak (a handle) without having to ask people to redeem your code? All you need to write some code to redeem your code 4 times from different user IDs and bam.

Want to delete a comment or message off Yik Yak? You can downvote that comment/message so many times (with different user ids) and eventually it'll be ripped off the face of the earth.

Want to know the top Yik Yaks posted in an area? You can exactly do that.  I was planning on making an publicly available service that you were able to pin a specific area/location and get all the top messages in that area, but got too lazy.

I'm giving you all the possibilities because I'm sure nobody will be utilizing this API anytime soon.

Sponsors
========

https://parse.com/ - Yik Yak uses this to host their application.
