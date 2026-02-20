## characters.rpy — Character Definitions for Mei VN
##
## SPRITE GUIDE FOR LATER:
## To add character sprites, place images in game/images/ with naming:
##   mei happy.png, mei sad.png, mei angry.png, mei thinking.png, etc.
##   vy neutral.png, vy laugh.png, vy shocked.png, etc.
##   dendora neutral.png, dendora eating.png, etc.
##   pi sad.png, pi singing.png, etc.
##   huong crying.png, huong happy.png, etc.
##   thanh neutral.png, thanh angry.png, etc.
##   teacher neutral.png
##
## For backgrounds, place in game/images/bg/:
##   bg school_exterior.png, bg classroom.png, bg hallway.png,
##   bg mei_room.png, bg school_yard.png, bg sunset.png, etc.
##
## Ren'Py will auto-detect images matching character names.

## ============================================================
## CHARACTER DEFINITIONS
## ============================================================

## Mai (Mei) — The Protagonist. Player sees her inner thoughts.
## Outer voice: calm, confident, perfect. Inner voice: anxious, sarcastic, vulnerable.
define mei = Character(
    "Mei",
    color="#e891b9",           # Soft pink — her "perfect" exterior
    what_color="#fce4ec",
    who_outlines=[(2, "#880e4f")],
)

## Mei's Inner Voice — Her true thoughts (distinct from dialogue)
define mei_inner = Character(
    "Mei {i}(trong đầu){/i}",
    color="#b388ff",           # Purple — her hidden "alien" self
    what_color="#e1bee7",
    what_italic=True,
    who_outlines=[(2, "#4a148c")],
)

## Vy — The "ordinary girl", energetic, chaotic good
define vy = Character(
    "Vy",
    color="#81d4fa",           # Light blue — simple, bright
    what_color="#e1f5fe",
    who_outlines=[(2, "#01579b")],
)

## Den-Dora — The robot cat from the future (Doraemon parody)
define dendora = Character(
    "Den-Dora",
    color="#ffcc80",           # Orange — quirky, warm
    what_color="#fff3e0",
    who_outlines=[(2, "#e65100")],
)

## Pi — The boy with the "eunuch voice" / Angel's Voice
define pi = Character(
    "Pi",
    color="#a5d6a7",           # Soft green — gentle, vulnerable
    what_color="#e8f5e9",
    who_outlines=[(2, "#1b5e20")],
)

## Hương — The girl with the secret crush
define huong = Character(
    "Hương",
    color="#f48fb1",           # Pink — romantic, emotional
    what_color="#fce4ec",
    who_outlines=[(2, "#880e4f")],
)

## Thành — Hương's friend/crush, quiet and brooding
define thanh = Character(
    "Thành",
    color="#90a4ae",           # Blue-grey — stoic, distant
    what_color="#eceff1",
    who_outlines=[(2, "#263238")],
)

## Teacher — Generic teacher figure
define teacher = Character(
    "Giáo viên",
    color="#fff176",           # Yellow — authority
    what_color="#fffde7",
    who_outlines=[(2, "#f57f17")],
)

## Narrator — 4th-wall-breaking, sarcastic, meta
define narrator_voice = Character(
    "Người kể chuyện",
    color="#80cbc4",           # Teal — omniscient, detached
    what_color="#e0f2f1",
    who_outlines=[(2, "#004d40")],
    what_italic=True,
)

## System/Scene description — No character name
define scene_desc = Character(
    None,
    what_color="#b0bec5",
    what_italic=True,
    what_size=28,
)

## Classmate (generic)
define classmate = Character(
    "Bạn cùng lớp",
    color="#ce93d8",
    what_color="#f3e5f5",
)

## Mai's Mom (appears in flashbacks)
define mom = Character(
    "Mẹ",
    color="#ef9a9a",
    what_color="#ffebee",
    who_outlines=[(2, "#b71c1c")],
)

## ============================================================
## GAME VARIABLES — Choice tracking
## ============================================================

default facade = 50          # 0-100: How tightly Mei clings to her perfect mask
                             # High = doubling down on perfection
                             # Low = letting the mask slip

default empathy = 50         # 0-100: How much Mei connects with others
                             # High = opening up, helping people
                             # Low = isolating, "I don't need anyone"

default self_worth = 50      # 0-100: How Mei values herself beyond grades
                             # High = accepting imperfection
                             # Low = self-hatred, "I'm nothing without grades"

## Relationship trackers
default vy_relationship = 0  # -100 to 100: Rival (-) to Friend (+)
default pi_bond = 0          # 0-100: How much Mei connects with Pi
default huong_bond = 0       # 0-100: How much Mei connects with Hương

## Story flags
default cheated_on_test = False
default helped_pi = False
default helped_huong = False
default explored_clones = False
default confronted_vy = False
default flashback_seen = False
default secret_ending_unlocked = False

## Clone account exploration flags
default clone_meme = False
default clone_vent = False
default clone_art = False
default clone_music = False
default clone_deep_web = False

## Chapter completion tracking
default chapter1_done = False
default chapter2_done = False
default chapter3_done = False
default chapter4_done = False
default chapter5_done = False
default chapter6_done = False
