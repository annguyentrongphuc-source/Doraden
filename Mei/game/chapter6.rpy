## chapter6.rpy — Chương 6: Alien Giữa Loài Người (Alien Among Humans)
## ============================================================
## NEW chapter. Mai's deep backstory flashback.
## Family pressure, BFF betrayal, building the fortress.
## The turning point: confronting the Alien identity.
## ============================================================

label chapter6_start:

    ## --------------------------------------------------------
    ## PART 1: ĐÊM — THE NIGHTMARE
    ## --------------------------------------------------------

    scene black
    scene_desc "Tối. Mưa. Mei nằm trên giường, mắt mở."

    mei_inner "Tối nay mình không ngủ được."
    mei_inner "Không phải vì deadline. Không phải vì clone accounts."
    mei_inner "Mà vì... Mấy ngày qua."
    mei_inner "Vy. Pi. Hương. Thành."
    mei_inner "Mặt nạ rạn nứt. Vết nứt rộng ra."
    mei_inner "Và bên trong..."
    mei_inner "Mình nghe thấy tiếng. Tiếng từ rất lâu rồi."

    scene black with fade
    scene_desc "Mắt nhắm lại. Và ký ức tràn về."

    ## --------------------------------------------------------
    ## PART 2: FLASHBACK — LỚP 7 (5 NĂM TRƯỚC)
    ## --------------------------------------------------------

    show text "{size=40}{color=#b388ff}5 năm trước...{/color}{/size}" with dissolve
    pause 1.5
    hide text with dissolve

    ## [BG: bg old_classroom — An older, simpler classroom]
    scene_desc "Lớp 7. Trường cấp 2. Dãy bàn cũ kỹ."
    scene_desc "Một cô bé nhỏ xíu, tóc ngắn, cười toe toét. Chạy vào lớp."

    mei_inner "... Đó là mình."
    mei_inner "Mình của 5 năm trước."
    mei_inner "Lúc đó... Mình cười thật."

    scene_desc "Bé Mai chạy tới bàn, ngồi cạnh một cô bé khác — Linh, bạn thân nhất."

    mei_inner "Linh."
    mei_inner "Tên đó... Mình không nhắc tới đã lâu. Rất lâu."

    scene_desc "Hai đứa cười đùa, trao đổi vở, vẽ linh tinh trong tập."

    mei_inner "Tui với Linh — inseparable. Best friends. Kiểu 'chết cũng chết chung.'"
    mei_inner "Mình tin vậy."
    mei_inner "Mình tin... Rằng tình bạn này sẽ mãi mãi."

    ## The Betrayal
    scene_desc "Rồi một ngày..."

    scene_desc "Lớp xì xào. Mấy đứa nhìn Mai, che miệng cười."

    mei_inner "... Gì vậy?"
    mei_inner "Sao mọi người nhìn mình?"

    scene_desc "Bé Mai đi tìm Linh. Linh đang ngồi với nhóm bạn khác. Thấy Mai đi tới, Linh quay mặt đi."

    mei_inner "Linh?"

    scene_desc "Bé Mai nghe thấy tiếng thì thào từ nhóm bạn của Linh."
    scene_desc "'Con đó hả? Nó weird lắm, mày ơi.'"
    scene_desc "'Ừ, Linh nói nó tối ngày lên mạng xem mấy cái creepy.'"
    scene_desc "'Bệnh hoạn.'"
    scene_desc "'Linh nói nó còn lập mấy cái acc ảo nữa. Psycho vậy.'"

    mei_inner "..."
    mei_inner "Linh kể."
    mei_inner "Linh kể cho bọn nó nghe."
    mei_inner "Mọi thứ mình chia sẻ. Mọi bí mật. Mọi thứ 'weird' về mình."
    mei_inner "Mình tin nó. Và nó... Dùng nó để được vào nhóm khác."

    scene_desc "Bé Mai đứng giữa lớp. Mắt ướt. Nhưng không khóc."

    mei_inner "Mình không khóc."
    mei_inner "Lúc đó mình quyết định."
    mei_inner "KHÔNG BAO GIỜ NỮA."
    mei_inner "Không bao giờ cho ai thấy bản thân thật nữa."
    mei_inner "Không bao giờ tin ai nữa."

    scene_desc "Bé Mai bước ra khỏi lớp. Lưng thẳng. Mặt bình thản."
    scene_desc "Và từ ngày đó..."

    mei_inner "Mặt nạ đầu tiên. Version 1.0."
    mei_inner "Rough. Thô ráp. Nhưng hoạt động."

    ## --------------------------------------------------------
    ## PART 3: FLASHBACK — MẸ VÀ ĐIỂM SỐ
    ## --------------------------------------------------------

    scene black with fade
    scene_desc "3 năm trước. Nhà. Bàn ăn."

    ## [BG: bg mei_home — Living room]
    mom "Con! Lại đây!"
    scene_desc "Bé Mai (lớp 9) ngồi trước mặt mẹ. Trên bàn — bảng điểm."
    mom "Sao Toán chỉ có 8?"
    mei "*nhỏ giọng* Con đã cố gắng..."
    mom "Cố gắng? Con Hoa nhà bác Lan 9 điểm! Con Trang 9.5!"
    mom "Mẹ đầu tư cho con học thêm để được 8 điểm hả?"
    mei "..."
    mom "Từ nay mỗi tối ôn thêm 2 tiếng nữa. Cấm điện thoại sau 9 giờ."

    mei_inner "8 điểm."
    mei_inner "8 điểm và mẹ nhìn mình như thể mình là thất bại."
    mei_inner "8 điểm. Trong khi mình thức tới 1 giờ sáng mỗi đêm."
    mei_inner "Nhưng 8 không phải 10. Và mẹ chỉ chấp nhận 10."

    scene_desc "Bé Mai cúi đầu."

    mei_inner "Từ hôm đó... Mình đổi chiến thuật."
    mei_inner "Không chỉ đeo mặt nạ ở trường."
    mei_inner "Mà đeo cả ở nhà."
    mei_inner "Mask version 2.0: Hoàn hảo mọi nơi, mọi lúc."

    ## CHOICE: How does Mei feel about this memory?
    menu:
        mei_inner "Nhìn lại..."

        "Giận mẹ — bà ấy ép mình thành robot":
            $ self_worth += 3
            mei_inner "Mẹ không hỏi mình có vui không."
            mei_inner "Mẹ không hỏi mình có mệt không."
            mei_inner "Mẹ hỏi mình mấy điểm."
            mei_inner "Và mình giận. Giận vì..."
            mei_inner "Vì mình biết bà ấy không xấu. Bà ấy yêu mình."
            mei_inner "Nhưng tình yêu của bà ấy... Có điều kiện."
            mei_inner "Và điều kiện đó là: Hoàn hảo."

        "Hiểu mẹ — bà ấy cũng chỉ biết cách đó":
            $ empathy += 5
            $ self_worth += 2
            mei_inner "Mẹ... Cũng lớn lên bằng điểm số."
            mei_inner "Bà ngoại cũng đối xử với mẹ như vậy."
            mei_inner "Và mẹ của bà ngoại cũng vậy."
            mei_inner "Một chuỗi mặt nạ truyền từ đời này sang đời khác."
            mei_inner "Mình giận... Nhưng cũng thương."
            mei_inner "Vì mẹ cũng là một phiên bản khác của mình."

        "Tự trách — mình yếu nên mới bị ảnh hưởng":
            $ self_worth -= 5
            $ facade += 3
            mei_inner "Mình yếu."
            mei_inner "Mẹ chỉ muốn tốt cho mình. Mà mình không đạt được."
            mei_inner "Nếu mình mạnh hơn... Giỏi hơn... Thông minh hơn..."
            mei_inner "Thì mình sẽ không cần mặt nạ."
            mei_inner "Vì mình sẽ thật sự hoàn hảo."
            mei_inner "... Nhưng mình không phải."

    ## --------------------------------------------------------
    ## PART 4: SỰ RA ĐỜI CỦA ALIEN — THE BIRTH OF MAITOPIA
    ## --------------------------------------------------------

    scene black with fade
    scene_desc "2 năm trước. Đêm. Phòng Mei."

    ## [BG: bg mei_room_night — Room, dark, single screen glow]
    scene_desc "Mei (lớp 10) ngồi trước laptop. 2 giờ sáng. Mắt thâm quầng."

    mei_inner "Linh phản bội 3 năm rồi."
    mei_inner "Mặt nạ cũng 3 năm rồi."
    mei_inner "Mình đã hoàn hảo. Top khối. Thủ quỹ lớp. Ai cũng khen."
    mei_inner "Nhưng..."
    mei_inner "Mình không thấy mình ở bất cứ đâu."
    mei_inner "Ở trường — mình là 'Mai giỏi'. Ở nhà — mình là 'con ngoan'."
    mei_inner "Trên mạng chính — mình là 'idol trường'."
    mei_inner "Nhưng MÌNH là ai?"

    scene_desc "Mei mở một tab mới. Tạo email mới. Username mới."

    mei_inner "Nếu không ai cho mình một nơi để là chính mình..."
    mei_inner "Thì mình sẽ tự tạo."

    scene_desc "Mei gõ: @maitopia_01"

    mei_inner "Maitopia."
    mei_inner "Hành tinh của Mai."
    mei_inner "Nơi mình là Alien."
    mei_inner "Vì nếu mình là Alien... Thì việc không thuộc về đâu là bình thường."
    mei_inner "Vì Alien không cần phải 'thuộc về'. Alien vốn dĩ... Ngoài cuộc."

    scene_desc "Clone số 1 ra đời. Rồi 2. Rồi 3. Rồi 9."

    mei_inner "Mỗi clone là một mảnh linh hồn."
    mei_inner "Mỗi clone là một phần của mình mà thế giới thật không cho phép tồn tại."
    mei_inner "Và tất cả cùng nhau... Tạo thành Maitopia."
    mei_inner "Hành tinh cô đơn. Nhưng an toàn."
    mei_inner "An toàn vì... Không ai ở đó."

    ## --------------------------------------------------------
    ## PART 5: QUAY LẠI HIỆN TẠI — THE PRESENT
    ## --------------------------------------------------------

    scene black with fade
    scene_desc "Hiện tại. Phòng Mei. Đêm."

    mei_inner "5 năm."
    mei_inner "5 năm xây pháo đài. 5 năm đeo mặt nạ."
    mei_inner "Và rồi... Mấy ngày qua... Đổ sạch."

    scene_desc "Mei ngồi dậy. Nhìn laptop — 9 tab clone vẫn mở."

    mei_inner "Vy. Con bé bình thường nhất trường."
    mei_inner "Với cái máy ảnh nhìn thấy sự thật."
    mei_inner "Nó không cần máy ảnh để nhìn mình."
    mei_inner "Nó nhìn thấy điểm thấp của mình. Và nó... Không care."
    mei_inner "Nó nhìn mình giúp Hương. Và nó... Gật đầu."

    ## CHOICE: The pivotal question
    mei_inner "Câu hỏi mà mình trốn chạy 5 năm..."
    menu:
        mei_inner "Hôm nay nó đứng trước mặt mình và không chịu đi."

        "\"Mình có cần cái mặt nạ này nữa không?\"":
            $ facade -= 15
            $ self_worth += 10
            mei_inner "5 năm. Mình đeo nó 5 năm."
            mei_inner "Nó bảo vệ mình. Nó giữ mình an toàn."
            mei_inner "Nhưng nó cũng... Giam mình."
            mei_inner "Giam trong Maitopia. Giam trong 9 clone accounts."
            mei_inner "Giam trong nỗi cô đơn mà mình tự tạo."
            mei_inner "..."
            mei_inner "Nếu Pi — bị ghét vì giọng — tìm thấy thiên thần trong đó..."
            mei_inner "Nếu Hương — sợ mất bạn — vẫn dám thú nhận..."
            mei_inner "Thì mình..."
            mei_inner "Mình có dám..."
            mei_inner "Bỏ mặt nạ xuống?"

        "\"Mình sợ. Sợ quá.\"":
            $ facade += 5
            $ self_worth -= 3
            mei_inner "Mình sợ."
            mei_inner "Sợ vì lần cuối mình để ai thấy bản thân thật..."
            mei_inner "Linh đã dùng nó để hại mình."
            mei_inner "Sợ vì nếu mình bỏ mặt nạ..."
            mei_inner "Đằng sau nó có thể chẳng còn gì."
            mei_inner "Và mình sẽ phải đối mặt với... Hư vô."

        "\"Có lẽ mình không cần chọn. Có lẽ mình vừa đeo vừa bỏ được.\"":
            $ self_worth += 5
            $ empathy += 5
            mei_inner "Hoặc..."
            mei_inner "Mình không cần 'bỏ' hoàn toàn."
            mei_inner "Mình có thể... Để vết nứt ở đó."
            mei_inner "Không vá lại. Nhưng cũng không phá sạch."
            mei_inner "Để ánh sáng vào qua vết nứt."
            mei_inner "Để ai đó — Vy, Pi, Hương — nhìn vào."
            mei_inner "Từng chút. Từng chút một."
            mei_inner "Không phải bỏ hết mặt nạ. Chỉ cần... Hé nó ra."

    ## --------------------------------------------------------
    ## PART 6: ĐỐI THOẠI VỚI ALIEN — TALKING TO HERSELF
    ## --------------------------------------------------------

    scene_desc "Mei đứng trước gương trong phòng tối. Chỉ có ánh đèn laptop chiếu từ phía sau."

    mei_inner "Này. Alien."
    mei_inner "Mày có ở đây không?"

    scene_desc "Bóng phản chiếu trong gương — mờ ảo, không rõ mặt."

    mei_inner "Mày sống trên Maitopia 5 năm rồi."
    mei_inner "Một mình. Trên hành tinh không ai."
    mei_inner "Mày nói mày ổn. Mày nói mày không cần ai."
    mei_inner "Mày nói mày là alien nên không thuộc về đâu cả."

    pause 0.5

    mei_inner "Nhưng mày biết không?"
    mei_inner "Alien cũng có trái tim."
    mei_inner "Alien cũng khóc lúc 3 giờ sáng."
    mei_inner "Alien cũng thèm được ai đó ôm."

    pause 0.5

    mei_inner "Mày không phải alien, Mai."
    mei_inner "Mày là con người."
    mei_inner "Một con người rất mệt, rất sợ, rất cô đơn."
    mei_inner "Nhưng vẫn là con người."

    scene_desc "Trong gương, hình ảnh dần rõ hơn — khuôn mặt Mei, mắt ướt, nhưng miệng đang cười."

    mei_inner "Và con người..."
    mei_inner "Cần nhau."

    ## --------------------------------------------------------
    ## PART 7: QUYẾT ĐỊNH — THE DECISION
    ## --------------------------------------------------------

    scene_desc "Mei nhìn điện thoại trên bàn. Danh bạ. Tên 'Vy'."

    mei_inner "Mình không bao giờ nhắn tin trước."
    mei_inner "Không bao giờ chủ động. Không bao giờ mở lời."
    mei_inner "Vì mở lời = vulnerable. Và vulnerable = nguy hiểm."

    ## CHOICE: The big decision
    menu:
        mei_inner "Nhưng hôm nay..."

        "Nhắn tin cho Vy — \"Ê.\"":
            $ facade -= 15
            $ empathy += 10
            $ vy_relationship += 20
            scene_desc "Mei cầm điện thoại. Tay run."
            scene_desc "Gõ: 'Ê.'"
            mei_inner "Một chữ. Một chữ thôi."
            mei_inner "Nhưng nó nặng hơn 10 bài kiểm tra."
            scene_desc "Gửi."
            scene_desc "..."
            scene_desc "3 phút."
            scene_desc "Điện thoại rung."
            scene_desc "Vy: 'ê. sao? 😶'"
            mei_inner "Nó reply. 3 phút."
            mei_inner "... Bình thường. Tự nhiên. Như thể mình nhắn mỗi ngày."
            scene_desc "Mei nhìn màn hình. Gõ tiếp."
            scene_desc "'Hôm nay... cám ơn.'"
            scene_desc "..."
            scene_desc "Vy: 'cảm ơn cái gì?? 🤔'"
            scene_desc "Mei: '... không biết. nhưng cám ơn.'"
            scene_desc "Vy: 'okay weirdo 😂'"
            scene_desc "Vy: 'btw, mai đi học nhớ mang thêm khăn giấy. hương hay khóc lắm.'"
            scene_desc "Mei: '... 😂'"
            mei_inner "Mình vừa dùng emoji cười."
            mei_inner "Và mình thật sự đang cười."
            mei_inner "... Alien biết dùng emoji rồi."

        "Viết thư — cho bản thân, không gửi cho ai":
            $ self_worth += 10
            $ facade -= 8
            scene_desc "Mei mở Word. Trang trắng."
            scene_desc "Gõ:"
            scene_desc "'Gửi Mai.'"
            scene_desc "'Mày không cần phải hoàn hảo.'"
            scene_desc "'Mày không cần 10 điểm để được yêu.'"
            scene_desc "'Mày không cần 9 clone accounts để tồn tại.'"
            scene_desc "'Mày chỉ cần... Là mày.'"
            scene_desc "'Và mày — với tất cả sự weird, sự mệt mỏi, sự creepy —'"
            scene_desc "'Là đủ.'"
            mei_inner "..."
            mei_inner "Mình chưa bao giờ viết cho mình."
            mei_inner "Mình viết cho hư vô. Viết cho clone accounts."
            mei_inner "Nhưng chưa bao giờ... Cho mình."
            scene_desc "Mei nhìn bức thư trên màn hình. Mắt ướt."
            mei_inner "Mình đủ."
            mei_inner "... Lần đầu tiên mình tin câu đó."

        "Không làm gì — chưa sẵn sàng, nhưng biết ngày đó sẽ đến":
            $ facade += 2
            $ self_worth += 3
            mei_inner "Chưa."
            mei_inner "Mình chưa sẵn sàng."
            mei_inner "Nhưng lần đầu tiên... 'Chưa' không có nghĩa là 'không bao giờ'."
            mei_inner "'Chưa' có nghĩa là... Đang trên đường."
            scene_desc "Mei đặt điện thoại xuống. Nằm lại. Nhắm mắt."
            mei_inner "Ngày mai... Hay ngày kia... Hay tuần sau..."
            mei_inner "Mình sẽ bước ra khỏi Maitopia."
            mei_inner "Nhưng hôm nay... Hôm nay mình cho phép mình nghỉ."

    ## --------------------------------------------------------
    ## TRANSITION TO FINAL CHAPTER
    ## --------------------------------------------------------

    scene black with fade
    pause 1.0

    mei_inner "Đêm đó... Mei ngủ."
    mei_inner "Không có mì tôm. Không có clone accounts. Không có deep web."
    mei_inner "Chỉ có... Giấc ngủ."
    mei_inner "Giấc ngủ đầu tiên... Bình yên."

    pause 1.0

    mei_inner "Và sáng hôm sau..."
    mei_inner "Bình minh."

    jump chapter6_end
