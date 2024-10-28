
class avatar:
    def __init__(self, name):
        self.name = name
        self._avatar_state = False

    def enter_avatar_state(self):
        self._avatar_state = True
        return f"{self.name} has enter the avatar state"
    
    def leave_avatar_state(self):
        self._avatar_state = False
        return f"{self.name} has exited the avatar state"
    
aang = avatar("Aang")
aang_gets_angry = aang.enter_avatar_state()
print(aang_gets_angry)

aang_calms_down = aang.leave_avatar_state()
print(aang_calms_down)