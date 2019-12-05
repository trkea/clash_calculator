# coding: UTF-8
import json

class ClashCalculator:

    def __init__(self, data_path):
        self.data_path = data_path

    def load_character(self, character_english_name):
        f = open(self.data_path, 'r')
        characters = json.load(f)
        for character in characters:
            if character['english_name'] == character_english_name:
                return character
        return False

    def calc_damage(self, attacker, defencer):
        attack_times = 0
        # アタッカーのタイプ
        UNIT_ATTACK_TYPE = 'ATTACK_TYPE'
        TOWER_ATTACK_TYPE = 'TOWER_ATTACK_TYPE'

        # ディフェンサーのタイプ
        UNIT_TYPE = 'UNIT_TYPE'
        BUILDING_TYPE = 'BUILDING_TYPE'
        SPELL_TYPE = 'SPELL_TYPE'

        #空中属性
        NON_FLY = 0
        ATTACK_ONLY = 1
        FLY = 2

        # 各ユニットがタワーかユニットか判定
        attacker_type = ''
        defencer_type = ''
        if attacker['attack'] == 0:
            attacker_type = TOWER_ATTACK_TYPE
        else:
            attacker_type = UNIT_ATTACK_TYPE
        if defencer['building'] == 1:
            defencer_type = BUILDING_TYPE
        else:
            defencer_type = UNIT_TYPE
        if defencer['hp'] == 0:
            defencer_type = SPELL_TYPE
        
        # 攻撃処理に入らない場合、falseを返す
        if attacker_type is TOWER_ATTACK_TYPE and defencer_type is UNIT_TYPE:
            return False
        if defencer_type is SPELL_TYPE:
            return False
        
        #各ユニットの空中属性から、攻撃に入るかどうかを判定
        if attacker['fly'] == NON_FLY and defencer['fly'] == FLY:
            return False
        
        # 使用する攻撃力を決める
        attack = 0
        if defencer_type is UNIT_TYPE:
            attack = attacker['attack']
        elif defencer_type is BUILDING_TYPE:
            attack = attacker['tower_damage']

        # 登場時ダメージ
        hp = defencer['hp']
        if attacker['first_attack'] != 0:
            hp -= attacker['first_attack']
            attack_times += 1
        
        # 攻撃処理を書く
        while hp > 0:
            hp = hp - attack
            attack_times += 1
        return attack_times

if __name__ == '__main__':
    clash = ClashCalculator('./character.json')
    bowler = clash.load_character('Lava_Hound')
    fisherman = clash.load_character('Lava_Hound')
    times = clash.calc_damage(fisherman, bowler)
    print(times)