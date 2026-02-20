## chapter2.rpy — Chương 2: Sau Lớp Vỏ (Behind the Shell)
## ============================================================
## Mai's evening at home: clone accounts, deep web, late night,
## the real "Alien Mai". An entirely NEW chapter not in original script.
## This explores Mai's psychological profile in depth.
## ============================================================

label chapter2_start:

    ## --------------------------------------------------------
    ## PART 1: CLONE WORLD — 9 TÀI KHOẢN, 9 MẢNH LINH HỒN
    ## --------------------------------------------------------

    ## [BG: bg mei_room_night — Night, desk lamp, laptop glow]
    scene_desc "11 giờ đêm. Ngôi nhà đã tắt đèn. Chỉ còn phòng Mei là sáng."

    mei_inner "Okay. Giờ hành chính trên Maitopia đã bắt đầu."
    mei_inner "Công dân duy nhất: Tui."
    mei_inner "Và 9 phiên bản khác của tui."

    scene_desc "Mei kéo ghế vào bàn, mở laptop. Trên màn hình — 9 tab browser, mỗi tab một tài khoản khác nhau."

    mei_inner "Người ta có việc gì phải lập 9 acc clone không?"
    mei_inner "... Người bình thường thì không."
    mei_inner "Nhưng mình không phải người bình thường. Mình là alien mà."
    mei_inner "Và mỗi acc là một miếng của mình mà thế giới thật không bao giờ được thấy."

    ## CLONE EXPLORATION — Player chooses which accounts to visit
    ## Each one reveals a different facet of Mai's personality

    label clone_menu:
        menu:
            mei_inner "Tối nay lướt cái nào..."

            "Clone #3 — Acc Meme (Khi buồn thì cười)" if not clone_meme:
                $ clone_meme = True
                $ explored_clones = True
                jump clone_meme_route

            "Clone #2 — Acc Vent (Khi cần la hét vào hư vô)" if not clone_vent:
                $ clone_vent = True
                $ explored_clones = True
                jump clone_vent_route

            "Clone #4 — Acc Art (Khi cần vẽ ra nỗi đau)" if not clone_art:
                $ clone_art = True
                $ explored_clones = True
                jump clone_art_route

            "Clone #5 — Acc Music (Playlist lúc 3 giờ sáng)" if not clone_music:
                $ clone_music = True
                $ explored_clones = True
                jump clone_music_route

            "Clone #9 — Acc Bí Mật (... cái mà chính mình cũng sợ)" if not clone_deep_web:
                $ clone_deep_web = True
                $ explored_clones = True
                jump clone_deepweb_route

            "Đủ rồi, đóng laptop" if explored_clones:
                jump clone_done

    ## ---- CLONE #3: MEME ACCOUNT ----
    label clone_meme_route:
        scene_desc "Tab 3: @alien_on_earth_03. Bio: 'chết cũng phải cười cho vui.'"

        mei_inner "Okay let's see..."
        scene_desc "Mei cuộn feed. Toàn meme trầm cảm Gen Z."

        mei_inner "\"POV: Bạn 3 giờ sáng, deadline 8 giờ, nhưng bạn đang coi video mèo.\""
        mei_inner "*snort* Literally me tối qua."

        mei_inner "\"khi ai hỏi 'mày ổn không?' và mày nói 'ổn' trong khi đang chết bên trong\""
        mei_inner "... Cái này hơi quá gần nhà rồi."

        scene_desc "Mei đăng một meme mới lên story: \"Hành tinh của tui chỉ có tui, nhưng wifi vẫn chậm.\""

        mei_inner "2 view. Cả 2 đều là bot."
        mei_inner "Hoàn hảo. Đúng số lượng khán giả mà mình cần."

        ## CHOICE: React?
        menu:
            "Cười, cảm thấy nhẹ nhõm nhờ humor":
                $ self_worth += 2
                mei_inner "Humor đen là cơ chế sinh tồn. Change my mind."
                mei_inner "Ít nhất ở đây... Mình có thể buồn mà không cần permission."

            "Cảm thấy trống rỗng — meme cũng không cứu nổi nữa":
                $ self_worth -= 2
                mei_inner "Ngày xưa meme còn khiến mình cười."
                mei_inner "Giờ mình chỉ cuộn. Và cuộn. Và cuộn."
                mei_inner "Như thể đang tìm kiếm một cái gì đó... mà bản thân cũng không biết nó là gì."

        jump clone_menu

    ## ---- CLONE #2: VENT ACCOUNT ----
    label clone_vent_route:
        scene_desc "Tab 2: @______void______. Bio: trống. Followers: 0. Following: 0."

        mei_inner "Acc vent. Nơi mà mình la hét vào hư vô."
        mei_inner "Không ai follow. Không ai đọc. Đó mới là ý nghĩa của nó."

        scene_desc "Mei nhìn lại những status cũ mình đã đăng:"
        scene_desc "'3:47am — mệt quá rồi. Mệt cả việc mệt luôn.'"
        scene_desc "'Hôm nay mẹ hỏi bao nhiêu điểm. Mình nói 10. Mẹ nói giữ vậy. Mình muốn biến mất.'"
        scene_desc "'Có khi nào... người ta mệt tới mức không còn buồn nổi nữa không?'"

        mei_inner "..."
        mei_inner "Đọc lại... thấy mình pathetic ghê."
        mei_inner "Nhưng cũng thấy... mình thật."

        ## CHOICE: Write something new?
        menu:
            "Đăng status mới — xả hết ra":
                $ facade -= 5
                $ self_worth += 3
                mei_inner "Okay. Let it out."
                scene_desc "Mei gõ:"
                scene_desc "'2:03am — tại sao mọi người muốn mình hoàn hảo? tại sao mình cũng muốn mình hoàn hảo? ai bắt đầu cái vòng lặp khốn nạn này?'"
                mei_inner "Không ai đọc. Không ai quan tâm."
                mei_inner "Nhưng ít nhất... mình đã nói ra."
                mei_inner "Và đôi khi, nói ra cho hư vô nghe... cũng đủ rồi."

            "Đọc lại status cũ, nhưng không đăng gì mới":
                $ facade += 2
                mei_inner "Không. Không nên viết thêm."
                mei_inner "Nếu lỡ ai đó tìm thấy acc này... Nếu lỡ bọn họ biết..."
                mei_inner "Biết rằng Mai Trần, top 1 khối, thức 3 giờ sáng để khóc trên một acc không follower..."
                mei_inner "Thà chết còn hơn."

            "Xóa hết — sợ bị phát hiện":
                $ facade += 5
                $ self_worth -= 3
                mei_inner "Không. Quá nguy hiểm."
                scene_desc "Mei select all. Delete. Delete. Delete."
                mei_inner "Mỗi status biến mất... như nó chưa từng tồn tại."
                mei_inner "Giống như nỗi buồn của mình: đằng nào cũng không ai thấy, thì xóa đi cho gọn."
                mei_inner "..."
                mei_inner "Xong. Sạch sẽ. Hoàn hảo."
                mei_inner "Hoàn hảo... như mọi khi."

        jump clone_menu

    ## ---- CLONE #4: ART ACCOUNT ----
    label clone_art_route:
        scene_desc "Tab 4: @maitopia_art. Bio: 'i draw when i can\\'t speak.'"

        mei_inner "Acc art. Nơi mình vẽ những thứ mà miệng không nói được."

        scene_desc "Mei cuộn qua gallery — những bức vẽ digital đơn giản nhưng đầy cảm xúc."
        scene_desc "Một cô gái nhỏ đứng trước gương. Bóng phản chiếu không giống cô ấy."
        scene_desc "Một hành tinh cô đơn giữa vũ trụ, xung quanh toàn sao nhưng không đến gần được cái nào."
        scene_desc "Một đôi tay đang giữ một chiếc mặt nạ cười, phía sau là khuôn mặt mờ khuất trong bóng tối."

        mei_inner "Mỗi bức vẽ là mỗi lần mình muốn la lên nhưng không dám."
        mei_inner "Nên mình vẽ. Vẽ cho cái phần Alien bên trong mình có chỗ để thở."

        ## CHOICE: Draw something?
        menu:
            "Vẽ thêm gì đó — hôm nay có nhiều điều muốn nói":
                $ self_worth += 3
                $ empathy += 2
                mei_inner "Hôm nay... Mình muốn vẽ..."
                scene_desc "Tay Mei di chuyển trên tablet. Từng nét từng nét."
                scene_desc "Hình ảnh hiện dần: Hai bóng người đứng cạnh nhau — một người sáng rực, một người mờ ảo."
                scene_desc "Người sáng rực đang cười. Người mờ ảo đang nhìn."
                mei_inner "... Ai là ai nhỉ."
                mei_inner "Mình... và Vy?"
                mei_inner "Hay mình... và bản thân mình?"
                mei_inner "Kệ. Tác phẩm không cần giải thích. Đó mới là art."

            "Chỉ xem lại — không có hứng vẽ":
                mei_inner "Hôm nay tay mình run quá. Không vẽ nổi."
                mei_inner "Có khi nào... đến nghệ thuật cũng bỏ mình."

        jump clone_menu

    ## ---- CLONE #5: MUSIC ACCOUNT ----
    label clone_music_route:
        scene_desc "Tab 5: Spotify — playlist 'dành cho alien trầm cảm (vol. 47)'"

        mei_inner "Volume 47. Mỗi đêm mình thêm 2-3 bài."
        mei_inner "Giờ playlist dài hơn tuổi đời mình."

        scene_desc "Mei bấm play. Nhạc trôi trong căn phòng tối — những giai điệu nhè nhẹ, buồn nhưng đẹp."

        mei_inner "Sleeping At Last — Saturn."
        mei_inner "'You taught me the courage of stars before you left...'"
        mei_inner "... Bài này mình nghe từ năm lớp 10. Khi lần đầu tiên mình nhận ra..."
        mei_inner "Rằng mình cô đơn. Không phải vì không có ai. Mà vì không ai hiểu."

        ## CHOICE: What does the music make Mei feel?
        menu:
            "Nhắm mắt, để nhạc cuốn đi — đây là liệu pháp":
                $ self_worth += 3
                scene_desc "Mei nhắm mắt. Thả đầu ra sau ghế."
                mei_inner "Nhạc hay có sức mạnh không giải thích được."
                mei_inner "Nó không sửa được gì. Nhưng nó khiến mình cảm thấy..."
                mei_inner "Rằng nỗi buồn của mình cũng đáng để tồn tại."
                mei_inner "Rằng mình không cần phải 'fix' bản thân. Chỉ cần... cảm nhận."
                scene_desc "Một giọt nước mắt lăn dài. Mei không lau. Lần đầu tiên hôm nay."
                mei_inner "Okay. Đủ rồi. Bài tiếp."

            "Bỏ tai nghe ra — đêm nay không chịu nổi":
                $ self_worth -= 1
                mei_inner "Không. Đêm nay không chịu nổi."
                mei_inner "Nhạc buồn lúc này giống như đổ thêm muối vào."
                mei_inner "Mà mình đã đủ mặn rồi."
                scene_desc "Mei tắt nhạc. Phòng im lặng đến đáng sợ."

        jump clone_menu

    ## ---- CLONE #9: DEEP WEB / SECRET ACCOUNT ----
    label clone_deepweb_route:
        scene_desc "Tab 9: Chế độ ẩn danh. Trang chủ — Reddit, các subreddit về true crime, deep web stories."

        mei_inner "Clone số 9. Acc mà chính mình đôi khi cũng quên."
        mei_inner "Hay đúng hơn... đôi khi mình MUỐN quên."

        scene_desc "Mei staring at the screen. Tay lướt qua những thread về Creepypasta, vụ án mạng có thật, những thí nghiệm tâm lý đáng sợ."

        mei_inner "Mọi người nghĩ đây là bệnh hoạn. Nghĩ mình... weird."
        mei_inner "Nhưng bọn họ không hiểu."
        mei_inner "Khi mình đọc về những thứ kinh dị thật sự... Deadline 8 giờ sáng bỗng trở nên... nhỏ bé."
        mei_inner "Áp lực điểm số? Haha. Có người ngoài kia mất mạng vì một cuộc gọi nhầm."
        mei_inner "Đó. Perspective."

        ## CHOICE: How deep to go?
        menu:
            "Đọc thêm — mình cần perspective lớn hơn":
                $ facade -= 2
                $ self_worth += 1
                mei_inner "Russian Sleep Experiment. Lại cái này."
                mei_inner "Lần thứ 4 đọc rồi. Nhưng mỗi lần đọc lại thấy khác."
                mei_inner "Lần 1: Sợ. Lần 2: Tò mò. Lần 3: Phân tích. Lần 4..."
                mei_inner "Thấy mình... cũng giống mấy subject đó."
                mei_inner "Bị nhốt. Không được ngủ. Bị quan sát."
                mei_inner "Khác là mình tự nhốt mình thôi."

            "Đóng tab — nửa đêm rồi, đừng self-scare nữa":
                $ self_worth += 2
                mei_inner "Okay okay, đủ rồi. 1 giờ sáng rồi."
                mei_inner "Mình đang ngồi trong bóng tối, đọc về serial killers."
                mei_inner "Nếu ai nhìn vào cửa sổ lúc này chắc tưởng mình là final boss."
                mei_inner "*snort* ... Ít nhất vẫn còn biết đùa."

        ## SECRET ENDING FLAG CHECK
        if clone_meme and clone_vent and clone_art and clone_music and clone_deep_web:
            $ secret_ending_unlocked = True
            mei_inner "..."
            mei_inner "Mình vừa lướt qua... tất cả 5 clone trong một đêm."
            mei_inner "9 mảnh linh hồn. 9 phiên bản khác nhau của Mai."
            mei_inner "Liệu có phiên bản nào... là thật?"
            mei_inner "Hay tất cả đều là thật... và đó mới là vấn đề?"

        jump clone_menu

    ## ---- DONE WITH CLONES ----
    label clone_done:

        scene_desc "Mei đóng laptop. Màn hình tắt. Phòng chìm trong bóng tối."

        ## --------------------------------------------------------
        ## PART 2: NẤU MÌ LÚC NỬA ĐÊM — MIDNIGHT COOKING
        ## --------------------------------------------------------

        mei_inner "Đói."
        mei_inner "1 giờ sáng. Bụng kêu. Não cần glucose."
        mei_inner "Giải pháp: Mì."

        scene_desc "Mei rón rén mở cửa phòng. Hành lang tối om. Tiếng ngáy ngủ vọng từ phòng bố mẹ."

        mei_inner "Mission: Nấu mì không gây tiếng động. Difficulty: Expert."

        ## [BG: bg kitchen_dark — Kitchen, only stove light]
        scene_desc "Bếp. Ánh đèn hood bếp là nguồn sáng duy nhất."

        scene_desc "Mei mở tủ lạnh — ánh sáng tràn ra như cổng dịch chuyển về một vũ trụ khác."

        mei_inner "Okay. Mì + trứng + ... Hmm..."
        mei_inner "Bạch tuộc đông lạnh? Nấu chung với mì được không?"
        mei_inner "Phô mai? Sốt tương? Kimchi?"
        mei_inner "..."
        mei_inner "All of the above."

        scene_desc "Mei bắt đầu nấu — thả tất cả vào nồi. Mì, trứng, bạch tuộc, phô mai, kim chi."
        scene_desc "Hỗn hợp trông như một thí nghiệm hóa học thất bại."

        mei_inner "Đây không phải nấu ăn. Đây là art."
        mei_inner "Abstract Expressionism phiên bản bếp núc."
        mei_inner "Pollock cũng nấu mì kiểu này nếu ổng sống tới thời Gen Z."

        ## CHOICE: Eating feelings
        menu:
            mei_inner "Và... ăn."

            "Ăn chậm, ngồi suy nghĩ — thời gian này là quý giá":
                $ self_worth += 3
                scene_desc "Mei ngồi trên sàn bếp, lưng dựa tủ, tô mì bốc khói trên đùi."
                mei_inner "1 giờ 47 phút sáng."
                mei_inner "Cả thế giới đang ngủ. Chỉ có mình thức."
                mei_inner "Và cảm giác này... Lạ lắm."
                mei_inner "Sáng mai mình sẽ lại đeo mặt nạ. Lại cười. Lại hoàn hảo."
                mei_inner "Nhưng lúc này, ngay lúc này..."
                mei_inner "Mình chỉ là một đứa con gái ngồi ăn mì lúc 2 giờ sáng."
                mei_inner "Và... Đó là okay."
                mei_inner "Đó là đủ."
                scene_desc "Tiếng xì xụp nhẹ. Hơi nóng từ tô mì sưởi ấm khuôn mặt."
                mei_inner "... Ngon thật."

            "Ăn nhanh rồi đi ngủ — mai còn phải chiến tiếp":
                $ facade += 2
                mei_inner "Fast. Efficient. Như mọi thứ trong cuộc đời mình."
                scene_desc "Mei ăn xong trong 5 phút. Rửa nồi. Lau bếp. Không để lại dấu vết."
                mei_inner "Clean. Perfect. Không ai biết mình thức."
                mei_inner "Không ai biết... bất cứ điều gì."

            "Ăn xong, ngồi thêm — không muốn về phòng, không muốn đi ngủ":
                $ self_worth -= 1
                $ facade -= 3
                scene_desc "Mei ăn xong nhưng vẫn ngồi yên. Tô mì đã trống. Nhưng bên trong..."
                mei_inner "Sao mình không muốn ngủ?"
                mei_inner "Vì ngủ = ngày mai. Ngày mai = mask. Mask = mệt."
                mei_inner "Nên mình cứ ngồi đây. Kéo dài đêm. Kéo dài khoảng tự do nhỏ bé này."
                mei_inner "Như thể nếu mình không đi ngủ... Ngày mai sẽ không đến."
                scene_desc "2 giờ 30. 2 giờ 45. 3 giờ..."
                mei_inner "... Maitopia mãi mãi."

    ## --------------------------------------------------------
    ## PART 3: TRƯỚC KHI NGỦ — BEFORE SLEEP
    ## --------------------------------------------------------

    ## [BG: bg mei_room_night — Back in her room, deep night]
    scene_desc "Phòng ngủ. Mei nằm trên giường, điện thoại chiếu sáng trần nhà."

    mei_inner "Cuộn Facebook một lần cuối."
    mei_inner "Acc chính. Thế giới thật."

    scene_desc "Mei nhìn story của người khác: bạn bè đi chơi nhóm, chụp ảnh cùng nhau, cười đùa vô tư."

    mei_inner "Mọi người có vẻ... vui thật."
    mei_inner "Họ có phải diễn không nhỉ? Hay thật sự... Cuộc sống của họ dễ dàng hơn?"

    ## CHOICE: Last thought before sleep
    menu:
        mei_inner "Và... Suy nghĩ cuối cùng trước khi mắt nhắm lại..."

        "\"Ngày mai sẽ khác.\" — Một chút hy vọng":
            $ self_worth += 2
            $ empathy += 1
            mei_inner "Biết đâu... Ngày mai sẽ khác."
            mei_inner "Mình không biết khác kiểu gì. Nhưng..."
            mei_inner "Cứ hy vọng đã."
            scene_desc "Mei mỉm cười nhẹ trong bóng tối. Mắt từ từ khép lại."
            mei_inner "Good night, Maitopia."

        "\"Ngày mai cũng vậy thôi.\" — Quen rồi":
            $ facade += 2
            mei_inner "Ngày mai cũng vậy."
            mei_inner "5:30 dậy. Mask on. Perform. Về nhà. Clone. Mì. Ngủ."
            mei_inner "Loop."
            mei_inner "Nhưng mà loop cũng được. Ít nhất loop thì mình biết kịch bản."
            mei_inner "Sợ nhất là khi kịch bản thay đổi."
            scene_desc "Mei nhắm mắt. Trằn trọc thêm 20 phút rồi thiếp đi."

        "\"Nếu mình biến mất... ai sẽ nhận ra?\" — Suy nghĩ tối":
            $ self_worth -= 5
            $ empathy -= 2
            mei_inner "Nếu ngày mai mình không tới trường..."
            mei_inner "Ai sẽ hỏi? Bao lâu thì có người notice?"
            mei_inner "1 ngày? 2 ngày? 1 tuần?"
            mei_inner "... Không. Dừng lại."
            mei_inner "Đây không phải suy nghĩ lành mạnh."
            mei_inner "Nhưng mà... Nó cứ đến. Mỗi đêm."
            mei_inner "Như một vị khách không mời mà cứ gõ cửa."
            scene_desc "Mei ôm gối, co người lại. Mắt mở thao láo trong bóng tối."
            mei_inner "3 giờ 14 sáng. Và mình... vẫn thức."
            mei_inner "..."
            mei_inner "Alien không cần ngủ. Alien ổn mà. Alien... Ổn..."
            scene_desc "Mắt cuối cùng cũng nhắm lại. Giấc ngủ đến — nặng nề, không bình yên."

    ## --------------------------------------------------------
    ## TRANSITION TO NEXT DAY
    ## --------------------------------------------------------

    scene black with fade
    pause 1.0

    scene_desc "..."
    scene_desc "5:30 sáng."
    scene_desc "Chuông báo thức reo."
    scene_desc "Và loop bắt đầu lại."

    pause 0.5

    mei_inner "..."
    mei_inner "Nhưng hôm nay... Có gì đó sẽ khác."
    mei_inner "Mình chỉ chưa biết là gì thôi."

    jump chapter2_end
