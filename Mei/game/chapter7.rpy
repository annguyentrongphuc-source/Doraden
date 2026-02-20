## chapter7.rpy — Chương cuối: Bình Minh (Dawn)
## ============================================================
## Multiple endings based on accumulated choices.
## 7 endings determined by facade, empathy, self_worth.
## ============================================================

label chapter7_start:

    ## --------------------------------------------------------
    ## MORNING — THE LAST DAY
    ## --------------------------------------------------------

    ## [BG: bg mei_room_morning — Morning light, warm]
    scene_desc "Sáng. Ánh nắng xuyên qua rèm cửa."
    scene_desc "Mei mở mắt. Nhìn trần nhà."

    mei_inner "Hôm nay là... Hôm nay."
    mei_inner "Không phải ngày mai. Không phải hôm qua."
    mei_inner "Hôm nay."

    scene_desc "Mei ngồi dậy. Nhìn vào gương."

    mei_inner "Chào, Mai."
    mei_inner "Mày trông... Khác."
    mei_inner "Không phải vì tóc hay quần áo."
    mei_inner "Mà vì... Đôi mắt."
    mei_inner "Đôi mắt hôm nay... Có gì đó sống."

    ## --------------------------------------------------------
    ## ROUTING TO ENDINGS
    ## Based on 3 axes: facade, empathy, self_worth
    ## --------------------------------------------------------

    ## Calculate ending
    ## Note: facade starts at 50, empathy at 50, self_worth at 50

    ## SECRET ENDING — requires exploring all 5 clone accounts
    if secret_ending_unlocked and empathy >= 60 and self_worth >= 55:
        jump ending_secret

    ## TRUE ENDING — high empathy, high self_worth, low facade
    if empathy >= 75 and self_worth >= 70 and facade <= 30:
        jump ending_true

    ## BITTERSWEET — high empathy, mid self_worth
    if empathy >= 65 and self_worth >= 50 and self_worth < 70:
        jump ending_bittersweet

    ## UNEXPECTED BOND — max vy_relationship
    if vy_relationship >= 50 and empathy >= 60:
        jump ending_bond

    ## RIVAL — high facade, high self_worth I
    if facade >= 70 and self_worth >= 55:
        jump ending_rival

    ## LONER — high facade, low empathy
    if facade >= 60 and empathy <= 40:
        jump ending_loner

    ## BREAKING POINT — low self_worth, low empathy
    if self_worth <= 30 and empathy <= 35:
        jump ending_breaking

    ## DEFAULT BITTERSWEET if nothing else matches
    jump ending_bittersweet

    ## ============================================================
    ## ENDING 1: TRUE ENDING — "Maitopia Is Here"
    ## ============================================================

label ending_true:

    show text "{size=60}{color=#e891b9}Kết thúc thật\n\n{size=30}{color=#b388ff}Maitopia Is Here{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg school_rooftop — Rooftop, sunrise]
    scene_desc "Sân thượng trường. Bình minh."
    scene_desc "Mei đứng ở đó. Gió thổi tóc bay."

    mei_inner "Mình đã lên sân thượng bao lần."
    mei_inner "Để trốn. Để khóc. Để lướt clone accounts."
    mei_inner "Nhưng hôm nay... Mình lên đây để..."

    scene_desc "Tiếng bước chân phía sau."

    vy "Ê. Lên sớm vậy?"

    scene_desc "Vy đang đứng ở cầu thang, tay cầm hai hộp sữa."

    mei "... Mày sao biết mình ở đây?"
    vy "*nhún vai* Tao cũng hay lên đây ngủ gật. Gặp thì gặp thôi."
    vy "*đưa hộp sữa* Nè."
    mei "... Cám ơn."

    scene_desc "Hai người ngồi trên sân thượng. Nhìn bình minh."
    scene_desc "Im lặng. Nhưng dễ chịu."

    vy "Ê Mai."
    mei "Hm?"
    vy "Tao... Biết mày không phải lúc nào cũng 10 điểm."
    mei "... Biết rồi."
    vy "Và tao biết mày cũng không phải lúc nào cũng ổn."
    mei "..."
    vy "Nhưng mày biết không? Tao cũng vậy."
    vy "4 điểm hoài mà cũng chẳng chết ai."

    mei "*bật cười*"

    vy "Nè, tao có cái máy ảnh lạ lắm. Muốn biết bản chất thật của mày không?"
    mei "... Thôi."
    vy "Hả?"
    mei "*mỉm cười* Tui tự biết rồi."

    scene_desc "Vy nhìn Mei. Mei nhìn bình minh."

    mei_inner "Maitopia."
    mei_inner "5 năm... Mình tự xây một hành tinh cô đơn."
    mei_inner "Và bây giờ..."
    mei_inner "Maitopia không cần phải là nơi mình trốn nữa."
    mei_inner "Vì Maitopia... Ở ngay đây."
    mei_inner "Trên sân thượng trường, với hộp sữa, với bình minh."
    mei_inner "Và với một đứa con gái bình thường nhất thế giới."
    mei_inner "Bình thường... Nhưng nhìn thấy mình."

    mei "Vy."
    vy "Hm?"
    mei "... Mình đang cười."
    vy "Thấy rồi."
    mei "Không. Ý tui là... Cười thật."
    vy "*cười* Biết mà."

    scene black with fade
    scene_desc "Ánh nắng bình minh tràn qua."
    scene_desc "Và ở đâu đó trong ánh sáng đó..."
    scene_desc "Một cô gái alien... Cuối cùng cũng tìm thấy nhà."

    show text "{size=40}{color=#e891b9}\"Có khi... Nhà không phải một nơi.\nNhà là khi ai đó nhìn thấy mày — thật sự thấy —\nvà không bỏ đi.\"{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## ENDING 2: BITTERSWEET — "The Alien Learns to Land"
    ## ============================================================

label ending_bittersweet:

    show text "{size=60}{color=#e891b9}Kết thúc\n\n{size=30}{color=#b388ff}Alien Học Cách Hạ Cánh{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg school_hallway — Hallway, morning]
    scene_desc "Hành lang trường. Buổi sáng. Bình thường."

    mei_inner "Hôm nay mình vẫn đeo mặt nạ."
    mei_inner "Nhưng nó nhẹ hơn. Mỏng hơn."
    mei_inner "Và có... Vết nứt."

    scene_desc "Mei đi ngang Vy. Gật đầu."
    scene_desc "Vy gật lại."

    mei_inner "Mình chưa sẵn sàng để bỏ mặt nạ."
    mei_inner "Mình chưa sẵn sàng để là bạn ai đó."
    mei_inner "Nhưng mình đã sẵn sàng để... Thử."

    scene_desc "Mei mở điện thoại. Clone account #2 — acc vent."
    scene_desc "Gõ: 'Hôm nay mình gật đầu chào ai đó. Và mình cảm thấy... Okay.'"

    mei_inner "Alien chưa hạ cánh."
    mei_inner "Nhưng alien đã bay thấp hơn."
    mei_inner "Đủ thấp để thấy... Mặt đất cũng không tệ."

    show text "{size=40}{color=#e891b9}\"Chữa lành không phải một khoảnh khắc.\nNó là từng bước nhỏ. Từng vết nứt.\nTừng nụ cười thật giữa nghìn nụ cười giả.\"{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## ENDING 3: LONER — "Fortress Intact"
    ## ============================================================

label ending_loner:

    show text "{size=60}{color=#e891b9}Kết thúc\n\n{size=30}{color=#b388ff}Pháo Đài Vẫn Đứng Vững{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg mei_room_night — Room, dark, screens glowing]
    scene_desc "Đêm. Phòng Mei. 9 tab clone. Mì tôm. Deep web."

    mei_inner "Mọi thứ trở lại bình thường."
    mei_inner "Vy — vẫn bình thường. Mình — vẫn hoàn hảo."
    mei_inner "Không ai biết. Không ai thấy."

    scene_desc "Mei cuộn feed. Meme. Vent. Art."

    mei_inner "Pháo đài vẫn đứng vững."
    mei_inner "Mặt nạ vẫn dính chặt."
    mei_inner "Và Maitopia... Vẫn cô đơn."

    mei_inner "An toàn."
    mei_inner "... Cô đơn."
    mei_inner "Nhưng an toàn."

    scene black with fade
    show text "{size=40}{color=#e891b9}\"Có những người chọn sự an toàn\nhơn sự tự do.\nVà ai dám nói họ sai?\n\n...Nhưng ai dám nói họ hạnh phúc?\"{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## ENDING 4: BREAKING POINT — "Cracked Mirror"
    ## ============================================================

label ending_breaking:

    show text "{size=60}{color=#e891b9}Kết thúc\n\n{size=30}{color=#b388ff}Gương Vỡ{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg bathroom — School bathroom, dim]
    scene_desc "Toilet trường. Gương. Nước chảy từ vòi."

    scene_desc "Mei nhìn vào gương. Nhưng không thấy mình."

    mei_inner "Mình là ai?"
    mei_inner "Mặt nạ vỡ rồi. Nhưng bên dưới..."
    mei_inner "Mình không tìm thấy gì."
    mei_inner "Không có alien. Không có Mai Trần. Không có ai."

    scene_desc "Nước mắt chảy. Nhưng Mei không lau."

    mei_inner "5 năm xây pháo đài..."
    mei_inner "Và khi nó sụp..."
    mei_inner "Mình chìm theo."

    scene_desc "Tiếng chuông reo từ xa. Lớp bắt đầu."
    scene_desc "Mei vẫn đứng trước gương."

    mei_inner "..."
    mei_inner "Mình cần giúp đỡ."
    mei_inner "Mình cần... Ai đó."
    mei_inner "Nhưng mình không biết cách xin."

    scene black with fade

    scene_desc "..."
    scene_desc "Ngoài hành lang, bước chân dừng lại trước cửa toilet."
    scene_desc "Tiếng gõ nhẹ."

    vy "*qua cửa* Ê. Mai. Tui biết mày ở đây."
    vy "... Không cần nói gì. Tui đứng đây thôi."

    mei_inner "..."
    mei_inner "Ai đó... Ở đây."

    show text "{size=40}{color=#e891b9}\"Đôi khi... Vỡ là bước đầu để xây lại.\nNhưng mình không cần xây một mình.\nVà việc nhận ra điều đó...\nlà bước khó nhất.\"{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## ENDING 5: RIVAL — "Better Than You"
    ## ============================================================

label ending_rival:

    show text "{size=60}{color=#e891b9}Kết thúc\n\n{size=30}{color=#b388ff}Giỏi Hơn Mày{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg classroom — Classroom, competitive]
    scene_desc "Lớp học. Bài kiểm tra mới."

    mei_inner "10 điểm. Thật. Lần này THẬT."
    mei_inner "Mình ôn cả đêm. Mình biết hết. Mình làm được."

    scene_desc "Mei nhìn xuống bài kiểm tra. 10 điểm. Thật sự."

    mei_inner "Thấy chưa? Mình GIỎI. Mình không cần gian lận."
    mei_inner "Mình không cần Vy. Không cần Pi. Không cần ai."
    mei_inner "Mình là Mai Trần. Top 1."

    scene_desc "Mei đứng dậy. Đi ngang Vy."

    mei "Ê Vy. Lần này 10 điểm thiệt nè. *giơ bài lên*"
    vy "*nhìn* ... Chúc mừng."
    mei "Lần sau cố lên nha. *nháy mắt*"

    mei_inner "..."
    mei_inner "Nụ cười chiến thắng."
    mei_inner "Nhưng sao..."
    mei_inner "Sao nó không vui như mình tưởng?"

    scene_desc "Mei đi về chỗ. Ngồi xuống."

    mei_inner "10 điểm. Hoàn hảo. Thật."
    mei_inner "Nhưng cô đơn."
    mei_inner "... Kệ."
    mei_inner "Mình không cần ai hiểu."
    mei_inner "Mình chỉ cần... Giỏi hơn."

    show text "{size=40}{color=#e891b9}\"Chiến thắng trong cô đơn\nvẫn là chiến thắng.\n... Phải không?\"{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## ENDING 6: UNEXPECTED BOND — "The Old Soul & The Ordinary Girl"
    ## ============================================================

label ending_bond:

    show text "{size=60}{color=#e891b9}Kết thúc\n\n{size=30}{color=#b388ff}Linh Hồn Già & Cô Gái Bình Thường{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg cafe — Small café after school]
    scene_desc "Quán cà phê nhỏ ven đường. Sau giờ học."

    scene_desc "Mei và Vy ngồi đối diện. Trước mặt — 2 ly trà sữa."

    mei "Mày uống trà sữa mỗi ngày thật hả?"
    vy "Ừ. Sữa tươi trân châu. Không thay đổi."
    mei "*nhìn* Bình thường ghê."
    vy "Cám ơn. *nhấp*"

    mei_inner "... Mình đang ngồi quán cafe với Vy."
    mei_inner "MAI TRẦN đang ngồi quán cafe với VY."
    mei_inner "The Perfect Girl và The Ordinary Girl."
    mei_inner "... Và mình đang vui."

    vy "Nè. Tao muốn hỏi..."
    mei "Hm?"
    vy "Mày... Lúc nào cũng cười kiểu đó hả? Kiểu... Hoàn hảo."
    mei "..."
    vy "Vì tao thấy hôm trước mày cười khác. Hơi xấu. Méo méo."
    vy "Nhưng... Real hơn."
    mei "..."
    mei "... Vy."
    vy "?"
    mei "Mày biết... Tui có 9 cái acc clone không?"
    vy "*phun trà sữa* GÌ???"
    mei "*bật cười—cười xấu, cười méo, cười thật* 9 ACC! MỖI CÁI MỘT TÍNH CÁCH!"
    vy "TRỜI ƠI! Psycho!"
    mei "BIẾT RỒI!"

    scene_desc "Cả hai cười. Cười to. Cười xấu."
    scene_desc "Cả quán nhìn."
    scene_desc "Mà kệ."

    vy "Okay tao cần nghe hết 9 acc đó."
    mei "*lau mắt vì cười* Deal."
    vy "Và... Mai?"
    mei "Hm?"
    vy "Cười kiểu méo méo... Đẹp hơn 10 điểm."
    mei "..."
    mei "*nhỏ giọng* ... Cám ơn."

    scene_desc "Trà sữa. Nắng chiều. Tiếng cười."
    scene_desc "Hai cô gái — một alien, một bình thường — ngồi cùng nhau."
    scene_desc "Và lần đầu tiên, cả hai đều thấy: Bình thường mới là đặc biệt."

    show text "{size=40}{color=#e891b9}\"Đôi khi tình bạn không bắt đầu bằng sự tương đồng.\nMà bằng việc ai đó nói: 'Mày weird lắm.'\nVà mày đáp: 'Ừ. Muốn uống trà sữa không?'\"{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## ENDING 7: SECRET — "Clone #10"
    ## ============================================================

label ending_secret:

    show text "{size=60}{color=#e891b9}Kết thúc bí mật\n\n{size=30}{color=#b388ff}Clone Số 10{/color}{/size}{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    ## [BG: bg mei_room_night — Room, but brighter than usual]
    scene_desc "Phòng Mei. Đêm. Nhưng đèn bật sáng — tất cả đèn."

    mei_inner "9 clone accounts."
    mei_inner "9 mảnh linh hồn."
    mei_inner "Meme. Vent. Art. Music. Deep web."
    mei_inner "Backup. Ghost. Diary. Random."
    mei_inner "Và... Mình."

    scene_desc "Mei ngồi trước laptop. Nhìn 9 tab."

    mei_inner "Suốt bao lâu nay... Mình chia bản thân thành 9 phần."
    mei_inner "Mỗi phần sống trên một tab riêng."
    mei_inner "Không ai thấy toàn bộ."
    mei_inner "Kể cả mình."

    scene_desc "Mei đóng tab 1. Tab 2. Tab 3."
    scene_desc "Tab 4. Tab 5. Tab 6."
    scene_desc "Tab 7. Tab 8."
    scene_desc "..."
    scene_desc "Tab 9."

    mei_inner "Không phải xóa. Không phải hủy."
    mei_inner "Chỉ là... Gom lại."

    scene_desc "Mei mở một tab mới. Tab cuối cùng."
    scene_desc "Tạo account mới."
    scene_desc "Username: @mai.tran"
    scene_desc "Bio: 'Alien retired. Just a human now. 🛸→🌍'"

    mei_inner "Clone số 10."
    mei_inner "Không. Không phải clone."
    mei_inner "Đây là... Account chính."
    mei_inner "Account duy nhất."
    mei_inner "Account mà mình thật sự là mình."

    scene_desc "Post đầu tiên:"
    scene_desc "'Hi. Tui là Mai. Tui hay ăn mì lúc 2 giờ sáng, thích deep web, vẽ linh tinh, và khóc khi nghe Saturn.'"
    scene_desc "'Tui không hoàn hảo. Tui không phải alien.'"
    scene_desc "'Tui chỉ là một đứa con gái bình thường.'"
    scene_desc "'Và lần đầu tiên trong đời... Tui thấy okay với điều đó.'"

    scene_desc "Gửi."

    mei_inner "..."
    mei_inner "1 like."

    scene_desc "Vy vừa like."

    mei_inner "*bật cười* Dĩ nhiên rồi."

    scene_desc "Comment: 'welcome to earth, weirdo 🌍😂 —Vy'"

    mei_inner "Welcome to Earth."
    mei_inner "... Mình đã về nhà."

    show text "{size=40}{color=#e891b9}\"9 mảnh linh hồn. 9 bức tường.\n9 lý do để ẩn.\n\nNhưng chỉ cần 1 người nhìn thấy...\nvà nói: 'Welcome.'\n\nĐể biết rằng mình không cần 9 bức tường.\nChỉ cần 1 cánh cửa mở.\"{/color}{/size}" with dissolve
    pause 5.0
    hide text with dissolve

    jump credits

    ## ============================================================
    ## CREDITS
    ## ============================================================

label credits:

    scene black with fade
    pause 1.0

    show text "{size=50}{color=#e891b9}Mei — Alien Giữa Loài Người{/color}{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show text "{size=30}{color=#b388ff}Dựa trên vở kịch sân khấu THPT\n\"Bộ phim bình thường\"\n\nChuyển thể Visual Novel bởi đội ngũ sáng tạo{/color}{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    show text "{size=30}{color=#e891b9}Nhân vật{/color}\n\n{size=24}{color=#fce4ec}Mei (Mai) — Protagonist\nVy — The Ordinary Girl\nDen-Dora — The Robot Cat\nPi — Angel's Voice\nHương — The Girl Who Dared\nThành — The Quiet One\nNarrator — The One Who Breaks Walls{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    show text "{size=30}{color=#b388ff}Story Stats{/color}\n\n{size=24}{color=#e1bee7}Facade: [facade]/100\nEmpathy: [empathy]/100\nSelf-Worth: [self_worth]/100\n\nVy Relationship: [vy_relationship]\nPi Bond: [pi_bond]\nHương Bond: [huong_bond]{/color}{/size}" with dissolve
    pause 5.0
    hide text with dissolve

    show text "{size=40}{color=#e891b9}Cám ơn đã chơi.\n\n{size=24}{color=#b388ff}\"Everybody is a moon, and has a dark side\nwhich he never shows to anybody.\"\n— Mark Twain{/color}{/size}{/color}{/size}" with dissolve
    pause 4.0
    hide text with dissolve

    ## Return to main menu
    return
