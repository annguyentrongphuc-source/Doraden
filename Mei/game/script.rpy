## script.rpy — Main Entry Point
## Mei — Alien Giữa Loài Người
## A Visual Novel retold from Mai's perspective

## ============================================================
## TITLE SCREEN & INTRO
## ============================================================

label splashscreen:
    scene black with fade
    pause 0.5

    show text "{size=60}{color=#b388ff}\"Đôi khi, kẻ đeo mặt nạ hoàn hảo nhất\n chính là người cô đơn nhất.\"{/color}{/size}" with dissolve
    pause 3.0
    hide text with dissolve
    pause 0.5
    return

## ============================================================
## GAME START
## ============================================================

label start:

    ## Reset all variables
    $ facade = 50
    $ empathy = 50
    $ self_worth = 50
    $ vy_relationship = 0
    $ pi_bond = 0
    $ huong_bond = 0
    $ cheated_on_test = False
    $ helped_pi = False
    $ helped_huong = False
    $ explored_clones = False
    $ confronted_vy = False
    $ flashback_seen = False
    $ secret_ending_unlocked = False
    $ clone_meme = False
    $ clone_vent = False
    $ clone_art = False
    $ clone_music = False
    $ clone_deep_web = False

    scene black with fade
    pause 0.5

    ## --------------------------------------------------------
    ## NARRATOR INTRO — Breaking the 4th wall (from original script)
    ## --------------------------------------------------------

    narrator_voice "*khụ khụ* E... hèm..."
    narrator_voice "Tui không định nói điều này, nhưng đây chỉ là một bộ phim về những con người bình thường có cuộc sống bình thường."
    narrator_voice "Nói chung nó rất là bình thường nên đừng mong đợi quá nhiều."
    narrator_voice "Dù sao thì... cứ coi đi."

    ## Scene: School exterior (slow-mo pan)
    scene black
    ## [BG: bg school_exterior — add later]
    scene_desc "Ánh nắng buổi sáng chiếu rọi qua hành lang trường. Những tán cây xanh rì rào theo gió."

    narrator_voice "Yup... Đây, một cái intro lờn con mắt."
    narrator_voice "Và đoán xem tiếp theo là gì nào, giới thiệu nhân vật chính..."
    narrator_voice "Đợi tí... hm..."

    ## TWIST — Instead of showing Vy first (like the original),
    ## we start INSIDE Mai's head

    narrator_voice "Cô ấy đây rồi."

    ## [SPRITE: mei neutral — add later]
    scene_desc "Một cô gái bước qua cổng trường. Lưng thẳng, áo quần chỉn chu, nụ cười nhẹ hoàn hảo đến từng milimet."

    narrator_voice "Nhìn dáng người ấy xem. Khuôn mặt thật đẹp đẽ."
    narrator_voice "Từ dáng đi cho đến thần thái rạng ngời khiến ai cũng ngước nhìn."
    narrator_voice "Đúng là một hình mẫu nhân vật chính cho mọi bộ phim."

    pause 0.5

    narrator_voice "Nhưng nè..."
    narrator_voice "Bây giờ bây bị gạt rồi, teehee."
    narrator_voice "Vì lần này... chúng ta sẽ nhìn thế giới qua đôi mắt CỦA CÔ ẤY."

    scene black with fade
    pause 0.3

    show text "{size=80}{color=#e891b9}Chương 1{/color}\n\n{size=40}{color=#b388ff}Mặt Nạ Hoàn Hảo{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve

    jump chapter1_start

## ============================================================
## INTER-CHAPTER ROUTING
## ============================================================

label chapter1_end:
    $ chapter1_done = True
    scene black with fade
    show text "{size=80}{color=#e891b9}Chương 2{/color}\n\n{size=40}{color=#b388ff}Sau Lớp Vỏ{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve
    jump chapter2_start

label chapter2_end:
    $ chapter2_done = True
    scene black with fade
    show text "{size=80}{color=#e891b9}Chương 3{/color}\n\n{size=40}{color=#b388ff}Cỗ Máy Ảnh{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve
    jump chapter3_start

label chapter3_end:
    $ chapter3_done = True
    scene black with fade
    show text "{size=80}{color=#e891b9}Chương 4{/color}\n\n{size=40}{color=#b388ff}Vỡ Mộng{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve
    jump chapter4_start

label chapter4_end:
    $ chapter4_done = True
    scene black with fade
    show text "{size=80}{color=#e891b9}Chương 5{/color}\n\n{size=40}{color=#b388ff}Kết Nối{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve
    jump chapter5_start

label chapter5_end:
    $ chapter5_done = True
    scene black with fade
    show text "{size=80}{color=#e891b9}Chương 6{/color}\n\n{size=40}{color=#b388ff}Alien Giữa Loài Người{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve
    jump chapter6_start

label chapter6_end:
    $ chapter6_done = True
    scene black with fade
    show text "{size=80}{color=#e891b9}Chương cuối{/color}\n\n{size=40}{color=#b388ff}Bình Minh{/color}{/size}{/size}" with dissolve
    pause 2.5
    hide text with dissolve
    jump chapter7_start
