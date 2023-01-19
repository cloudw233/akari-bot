from core.builtins.message import MessageSession
from core.component import on_command
from .dice import roll

dice = on_command('dice', alias={'d20': 'dice d20', 'd100': 'dice d100',
                  'd6': 'dice d6'}, developers=['Light-Beacon'], desc='随机骰子',)


@dice.handle('[<dices>] [<dc>] {摇动指定骰子,可指定 dc 判断判定。}',)
async def _(msg: MessageSession):
    dice = msg.parsed_msg.get('<dices>', "D20")
    dc = msg.parsed_msg.get('<dc>', 0)
    await msg.finish(await roll(dice, dc))
