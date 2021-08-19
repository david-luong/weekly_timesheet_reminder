##Randomise words for weekly timesheet reminder to avoid overthinking.
##Because automated timesheet reminders aren't very effective.
#need to have random and emoji packages installed.

#to enable use of shuffling via random.shuffle to mix up the lists..
import random

#to enable use of emojis via emoji.emojize in our message.
#https://pypi.org/project/emoji/ (pip install emoji --upgrade)
import emoji

#typical phrase structure
#{STARTS} {NOUN}, weekly reminder to submit your timesheets! {EMOJI}

emojis = [':smile:',':blush:',':laughing:',':smiley:',':satisfied:',':heart_eyes:',':grinning:',':innocent:',':grin:']
nouns = ['team','everyone','everybody','all']
starts = ['hi','hello','hey']

#to test emojis are compatible
#for emote in emojis:
#    print(emoji.emojize(emote,use_aliases=True))

#shuffle the respective lists
random.shuffle(emojis)
random.shuffle(nouns)
random.shuffle(starts)

random_string = "{} {}, weekly reminder to submit your timesheets! {}".format(starts[0],nouns[0],emojis[0])

#enable use_aliases=True for full dictionary of emojis
string_with_emojis = emoji.emojize(random_string,use_aliases=True)
bold_string = "\033[1m"+string_with_emojis+"\033[0m"
print(bold_string)
