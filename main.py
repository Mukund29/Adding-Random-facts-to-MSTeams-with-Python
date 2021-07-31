import randfacts
import emoji
import pymsteams

new_fact = randfacts.get_fact()

message1 = ("Today's Fact: " + new_fact + "\n\n Disclaimer: Facts are not guaranteed to be true." + "\n\nGood Afternoon Team!!"+ emoji.emojize(":grinning_face_with_big_eyes:"))
"""
Create a channel in your MS teams
Select the more option in channel and choose WebHook
Configure the WebHook to get the MS teams webhook authorization key
Use the Authorization key to send msgs with the below code.
"""

myTeamsMessage = pymsteams.connectorcard("<MS Teams Auth Key>")
myTeamsMessage.text(message1)
myTeamsMessage.send()