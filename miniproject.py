from botoy import Botoy, GroupMsg
from botoy.action import Action
from botoy import FriendMsg
from botoy import refine
from botoy.refine import _group_msg
from botoy import decorators as deco
from rex import rex
bot = Botoy()

test= {
    "toUser": 1043190359,
    "sendToType": 2,
    "groupid": 0,
    "Content": "测试",
    "sendMsgType": "TextMsg",
    "atUser": 0
    
}

'''
@deco.from_these_groups(684033496)
'''

@bot.on_group_msg
@deco.from_these_groups(1043190359,684033496)
def group_(ctx: GroupMsg):
    if ctx.FromUserId != ctx.CurrentQQ and ("元" in ctx.Content):
        Action(ctx.CurrentQQ).sendFriendText(251031557,ctx.Content[:ctx.Content.find(")")]+")/")


@bot.on_group_msg
@deco.from_these_groups(1043190359,684033496)
def group_(ctx: GroupMsg):
    if ctx.FromUserId != ctx.CurrentQQ and ("毛巾" in ctx.Content):
        Action(ctx.CurrentQQ).sendFriendText(101096945,ctx.Content[:ctx.Content.find(")")]+")/")

@bot.on_group_msg
@deco.from_these_groups(1043190359,684033496)
def group_(ctx: GroupMsg):
    if ctx.FromUserId != ctx.CurrentQQ and ("显示器" in ctx.Content):
        Action(ctx.CurrentQQ).sendFriendText(291993554,ctx.Content[:ctx.Content.find(")")]+")/")



'''
@bot.on_group_msg
def group(ctx: GroupMsg):
    if ctx.FromUserId != ctx.CurrentQQ and ctx.Content == '1':
        Action(ctx.CurrentQQ).sendGroupText(2655226230,"1")
'''

@bot.on_friend_msg
def friend(ctx:FriendMsg):
    if ctx.FromUin != ctx.CurrentQQ and ctx.Content == '你好':
        Action(ctx.CurrentQQ).sendFriendText(251031557,ctx.Content)    



if __name__ == '__main__':
    bot.run()