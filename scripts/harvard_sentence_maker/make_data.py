#!/usr/bin/env python3

import json

sentences = """The curtain rose and the show was on.
The birch canoe slid on the smooth planks.
Glue the sheet to the dark blue background.
It's easy to tell the depth of a well.
Rice is often served in round bowls.
The box was thrown beside the parked truck.
The source of the huge river is the clear spring.
The salt breeze came across from the sea.
Two blue fish swam in the tank.
The colt reared and threw the tall rider.
It snowed, rained, and hailed the same morning.
Take the winding path to reach the lake.
The wide road shimmered in the hot sun.
Lift the square stone over the fence.
The frosty air passed through the coat.
A saw is a tool used for making boards.
Use a pencil to write the first draft.
A small creek cut across the field.
The dune rose from the edge of the water.
Those words were the cue for the actor to leave.
The ink stain dried on the finished page.
The fruit peel was cut in thick slices.
There are more than two factors here.
The grass curled around the fence post.
Cut the pie into large parts.
A wisp of cloud hung in the blue air.
Oak is strong and also gives shade.
The pipe began to rust while new.
Open the crate but don't break the glass.
The ripe taste of cheese improves with age.
The bark of the pine tree was shiny and dark.
Split the log with a quick, sharp blow.
He ordered peach pie with ice cream.
Weave the carpet on the right hand side.
The cup cracked and spilled its contents.
Pluck the bright rose without leaves.
The young kid jumped the rusty gate.
Guess the results from the first scores.
A salt pickle tastes fine with ham.
These thistles bend in a high wind.
The tree top waved in a graceful way.
The spot on the blotter was made by green ink.
The cigar burned a hole in the desk top.
He broke a new shoelace that day.
The coffee stand is too high for the couch.
The urge to write short stories is rare.
The pencils have all been used.
The sofa cushion is red and of light weight.
The jacket hung on the back of the wide chair.
At that high level the air is pure.
The office paint was a dull sad tan.
Steam hissed from the broken valve.
There was a sound of dry leaves outside.
Torn scraps littered the stone floor.
We admire and love a good cook.
He carved a head from the round block of marble.
Corn cobs can be used to kindle a fire.
Where were they when the noise started.
The paper box is full of thumb tacks.
The petals fall with the next puff of wind.
Bring your best compass to the third class.
A fresh start will work such wonders.
He wrote his last novel there at the inn.
It is hard to erase blue or red ink.
Write at once or you may forget it.
The doorknob was made of bright clean brass.
They took the axe and the saw to the forest.
Jazz and swing fans like fast music.
The map had an X that meant nothing.
Some ads serve to cheat buyers.
On the islands the sea breeze is soft and mild.
Add salt before you fry the egg.
The houses are built of red clay bricks.
Ducks fly north but lack a compass.
He used the lathe to make brass objects.
The vane on top of the pole revolved in the wind.
Let it burn, it gives us warmth and comfort.
A castle built from sand fails to endure.
Tack the strip of carpet to the worn floor.
Pour the stew from the pot into the plate.
Each penny shone like new.
The dirt piles were lines along the road.
The logs fell and tumbled into the clear stream.
Just hoist it up and take it away,
Our plans right now are hazy.
It takes a good trap to capture a bear.
Feed the white mouse some flower seeds.
The thaw came early and freed the stream.
He took the lead and kept it the whole distance.
The key you designed will fit the lock.
This plank was made for walking on.
The lake sparkled in the red hot sun.
He crawled with care along the ledge.
Tend the sheep while the dog wanders.
Mark the spot with a sign painted red.
The fur of cats goes by many names.
Go now and come here later.
Soap can wash most dirt away.
That move means the game is over.
He wrote down a long list of items.
A siege will crack the strong defense.
Roads are paved with sticky tar.
The drip of the rain made a pleasant sound.
Smoke poured out of every crack.
Much of the story makes good sense.
The sun came up to light the eastern sky.
Heave the line over the port side.
A lathe cuts and trims any wood.
It's a dense crowd in two distinct ways.
The desk was firm on the shaky floor.
It takes heat to bring out the odor.
Raise the sail and steer the ship northward.
Jerk the dart from the cork target.
No cement will hold hard wood.
We now have a new base for shipping.
The list of names is carved around the base.
The sheep were led home by a dog.
No hardship seemed to keep him sad.
Once we stood beside the shore.
A chink in the wall allowed a draft to blow.
Fasten two pins on each side.
A cold dip restores health and zest.
The sand drifts over the sill of the old house.
The point of the steel pen was bent and twisted.
There is a lag between thought and act.
Seed is needed to plant the spring corn.
Draw the chart with heavy black lines.
Hats are worn to tea and not to dinner.
The ramp led up to the wide highway.
Beat the dust from the rug onto the lawn.
Say it slowly but make it ring clear.
The straw nest housed five robins.
Screen the porch with woven straw mats.
This horse will nose his way to the finish.
The dry wax protects the deep scratch.
Twist the valve and release hot steam.
The marsh will freeze when cold enough.
They slice the sausage thin with a knife.
The bloom of the rose lasts a few days.
A gray mare walked before the colt.
Breakfast buns are fine with a hot drink.
Bottles hold four kinds of rum.
The man wore a feather in his felt hat.
He wheeled the bike past the winding road.
Drop the ashes on the worn old rug.
The desk and both chairs were painted tan.
Throw out the used paper cup and plate."""


data = {
  "description": "Harvard Sentences - single sentences",
  "source": "https://www.cs.columbia.edu/~hgs/audio/harvard.html",
  "_note": "Please don't use this as an API. I'm posting these so you can pull them down and work with them that way",
  "data": [
sentences.split("\n")
  ]
}

with open("../../site/json-examples/harvard-sentences--single-sentences--2hzdotjpybui/data.json", "w") as _out:
    json.dump(data, _out, sort_keys=True, indent=2)
