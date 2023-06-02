import random
import math


def constructVampire(Class, Prior):
    return Monster(round(Class * 2.5), Prior)


class StatBoard:
    def __init__(self, Str, Dex, Con, Int, Wis, Cha):
        self.Str = Str
        self.Dex = Dex
        self.Con = Con
        self.Int = Int
        self.Wis = Wis
        self.Cha = Cha


class Monster:

    def __init__(self, dang, StatsPrior, Class):
        self.Class = Class

        self.Str = round(self.CalculStat(StatsPrior.Str, self.DangClass(dang)))
        self.Dex = round(self.CalculStat(StatsPrior.Dex, self.DangClass(dang)))
        self.Con = round(self.CalculStat(StatsPrior.Con, self.DangClass(dang)))
        self.Int = round(self.CalculStat(StatsPrior.Int, self.DangClass(dang)))
        self.Wis = round(self.CalculStat(StatsPrior.Wis, self.DangClass(dang)))
        self.Cha = round(self.CalculStat(StatsPrior.Cha, self.DangClass(dang)))

        self.AC = round(8 + self.Modifier(self.Dex)/1.2 + min(self.DangClass(dang), 5))
        self.HP = round(
            (self.Modifier(self.Con) * self.DangClass(dang) + random.randint(4, 6 + (StatsPrior.Con + 1) // 3 * 2)) * 5)

        if StatsPrior.Dex <= 3 and StatsPrior.Str <= 3:
            self.Attacks = max(1, round(math.log(self.DangClass(dang), 4)))

            self.DiceNum = max(1, round(math.log(self.DangClass(dang), 4)))
            self.DamageDice = min(12, 6 + 2 * round(math.log(self.DangClass(dang), 5)))

            self.HitDamage = str(self.DiceNum) + "d" + str(self.DamageDice)

        else:
            self.Attacks = max(1, round(math.log(self.DangClass(dang), 2)))

            self.DiceNum = max(1, round(math.log(self.DangClass(dang), 2)))
            self.DamageDice = min(12, 6 + 2 * round(math.log(self.DangClass(dang), 2)))

            self.HitDamage = str(self.DiceNum) + "d" + str(self.DamageDice) + "+" + str(
                max(self.Modifier(self.Str), self.Modifier(self.Dex)))

    def get(self):
        print(" HP: " + str(self.HP) + " AC: " + str(self.AC))
        print(" Str  Dex  Con  Int  Wis  Cha")
        print(" " + self.MakeStr(self.Str) + "  " + self.MakeStr(self.Dex) + "  " + self.MakeStr(
            self.Con) + "  " + self.MakeStr(
            self.Int) + "  " + self.MakeStr(self.Wis) + "  " + self.MakeStr(self.Cha))
        print(" " + self.MakeMod(self.Str) + "  " + self.MakeMod(self.Dex) + "  " + self.MakeMod(
            self.Con) + "  " + self.MakeMod(
            self.Int) + "  " + self.MakeMod(self.Wis) + "  " + self.MakeMod(self.Cha))
        print(" AttacksNum: " + str(self.Attacks) + " Damage: " + self.HitDamage)

    def DangClass(self, dang):
        return dang / 5

    def CalculStat(self, prior, DC):
        return 10 + random.randint(-2, 2) + prior * DC / 5

    def Modifier(self, stat):
        return (stat - 10) // 2

    def MakeStr(self, num):
        res = str(num)
        if len(res) < 3:
            res = " " * (3 - len(res)) + res
        return res

    def MakeMod(self, num):
        num = self.Modifier(num)
        res = str(num)
        if num > 0:
            res = "+" + res
        if len(res) < 3:
            res = " " * (3 - len(res)) + res
        return res

StatPriorBook = {
    "Mage": StatBoard(1, 4, 5, 6, 2, 3),
    "Warior": StatBoard(6, 4, 5, 1, 2, 3),
    "Rogue": StatBoard(2, 6, 5, 4, 3, 1),
    "Cleric": StatBoard(1, 4, 5, 2, 6, 3),
}

MonsterTypes = StatPriorBook.keys()


