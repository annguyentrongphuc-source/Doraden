## chapter1.rpy — Chương 1: Mặt Nạ Hoàn Hảo (The Perfect Mask)
## ============================================================
## Mai's morning, the school facade, the test, teasing Vy.
## We see the anxiety, the perfectionism, the cracks.
## ============================================================

label chapter1_start:

    ## --------------------------------------------------------
    ## PART 1: BUỔI SÁNG — THE MORNING RITUAL
    ## --------------------------------------------------------

    scene black
    with fade

    scene bg/mei_room_dark
    with dissolve

    scene_desc "5:30 sáng. Căn phòng tối om, chỉ có ánh đèn điện thoại nhấp nháy."

    play sound "audio/alarm.ogg"

    mei_inner "..."
    mei_inner "Lại một ngày nữa."

    scene_desc "Bàn tay với lấy điện thoại. Ánh sáng màn hình chiếu lên khuôn mặt mệt mỏi — đôi mắt thâm quầng, tóc rối bù."

    mei_inner "3 tiếng ngủ. Kỷ lục mới. Nên tự hào hay tự thương nhỉ."

    scene bg/mei_room_morning
    with dissolve

    scene_desc "Mei bật đèn. Căn phòng hiện ra — gọn gàng đến ám ảnh. Sách giáo khoa xếp theo thứ tự bìa, bút highlight xếp theo màu cầu vồng."

    mei_inner "Okay. Checklist buổi sáng."
    mei_inner "Rửa mặt. Kem chống nắng. Áo dài — là phẳng từ tối qua."
    mei_inner "Tóc — buộc gọn, không một sợi lạc. Cặp — đủ sách, đủ vở, đủ bút."
    mei_inner "Và quan trọng nhất..."

    show mei neutral at center
    with dissolve

    scene_desc "Mei đứng trước gương. Hít một hơi thật sâu."

    mei_inner "Nụ cười."

    hide mei neutral
    show mei mask_on at center
    with dissolve

    scene_desc "Khóe môi cong lên hoàn hảo. Đôi mắt sáng lên đúng mức. Không quá vui — sẽ trông giả tạo. Không quá nhạt — sẽ khiến người ta hỏi \"sao hôm nay mày buồn vậy?\""

    mei_inner "Hoàn hảo. Như mọi ngày."

    hide mei mask_on
    with dissolve

    ## CHOICE 1: Morning Phone Check
    menu:
        mei_inner "Trước khi đi... check điện thoại tí."

        "Lướt tài khoản chính (Instagram, kiểm tra comments)":
            $ facade += 3
            mei_inner "47 likes. 12 comments. \"Xinh quá Mai ơi!\" \"Học giỏi lại đẹp nữa.\" \"Ước gì được như bạn.\""
            mei_inner "..."
            mei_inner "Ước gì được như mình. Hmm. Ước gì bây biết mình thức tới 3 giờ sáng để có cái ảnh 'tự nhiên' đó."
            mei_inner "Nhưng không. Bọn họ không cần biết. Không ai cần biết."
            $ facade += 2

        "Lướt clone account (acc phụ, xả stress)":
            $ facade -= 3
            $ self_worth += 2
            mei_inner "Okay, clone số 3 — acc meme. Xem có gì mới không..."
            scene_desc "Mei cuộn qua hàng loạt meme về trầm cảm, về việc thức khuya, về Gen Z muốn nghỉ hưu từ năm 20 tuổi."
            mei_inner "*snort* Cái này đúng quá rồi... \"POV: Bạn ngủ 3 tiếng nhưng vẫn phải đẹp vào sáng hôm sau.\""
            mei_inner "... Ít nhất ở đây mình được là chính mình. Dù 'chính mình' nghe cũng buồn ghê."

        "Bỏ qua, đi luôn cho lẹ":
            mei_inner "Không. Không có thời gian. Đi thôi."
            mei_inner "Mỗi phút lãng phí là mỗi phút mình có thể bị bắt gặp... không hoàn hảo."

    ## --------------------------------------------------------
    ## PART 2: ĐƯỜNG ĐẾN TRƯỜNG — THE WALK TO SCHOOL
    ## --------------------------------------------------------

    scene black
    with fade

    scene bg/street_morning
    with fade

    scene_desc "Đường phố buổi sáng. Xe cộ qua lại, tiếng rao hàng rong vọng từ xa."

    mei_inner "Bước chân thứ 247 tới trường. Mình đếm mỗi ngày. Không phải vì thích đếm."
    mei_inner "Mà vì nếu không đếm, đầu óc sẽ bắt đầu nghĩ lung tung."
    mei_inner "Nghĩ về bài kiểm tra hôm nay. Nghĩ về mấy cái deadline. Nghĩ về..."
    mei_inner "Thôi. Đếm tiếp. 248. 249. 250."

    scene bg/school_gate
    with fade

    scene_desc "Cổng trường xuất hiện trước mặt. Từng đám học sinh ùa vào, cười nói rôm rả."

    mei_inner "Và... Action."

    show mei neutral at center
    with dissolve

    scene_desc "Như thể có ai bấm nút switch, toàn bộ ngôn ngữ cơ thể của Mei thay đổi trong một giây."
    scene_desc "Lưng thẳng hơn. Bước chân nhẹ nhàng hơn. Nụ cười — ON."

    hide mei neutral
    show mei mask_on at center
    with dissolve

    classmate "Ê Mai! Sáng nay đẹp quá ha!"

    hide mei mask_on
    show mei happy at center
    with dissolve

    mei "Cám ơn nha! *cười* Bữa nay trời đẹp mà, ai cũng đẹp lên hết á."

    mei_inner "Script số 14: \"Khen lại khi được khen.\" Đơn giản. Hiệu quả. Không ai nghi ngờ."

    classmate "Mai ơi, bữa nay kiểm tra Toán ha. Mày ôn chưa?"
    mei "Ôn rồi chứ! Cũng không khó lắm đâu, cố lên nha! *nháy mắt*"

    hide mei happy
    with dissolve

    mei_inner "\"Không khó lắm.\" Mình thức tới 3 giờ sáng. Uống 3 ly cà phê. Gần khóc 2 lần."
    mei_inner "Nhưng đó là chuyện của Mei-bên-trong. Mei-bên-ngoài thì luôn sẵn sàng."

    ## --------------------------------------------------------
    ## PART 3: TRONG LỚP HỌC — THE CLASSROOM
    ## --------------------------------------------------------

    scene bg/classroom
    with fade

    scene_desc "Lớp học sáng rực ánh nắng từ cửa sổ. Tiếng quạt trần xoay đều đều."

    show mei neutral at right
    with dissolve

    scene_desc "Mei bước vào lớp. Đúng tác phong: đến sớm 10 phút, ngồi đúng vị trí, bày sách vở ngay ngắn."

    mei_inner "Pháo đài đã thiết lập. Chiến trường đã sẵn sàng."

    ## Vy enters
    show vy sleepy at left
    with dissolve

    scene_desc "Cánh cửa lớp mở. Một cô gái tóc hơi rối bước vào — ba lô lệch vai, áo hơi nhăn, mặt vẫn còn ngái ngủ."

    mei_inner "Vy."
    mei_inner "Con bé bình thường nhất lớp. Không, có lẽ bình thường nhất trường."
    mei_inner "Sức khỏe — bình thường. Điểm số — bình thường. Quan hệ xã hội — cũng bình thường nốt."

    ## CHOICE 2: Mei's attitude toward Vy
    menu:
        mei_inner "Nhìn nó mà thấy... gì nhỉ?"

        "Ghen tị — Nó không cần cố gắng, không cần mặt nạ, sống sao cũng được":
            $ self_worth -= 3
            $ empathy += 2
            $ vy_relationship += 5

            hide mei neutral
            show mei thinking at right
            with dissolve

            mei_inner "Sao nó có thể sống thoải mái như vậy nhỉ?"
            mei_inner "Không ai kỳ vọng gì ở nó. Không ai soi mói. Nó muốn fail thì fail, muốn ngủ gật thì ngủ."
            mei_inner "... Tự do. Đó là thứ mà mình không bao giờ có."
            mei_inner "Hay đúng hơn... không bao giờ cho phép mình có."

        "Khinh thường — Bình thường thì mãi bình thường, có gì đáng nói":
            $ facade += 3
            $ empathy -= 3
            $ vy_relationship -= 5

            hide mei neutral
            show mei mask_on at right
            with dissolve

            mei_inner "Người ta nói 'bình thường là hạnh phúc'. Nhảm nhí."
            mei_inner "Bình thường là vô hình. Bình thường là không ai nhớ tới mày."
            mei_inner "Ít nhất mình... dù có giả tạo, nhưng mình có tồn tại trong mắt mọi người."
            mei_inner "Còn nó? Không ai thèm nhớ."

        "Thờ ơ — Kệ, không liên quan tới mình":
            hide mei neutral
            show mei thinking at right
            with dissolve

            mei_inner "Whatever."
            mei_inner "Mình có bài kiểm tra phải lo. Không có thời gian nghĩ về người khác."

    hide vy sleepy
    hide mei ## hide whatever mei sprite is showing

    ## --------------------------------------------------------
    ## PART 4: BÀI KIỂM TRA — THE TEST
    ## --------------------------------------------------------

    ## Same classroom, but tense now
    scene bg/classroom
    with vpunch

    scene_desc "Chuông reo. Giáo viên bước vào, tay cầm xấp đề kiểm tra."

    show teacher neutral at left
    with dissolve

    teacher "Mấy em dời bàn ra. Hôm nay kiểm tra 15 phút Toán."

    scene_desc "Lớp xôn xao. Tiếng kéo bàn kĩn kịt."

    hide teacher neutral
    with dissolve

    show mei thinking at center
    with dissolve

    mei_inner "Đây rồi."
    mei_inner "Tim đang đập 120 nhịp/phút. Tay hơi run. Dạ dày co thắt."
    mei_inner "Nhưng không ai được biết. Mặt bình thản. Tay đặt ngay ngắn trên bàn."
    mei_inner "Giống như một con vịt — trên mặt nước thì phẳng lặng, dưới nước thì đạp điên cuồng."

    teacher "Bắt đầu."

    scene_desc "Mei lật đề. Nhìn câu 1."

    mei_inner "..."
    mei_inner "Okay. Câu 1 biết. Câu 2... hmm... Câu 3..."
    mei_inner "Câu 3... Cái này... Hình như phần mình đọc lúc 2 giờ sáng..."
    mei_inner "Mà lúc đó mình đang nửa tỉnh nửa mơ..."

    hide mei thinking
    show mei sad at center
    with dissolve

    scene_desc "Mei cắn bút, nhíu mày. Cánh mũi phập phồng nhẹ."

    mei_inner "Bình tĩnh. BÌNH TĨNH! Mày là Mai Trần. Top 1 lớp. Không, top 1 khối."
    mei_inner "Mày PHẢI biết câu này."

    ## CHOICE 3: How to handle the test
    menu:
        mei_inner "Nhưng mà... không biết thật..."

        "Cố gắng làm bài thật — chấp nhận kết quả":
            $ facade -= 5
            $ self_worth += 5
            $ cheated_on_test = False

            hide mei sad
            show mei neutral at center
            with dissolve

            mei_inner "Không. Mình sẽ làm những gì mình biết. Cái gì không biết thì... thì..."
            mei_inner "Thì... chấp nhận."
            scene_desc "Mei hít một hơi sâu. Bắt đầu viết — chậm, cẩn thận."
            mei_inner "Lần đầu tiên trong đời... cho phép mình không hoàn hảo."
            mei_inner "Cảm giác thật lạ. Như rơi tự do mà không biết bên dưới có lưới hay không."

        "Liếc bài — mình PHẢI được điểm cao, bằng mọi giá":
            $ facade += 5
            $ self_worth -= 5
            $ cheated_on_test = True

            hide mei sad
            show mei mask_on at center
            with dissolve

            mei_inner "Không. KHÔNG ĐƯỢC PHÉP. Mình phải điểm cao."
            mei_inner "Nếu không... Nếu mình chỉ là trung bình... Thì mình còn gì?"
            scene_desc "Mei liếc sang — vừa đủ nhanh, vừa đủ khéo. Năm tháng luyện tập cho phút giây này."
            mei_inner "Đừng nhìn mình với ánh mắt đó. Mọi người đều gian lận. Mình chỉ... giỏi hơn thôi."
            mei_inner "Và không ai được phép biết."

        "Hỏi nhỏ bạn bên cạnh — chỉ gợi ý thôi":
            $ facade += 2
            $ self_worth -= 2
            $ cheated_on_test = True

            hide mei sad
            show mei thinking at center
            with dissolve

            scene_desc "Mei xoay người sang bên cạnh, thì thào."
            mei "Ê... Câu 3... Công thức gì vậy?"
            scene_desc "Bạn bên cạnh liếc giáo viên, rồi vội chỉ."
            mei_inner "Cám ơn. Dù gì thì... mình cũng chỉ cần gợi ý thôi mà."
            mei_inner "... Mình tự dối mình giỏi ghê."

    hide mei
    with dissolve

    ## --------------------------------------------------------
    ## PART 5: KẾT QUẢ — THE RESULTS
    ## --------------------------------------------------------

    scene_desc "15 phút trôi qua. Giáo viên thu bài."
    scene_desc "..."
    scene_desc "Và rồi..."
    scene_desc "Bài kiểm tra được trả lại."

    ## Branch based on cheating
    if cheated_on_test:
        show mei mask_on at center
        with dissolve

        scene_desc "Mei nhìn xuống bài kiểm tra. 10 điểm. Đỏ chói."
        mei_inner "10. Tất nhiên là 10. Luôn luôn là 10."
        mei_inner "..."
        mei_inner "Và luôn luôn là giả."

        hide mei mask_on
        with dissolve
    else:
        show mei sad at center
        with dissolve

        scene_desc "Mei nhìn xuống bài kiểm tra. 7 điểm."
        mei_inner "7."
        mei_inner "Bảy."
        mei_inner "Chỉ... bảy."
        mei_inner "Bảy không phải là tệ. Bảy là khá. Bảy là ổn đối với mọi người."
        mei_inner "Nhưng mình không phải mọi người. Mình là Mai Trần."
        mei_inner "Và 7 điểm... sẽ giết chết mình."

        ## Quick panic
        mei_inner "Nhanh — úp bài xuống. Không ai được thấy."

        hide mei sad
        show mei thinking at center
        with dissolve

        scene_desc "Mei lật úp tờ kiểm tra, tay hơi run."
        mei_inner "Okay. Breathe. Không ai thấy. Mình vẫn an toàn."

        hide mei thinking
        with dissolve

    ## Vy's result
    show vy neutral at left
    with dissolve

    scene_desc "Phía bên kia lớp, Vy đang nhìn bài kiểm tra của mình. 4 điểm."

    hide vy neutral
    show vy shocked at left
    with dissolve

    scene_desc "Vy vò đầu bức tóc, mặt méo xệch."

    vy "*thở dài* Haizzzz!!!"

    ## --------------------------------------------------------
    ## PART 6: KHOẢNH KHẮC GÂY ÁN — THE INTERACTION
    ## --------------------------------------------------------

    ## CHOICE 4: How Mei interacts with Vy about the test
    menu:
        mei_inner "Vy... 4 điểm hả... Mình nên..."

        "Trêu nhẹ — duy trì hình ảnh 'Mei hoàn hảo' (giống script gốc)":
            $ facade += 5
            $ empathy -= 5
            $ vy_relationship -= 10

            hide vy shocked
            show vy neutral at left
            with dissolve

            show mei mask_on at right
            with dissolve

            scene_desc "Mei cầm bài kiểm tra, đi qua chỗ Vy."

            if cheated_on_test:
                mei "Lại thấp điểm nữa à *cười*. Lần sau nhớ cố gắng lên, như tui nè."
                scene_desc "Mei giơ bài 10 điểm lên, vỗ vai Vy nhẹ."

                hide mei mask_on
                show mei happy at right
                with dissolve

                mei "Hì. *cười rồi đi chỗ khác*"

                hide mei happy
                with dissolve
            else:
                mei "Sao rồi? Lại trượt hả? *cười nhẹ* Cố lên nha."
                scene_desc "Mei vỗ vai Vy, nụ cười hoàn hảo. Nhưng không giơ bài lên."

                hide mei mask_on
                with dissolve

            hide vy neutral
            with dissolve

            mei_inner "..."
            mei_inner "Sao mình lại làm vậy?"
            mei_inner "Sao mỗi lần thấy ai khác thất bại, mình lại... cảm thấy nhẹ nhõm?"
            mei_inner "Vì khi ai đó kém hơn mình... mình cảm thấy mình vẫn có giá trị."
            mei_inner "..."
            mei_inner "Mình là con người khủng khiếp."

        "Im lặng, giả vờ không thấy — mình cũng chẳng khá hơn đâu":
            $ facade += 0
            $ empathy += 2

            hide vy shocked
            with dissolve

            show mei thinking at center
            with dissolve

            mei_inner "..."
            mei_inner "4 điểm. Nó fail."
            if cheated_on_test:
                mei_inner "Còn mình... 10 điểm gian lận. Ai fail hơn ai nhỉ?"
            else:
                mei_inner "Còn mình... 7 điểm. Cũng không khá hơn bao nhiêu."
            mei_inner "Kệ. Không phải việc của mình."
            scene_desc "Mei quay mặt sang cửa sổ, giả vờ nhìn trời."

            hide mei thinking
            with dissolve

        "Nói gì đó tử tế — thật lòng":
            $ facade -= 5
            $ empathy += 7
            $ self_worth += 3
            $ vy_relationship += 10

            hide vy shocked
            show vy neutral at left
            with dissolve

            show mei neutral at right
            with dissolve

            scene_desc "Mei do dự một lúc. Rồi đứng dậy, đi qua bàn Vy."

            mei "Ê."

            hide vy neutral
            show vy shocked at left
            with dissolve

            vy "*ngước lên* Hả...?"

            if cheated_on_test:
                hide mei neutral
                show mei sad at right
                with dissolve

                mei "Đừng buồn quá. Bài này... khó thiệt."
                mei_inner "Mình biết vì mình cũng không làm được. Nhưng mình không nói câu đó."
            else:
                hide mei neutral
                show mei sad at right
                with dissolve

                mei "Bài này khó ha. Tui cũng... không tốt lắm."

                hide vy shocked
                show vy shocked at left
                with dissolve

                vy "Hả? Mày mà? Nhưng... mày luôn điểm cao mà..."
                mei "... Không phải lúc nào cũng vậy đâu."
                mei_inner "Lần đầu tiên... nói thật."
                mei_inner "Cảm giác... lạ lắm. Nhẹ. Nhưng cũng... sợ."

            hide vy shocked
            show vy neutral at left
            with dissolve

            vy "..."
            vy "Ờ... Cám ơn... Mai."
            scene_desc "Vy nhìn Mei với ánh mắt hơi ngạc nhiên — như vừa thấy mặt trăng giữa ban ngày."

            hide mei sad
            hide vy neutral
            with dissolve

    ## --------------------------------------------------------
    ## PART 7: SAU GIỜ HỌC — AFTER CLASS
    ## --------------------------------------------------------

    scene_desc "Chuông reo. Hết tiết."
    scene_desc "Học sinh ùa ra khỏi lớp như nước vỡ bờ."

    scene bg/school_hallway
    with fade

    scene_desc "Mei đi dọc hành lang. Xung quanh, bạn bè cười đùa, chia nhóm ra về."

    show mei mask_on at center
    with dissolve

    mei_inner "Một ngày nữa qua đi."
    mei_inner "Mask — On. Performance — acceptable. Damage — contained."

    ## CHOICE 5: End of day reflection
    menu:
        mei_inner "Một ngày dài thật dài..."

        "Đi một mình — cần thời gian để xả cái mask":
            $ facade -= 2

            hide mei mask_on
            show mei neutral at center
            with dissolve

            scene bg/street_evening
            with fade

            show mei neutral at center
            with dissolve

            scene_desc "Mei đi một mình ra cổng trường, tai nghe đã cắm sẵn."
            mei_inner "Playlist 'dành cho alien trầm cảm'. Track 47. Repeat."
            mei_inner "Đi bộ về nhà mất 1,247 bước. Mình đếm mỗi ngày."
            mei_inner "Kỳ lạ... Nhưng kệ. Không ai biết mà."
            scene_desc "Ánh nắng chiều vàng trải dài trên con đường. Mei đi bộ, bóng mình kéo dài phía sau."
            mei_inner "Bóng mình... Trông cô đơn vậy ta."

            hide mei neutral
            with dissolve

        "Đi cùng đám bạn — duy trì hình ảnh xã hội":
            $ facade += 3
            $ empathy += 1

            hide mei mask_on
            show mei happy at center
            with dissolve

            scene_desc "Mei hòa vào đám bạn cùng lớp, cười nói rôm rả."
            classmate "Mai ơi, cuối tuần đi chơi không? Tụi tao đi Nowzone!"
            mei "Ồ hay quá! Để tui xem lịch ha! *cười*"

            hide mei happy
            with dissolve

            mei_inner "Script số 27: 'Luôn tỏ ra hứng thú, hẹn xem lịch, rồi từ chối vào phút cuối.' Kinh điển."
            mei_inner "Mình không ghét bọn nó. Mình chỉ... mệt."
            mei_inner "Mệt vì phải diễn. Nhưng cũng mệt vì sợ bị bỏ rơi nếu không diễn."

        "Nán lại thêm — muốn ở trường thêm tí, vì về nhà cũng chẳng khá hơn":
            $ self_worth -= 2

            hide mei mask_on
            with dissolve

            scene bg/classroom
            with fade

            show mei sad at center
            with dissolve

            scene_desc "Mei ngồi lại lớp sau khi mọi người đã đi. Lớp vắng tanh."
            mei_inner "Nhà. Về nhà."
            mei_inner "Nghĩa là đối mặt với mẹ hỏi 'hôm nay điểm bao nhiêu?'"
            mei_inner "Nghĩa là ngồi trước bàn học 4 tiếng, giả vờ ôn bài trong khi thực ra đang cuộn meme trên acc clone."
            mei_inner "Nghĩa là nấu mì 10 giờ tối, thức tới 3 giờ sáng, rồi lại thức dậy lúc 5:30."
            mei_inner "... Loop vô tận."
            scene_desc "Mei nhìn ra cửa sổ. Nắng chiều hắt qua những chấn song, vẽ những vệt sáng dài trên sàn."
            mei_inner "Nắng đẹp thật. Nhưng đẹp kiểu buồn."

            hide mei sad
            show mei neutral at center
            with dissolve

            ## Spot Vy in the hallway
            show vy sleepy at left
            with dissolve

            scene_desc "Trong khoảng lặng đó, phía hành lang, Mei thoáng thấy một bóng người đang ngồi lại — Vy."
            mei_inner "... Nó cũng ở lại. Có vẻ nó ngủ gật thì phải."
            mei_inner "Heh. Bình thường quá nhể."
            scene_desc "Mei mỉm cười nhẹ — lần này là thật — rồi đứng dậy đi về."

            hide vy sleepy
            hide mei neutral
            with dissolve

    ## --------------------------------------------------------
    ## PART 8: VỀ NHÀ — GOING HOME
    ## --------------------------------------------------------

    scene black
    with fade

    scene bg/street_evening
    with fade

    scene_desc "Con đường về nhà. Nắng chiều nhuộm cam cả bầu trời."

    mei_inner "Mình tự hỏi..."
    mei_inner "Nếu một ngày mình bỏ hết mặt nạ..."
    mei_inner "Bỏ hết điểm 10, bỏ hết nụ cười giả, bỏ hết sự hoàn hảo..."
    mei_inner "Còn lại gì?"

    pause 1.0

    mei_inner "..."

    pause 0.5

    mei_inner "Mình sợ câu trả lời là: Không còn gì cả."

    ## --------------------------------------------------------
    ## PART 9: VỀ TỚI NHÀ — MẸ
    ## --------------------------------------------------------

    scene bg/mei_home
    with fade

    scene_desc "Mei mở cửa nhà. Mùi nước lau sàn. Mùi cơm chiều."

    show mei mask_on at right
    with dissolve

    mom "Về rồi hả con?"
    mei "Dạ."
    mom "Hôm nay kiểm tra gì không?"

    mei_inner "Đây rồi. Câu hỏi quen thuộc. Đúng 3 giây sau khi bước vào nhà."
    mei_inner "Không phải 'hôm nay con có vui không?' Không phải 'con có mệt không?'"
    mei_inner "Mà là 'kiểm tra gì không?' Vì đó mới là thứ quan trọng."

    ## CHOICE 6: Responding to Mom
    menu:
        mei_inner "Trả lời sao đây..."

        "Nói thật (nếu điểm thấp) / Khoe bình thường (nếu điểm cao)":
            if cheated_on_test:
                mei "Dạ, Toán. 10 điểm ạ."
                mom "Giỏi! Vậy là phải giữ vậy hoài nha con."
                mei_inner "\"Giữ vậy hoài.\" Không phải khen. Đó là mệnh lệnh."
                mei_inner "Không phiền bao giờ cho phép mình nghỉ ngơi."

                hide mei mask_on
                with dissolve
            else:
                hide mei mask_on
                show mei sad at right
                with dissolve

                mei "Dạ, Toán. 7 điểm ạ."
                mom "7? Sao ít vậy? Mấy đứa khác bao nhiêu?"
                mei_inner "Không hỏi mình có ổn không. Hỏi mình so với mấy đứa khác."
                mei "Con... bài khó lắm mẹ."
                mom "Khó gì mà khó, con không chịu ôn bài kỹ thôi. Lần sau phải cố hơn nữa nghen."
                mei "Dạ."
                mei_inner "Dạ. Dạ. Luôn luôn là dạ."
                $ self_worth -= 3
                $ facade += 2

                hide mei sad
                with dissolve

        "Nói dối — 10 điểm":
            $ facade += 5
            $ self_worth -= 3

            mei "Dạ, Toán. 10 điểm ạ."
            mom "Tốt. Giữ vậy nha."
            mei_inner "10 điểm. Hoàn hảo. Giả dối. Như mọi khi."
            mei_inner "Nhưng ít nhất... mẹ không càm ràm. Và mình... an toàn."

            hide mei mask_on
            with dissolve

            scene_desc "Mei đi vào phòng, khóa cửa lại."
            mei_inner "Safe. Pháo đài vẫn đứng vững."
            mei_inner "Mệt vãi."

        "Né câu hỏi — đổi chủ đề":
            hide mei mask_on
            show mei happy at right
            with dissolve

            mei "Dạ, bình thường mẹ ơi. À, mẹ nấu gì ngon vậy?"
            mom "Canh chua cá lóc. Đi rửa tay rồi ăn."

            hide mei happy
            with dissolve

            mei_inner "Crisis averted. Tạm thời."
            mei_inner "Nhưng nó sẽ quay lại. Nó luôn quay lại."

    ## --------------------------------------------------------
    ## PART 10: MỘT MÌNH TRONG PHÒNG — ALONE
    ## --------------------------------------------------------

    scene bg/mei_room_night
    with fade

    scene_desc "Đêm. Căn phòng nhỏ. Chỉ còn ánh đèn bàn và ánh màn hình laptop."

    mei_inner "Okay. Cuối cùng thì cũng đến phần mình thích nhất trong ngày."
    mei_inner "Phần mà mình được... gỡ mặt nạ ra."

    show mei neutral at center
    with dissolve

    scene_desc "Mei thả mình xuống ghế, buông tóc, cởi bỏ cái dáng vẻ chỉn chu. Vai xụ xuống. Mặt trở lại vẻ mệt mỏi thật."

    hide mei neutral
    show mei sad at center
    with dissolve

    mei_inner "AHHHH... Cuối cùng."
    mei_inner "Giờ thì... Hành tinh Maitopia, ta đã trở về."

    scene_desc "Mei mở laptop. 9 tab đã mở sẵn — mỗi tab là một clone account."

    mei_inner "Clone số 1 — acc backup chính. Clone số 2 — acc vent, chuyên đăng status mấy giờ sáng."
    mei_inner "Clone số 3 — meme. Clone số 4 — art. Clone số 5 — music."
    mei_inner "Đến clone số 9... acc mà không ai biết. Ngay cả mình đôi khi cũng quên mình có."

    mei_inner "Ở đây... Mình không phải Mai Trần, top 1 khối."
    mei_inner "Mình chỉ là... Mình."
    mei_inner "Một alien lạc trên Trái Đất."

    hide mei sad
    with dissolve

    ## Transition to Chapter 2
    scene black
    with fade

    pause 0.5

    mei_inner "Và đêm nay... đêm nay..."
    mei_inner "Đêm nay là của Alien."

    jump chapter1_end