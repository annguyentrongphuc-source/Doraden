## chapter3.rpy — Chương 3: Cỗ Máy Ảnh (The Camera)
## ============================================================
## Original Script Scenes 2-3 from Mai's POV.
## Den-Dora appears to Vy (Mai observes from afar).
## The test where Vy suddenly scores 10 and Mai's real scores exposed.
## This is the CRISIS chapter — the facade starts cracking.
## ============================================================

label chapter3_start:

    ## --------------------------------------------------------
    ## PART 1: CÁI GÌ ĐÓ LẠ ĐANG XẢY RA — SOMETHING'S OFF
    ## --------------------------------------------------------

    ## [BG: bg classroom — Morning classroom]
    scene_desc "Hôm sau. Lớp học. Mọi thứ như cũ."
    scene_desc "Hay đúng hơn... gần như cũ."

    mei_inner "Vy hôm nay lạ lắm."

    scene_desc "Mei quan sát Vy từ chỗ ngồi. Vy đang nhìn chằm chằm vào một thứ gì đó trên bàn — giống... máy ảnh?"

    mei_inner "Nó ngồi nhìn cái máy ảnh đã hơn 5 phút rồi."
    mei_inner "Bình thường nó ngủ gật lúc này mới đúng."
    mei_inner "Và... máy ảnh từ đâu ra? Vy có phải dạng mua máy ảnh đâu."

    ## CHOICE: Observe or ignore?
    menu:
        mei_inner "Hmm..."

        "Để ý thêm — có gì đó không ổn":
            $ empathy += 2
            mei_inner "Mình không biết tại sao... Nhưng cảm giác có gì đó sắp xảy ra."
            mei_inner "Giống như khi trời sắp mưa — không thấy mây, nhưng da thấy ẩm."
            scene_desc "Mei khẽ nghiêng đầu, tiếp tục quan sát Vy."
            mei_inner "Và khuôn mặt Vy... Nó không phải mặt ngái ngủ thường ngày."
            mei_inner "Nó đang... trăn trở. Nghĩ ngợi."
            mei_inner "Vy mà biết nghĩ ngợi? Lạ thật."

        "Kệ đi — mắc gì lo chuyện người khác":
            $ facade += 2
            mei_inner "Whatever. Nó muốn ngồi nhìn cái gì thì nhìn."
            mei_inner "Mình còn phải ôn bài. Hôm nay kiểm tra Lý."
            mei_inner "Mai Trần không phân tâm vì chuyện linh tinh."

    ## --------------------------------------------------------
    ## PART 2: NGÀY HÔM TRƯỚC — FLASHBACK VY GẶP DEN-DORA (MAI's POV)
    ## --------------------------------------------------------

    scene black with fade
    scene_desc "Tua lại hôm qua. Cuối buổi học."

    ## [BG: bg school_hallway_evening — Empty hallway, sunset]
    scene_desc "Mei đang đi về — đi muộn vì ở lại chép bài cho bạn (dĩ nhiên, vì đó là việc 'Mai hoàn hảo' phải làm)."

    mei_inner "Hành lang vắng tanh. Ai cũng về hết rồi."
    mei_inner "Tốt. Mình thích trường lúc này. Yên. Tĩnh. Không ai nhìn."

    scene_desc "Bỗng — một tiếng nổ nhẹ từ phía lớp học."

    mei_inner "?!"
    mei_inner "Tiếng gì vậy? Từ phòng... Lớp mình?"

    ## CHOICE: Investigate or leave?
    menu:
        mei_inner "..."

        "Đi xem — tò mò mà":
            $ empathy += 3
            scene_desc "Mei rón rén quay lại. Cánh cửa lớp hé mở."
            scene_desc "Bên trong — Vy đang đứng, mặt ngơ ngác. Và trước mặt Vy... Một thứ gì đó nhỏ xíu, tròn tròn, vừa chui ra từ hộc bàn giáo viên."
            mei_inner "... What the — CÁI GÌ VẬY?"
            mei_inner "Mình nhìn thấy... Một sinh vật. Giống... mèo? Robot? Toy?"
            mei_inner "Nó nói chuyện với Vy. Vy đang la hét."
            mei_inner "Và rồi... Nó bày ra mấy thứ đồ trên bàn."
            scene_desc "Mei đứng ngoài cửa, mắt mở to. Nhìn qua khe cửa."
            mei_inner "Đồng hồ. Đèn pin. Sandwich. Và... Máy ảnh."
            mei_inner "..."
            mei_inner "Okay. Hoặc mình đang mơ. Hoặc mình cần đi khám."
            mei_inner "Hoặc... Cái con mèo máy đó là thật."

            ## Mei watches Vy test the gadgets
            scene_desc "Mei quan sát qua khe cửa. Vy bấm đồng hồ — không có gì xảy ra. Vy thử đèn pin — cũng không."
            scene_desc "Con mèo máy đang ăn sandwich."
            mei_inner "... Nó ăn bánh mì. Trong lúc Vy đang test đồ."
            mei_inner "Mình phải thừa nhận... Tình huống này absurd đến mức... Buồn cười."
            mei_inner "... Đợi. Mình vừa thấy cái gì vui mà không cần fake cười?"
            mei_inner "Lạ thật."

            scene_desc "Vy đánh con mèo máy một trận. Con mèo la oai oái. Rồi nó đưa Vy cái máy ảnh — 'Máy Ảnh Sự Thật'."
            mei_inner "'Máy Ảnh Sự Thật'?! Tên gì mà hãm vậy..."
            mei_inner "Nhưng mà... Sự thật?"
            mei_inner "..."
            mei_inner "Mình có rất nhiều thứ mình không muốn ai biết 'sự thật'."

            ## Vy notices someone
            scene_desc "Vy bỗng quay lại phía cửa. Mei giật mình."
            mei_inner "CHẾT! Nó nhìn thấy mình!"
            scene_desc "Mei vội lùi lại, hood lên, đi nhanh xuống hành lang."
            mei_inner "Nhanh nhanh nhanh—"
            mei_inner "... Nó có thấy mặt mình không?"
            mei_inner "... Chắc không. Hy vọng không."

        "Đi luôn — không phải việc mình":
            $ facade += 3
            mei_inner "Kệ. Chắc mấy đứa nghịch phá gì đó."
            mei_inner "Mai Trần không liên quan tới drama."
            scene_desc "Mei đi thẳng ra cổng, không ngoái lại."
            mei_inner "... Nhưng lạ thật. Tiếng nổ đó..."
            mei_inner "Kệ. Không phải việc mình."

    ## --------------------------------------------------------
    ## PART 3: BÀI KIỂM TRA THỨ HAI — THE SECOND TEST
    ## --------------------------------------------------------

    scene black with fade
    ## [BG: bg classroom — Classroom, tense]
    scene_desc "Quay lại hiện tại. Giáo viên bước vào."

    teacher "Mấy em dời bàn ra."

    mei_inner "... WHAT?!"
    mei_inner "KIỂM TRA?! HÔM NAY?!"

    scene_desc "Mei giật bắn. Mắt mở to."

    mei_inner "Không. Không không không."
    mei_inner "Mình... quên ôn."
    mei_inner "Tối qua mình lướt clone. Nấu mì. Nghĩ lung tung."
    mei_inner "Mình QUÊN ÔN BÀI."
    mei_inner "..."
    mei_inner "Lần đầu tiên trong đời."
    mei_inner "MAI TRẦN QUÊN ÔN BÀI."

    scene_desc "Tim Mei đập loạn. Tay run. Vai gồng cứng."

    mei_inner "Bình tĩnh. BÌNH TĨNH, Mai."
    mei_inner "Mày vẫn nhớ mấy cái cũ. Kiến thức nền. Logic. Pattern."
    mei_inner "Just... breathe."

    teacher "Bắt đầu."

    scene_desc "Đề kiểm tra úp xuống bàn. Mei lật lên."

    mei_inner "..."
    mei_inner "Câu 1... Okay. Biết. Có thể làm."
    mei_inner "Câu 2... Hmm. Mờ mờ. Hình như..."
    mei_inner "Câu 3... Câu 4... Câu 5..."
    mei_inner "..."
    mei_inner "Không. Mình không biết câu 4 và 5."
    mei_inner "Tuyệt đối không biết."

    scene_desc "Mei cắn bút. Mồ hôi lấm tấm trên trán."

    ## CHOICE: How to handle this test
    menu:
        mei_inner "Sao đây..."

        "Liếc bài — mặt nạ quan trọng hơn lương tâm":
            $ facade += 5
            $ self_worth -= 5
            $ cheated_on_test = True
            mei_inner "Không được phép điểm thấp. Không. Được. Phép."
            mei_inner "Nếu mình điểm thấp... Mọi người sẽ biết. Mẹ sẽ biết."
            mei_inner "Cái pháo đài mình xây cả đời sẽ sụp."
            scene_desc "Mei liếc sang — vừa đủ nhanh, vừa đủ kín. Bạn bên cạnh đang viết câu 4."
            mei_inner "4... B... Okay."
            mei_inner "... Mình kinh tởm bản thân quá."

        "Làm những gì biết — chấp nhận thực tế":
            $ facade -= 8
            $ self_worth += 5
            mei_inner "..."
            mei_inner "Mình chỉ biết 3 câu."
            mei_inner "Thì làm 3 câu. 2 câu còn lại... Viết cái gì đó. Bất kỳ cái gì."
            mei_inner "Lần đầu tiên... Mình cho phép mình thất bại."
            mei_inner "Cảm giác... Giống như rơi từ lầu 10 mà không biết có lưới hay không."
            scene_desc "Mei gục đầu xuống, viết. Chậm. Thành thật."
            mei_inner "Viết xong. 3/5 câu."
            mei_inner "Tệ. Nhưng thật."

        "Liếc sách dưới gầm bàn — last resort":
            $ facade += 3
            $ self_worth -= 3
            $ cheated_on_test = True
            mei_inner "Sách. Sách nằm trong cặp. Cặp ngay dưới gầm bàn."
            mei_inner "Mình chỉ cần... đạp nhẹ cái cặp, kéo ra tí..."
            scene_desc "Mei khẽ đạp cặp, cúi xuống giả vờ nhặt bút. Mắt liếc nhanh vào trang sách."
            mei_inner "Câu 4... Công thức... Okay. Got it."
            mei_inner "..."
            mei_inner "Vy liếc mình."
            mei_inner "... Nó thấy không?"
            mei_inner "Bình tĩnh. Mặt bình thản. Mày là Mai Trần. Không ai nghi ngờ Mai Trần."

    ## --------------------------------------------------------
    ## PART 4: GV ĐI RA NGOÀI — THE TEACHER LEAVES
    ## --------------------------------------------------------

    scene_desc "Chuông điện thoại giáo viên reo. Giáo viên nhíu mày, bước ra ngoài."

    mei_inner "Giáo viên đi rồi."

    scene_desc "Cả lớp xôn xao nhỏ. Vài đứa liếc bài nhau."

    ## Mei observes Vy pulling out the camera
    mei_inner "Khoan..."
    mei_inner "Vy vừa rút cái gì ra từ cặp?"

    scene_desc "Mei nhìn sang. Vy đang cầm cái máy ảnh — cái máy ảnh lạ hôm qua."

    mei_inner "Cái máy ảnh! Cái mà con mèo máy đưa cho nó!"
    mei_inner "Nó đang... Chĩa vào đề bài?"

    scene_desc "Click. Ánh flash nhẹ."

    mei_inner "..."
    mei_inner "Và rồi... Vy nhìn vào màn hình máy ảnh."
    mei_inner "Mặt nó..."

    scene_desc "Vy đang nhìn chằm chằm vào máy ảnh, miệng há hốc."

    vy "*thầm* Không thể nào..."

    mei_inner "Nó vừa thấy cái gì vậy?"
    mei_inner "Mà sao mặt nó... kinh ngạc tới vậy?"

    ## --------------------------------------------------------
    ## PART 5: KẾT QUẢ — THE REVEAL (from Mai's POV)
    ## --------------------------------------------------------

    scene_desc "15 phút sau. Bài kiểm tra được thu."
    scene_desc "..."
    scene_desc "Và khi bài được trả..."

    scene_desc "Vy nhìn bài kiểm tra của mình. 10 điểm."

    mei_inner "..."
    mei_inner "10 ĐIỂM?!"
    mei_inner "VY?! 10 ĐIỂM?!"

    scene_desc "Cả lớp nhìn Vy, xì xào."

    classmate "Vy 10 điểm hả?? Trời ơi!"
    classmate "Vy mà 10? Impossible!"

    mei_inner "Không... Không thể nào."
    mei_inner "Vy thấp điểm mãi. Vy 4 điểm hôm trước."
    mei_inner "Sao hôm nay bỗng dưng... 10?"

    scene_desc "Và rồi... Vy nhìn sang Mei."

    mei_inner "Nó nhìn mình. Sao nó nhìn mình?"

    scene_desc "Ánh mắt Vy không phải dạng khiêu khích. Cũng không phải đắc thắng."
    scene_desc "Mà là... Thương xót?"

    mei_inner "... Cái nhìn đó. Mình biết cái nhìn đó."
    mei_inner "Đó là cái nhìn khi ai đó... Biết bí mật của mình."

    ## Mei's test score
    if cheated_on_test:
        scene_desc "Mei nhìn xuống bài mình. 8 điểm. Gian lận mà cũng chỉ 8."
        mei_inner "8. Liếc bài mà cũng chỉ 8."
        mei_inner "Bình thường mình sẽ nuốt nỗi thất vọng vào trong."
        mei_inner "Nhưng hôm nay... Có gì đó khác."
    else:
        scene_desc "Mei nhìn xuống bài mình. 5 điểm."
        mei_inner "5."
        mei_inner "Năm. Điểm."
        mei_inner "..."
        mei_inner "Mai Trần. 5 điểm."
        mei_inner "Thế giới đang sụp đổ."

    ## The MOMENT — Vy sees Mai's real scores
    scene_desc "Vy đứng dậy, đi ngang qua bàn Mei. Mắt liếc xuống bài kiểm tra của Mei — vô tình, hay cố ý?"

    mei_inner "KHÔNG!"

    scene_desc "Mei vội lật úp bài. Nhưng quá muộn."

    mei_inner "Nó thấy rồi."
    mei_inner "NÓ THẤY ĐIỂM MÌNH RỒI."

    scene_desc "Vy nhìn Mei. Mei nhìn Vy. Một khoảnh khắc dài vô tận."

    mei_inner "Nó biết. Nó biết mình không phải 10 điểm."
    mei_inner "Nó biết... Mình cũng chỉ là..."
    mei_inner "Bình thường."

    ## CHOICE: Mei's reaction to being exposed
    menu:
        mei_inner "..."

        "Giả vờ không có chuyện gì — mask ON max level":
            $ facade += 10
            $ self_worth -= 5
            scene_desc "Mei ép nụ cười lên môi."
            mei "Hôm nay khó quá ha! Ai cũng điểm thấp hết á."
            mei_inner "Giọng mình run. Có nghe thấy không? Có ai nhận ra không?"
            scene_desc "Mei cất bài kiểm tra vào cặp, tay hơi run."
            mei_inner "Giấu. Giấu tất cả. Như mọi khi."
            mei_inner "Không ai được biết. Không ai được thấy."
            mei_inner "Nhất là... Vy."

        "Gục mặt xuống bàn — không che nổi nữa":
            $ facade -= 10
            $ self_worth -= 3
            $ empathy += 3
            scene_desc "Mei gục mặt xuống bàn. Đầu úp trên hai cánh tay."
            mei_inner "Mình không khóc. Mai Trần KHÔNG khóc."
            mei_inner "... Nhưng mắt cay quá."
            mei_inner "Cay vì muốn khóc, hay cay vì mặt nạ đang bong ra từng mảnh?"
            scene_desc "Vy nhìn Mei gục xuống. Ánh mắt Vy phức tạp — ngạc nhiên, rồi... hiểu."
            mei_inner "Nó đang nhìn mình."
            mei_inner "Lần đầu tiên... Có ai nhìn thấy mình... Thật."
            mei_inner "Và mình ghét cảm giác này."
            mei_inner "Nhưng cũng... Nhẹ."

        "Bỏ ra ngoài — cần không gian":
            $ facade -= 5
            $ empathy -= 2
            scene_desc "Mei đứng dậy đột ngột. Ghế kéo kĩn kịt."
            mei "Xin phép đi toilet ạ."
            scene_desc "Mei đi nhanh ra cửa. Không nhìn ai."
            mei_inner "Ra. Ra khỏi đây. NGAY BÂY GIỜ."
            ## [BG: bg bathroom — School bathroom, mirror]
            scene_desc "Toilet cũ. Gương. Nước rỉ từ vòi."
            scene_desc "Mei nhìn vào gương. Khuôn mặt phản chiếu — đôi mắt đỏ, môi mím chặt."
            mei_inner "Mặt nạ mình đâu rồi? Sao mình không tìm thấy nó?"
            mei_inner "Cả đời mình xây. Mười mấy năm diễn."
            mei_inner "Sụp. Chỉ vì một con bé bình thường nhìn thấy điểm số."
            scene_desc "Mei vặn vòi nước, vốc nước lạnh lên mặt. Lạnh buốt."
            mei_inner "Tỉnh lại đi, Mai."
            mei_inner "Mày vẫn còn nguyên. Mày vẫn đứng đây."
            mei_inner "Một bài kiểm tra thấp không giết chết ai."
            mei_inner "... Nhưng sao mình cảm giác như đang chết nhỉ."

    ## --------------------------------------------------------
    ## PART 6: SAU GIỜ HỌC — AFTERMATH
    ## --------------------------------------------------------

    scene black with fade
    ## [BG: bg school_hallway — Hallway, end of day]
    scene_desc "Hết buổi học. Hành lang. Ánh nắng chiều hắt qua cửa sổ."

    mei_inner "Mình đi qua ngày hôm nay... Bằng cách nào?"
    mei_inner "Autopilot. Zombi mode. Cười đúng chỗ. Gật đầu đúng lúc."
    mei_inner "Nhưng bên trong thì..."
    mei_inner "Bên trong thì mình đang... Rơi."

    scene_desc "Mei đi dọc hành lang. Bước chân nặng nề hơn bình thường."

    mei_inner "Vy biết điểm mình rồi."
    mei_inner "Vy — đứa con gái bình thường nhất trường — biết rằng Mai Trần cũng chỉ... bình thường."
    mei_inner "Câu hỏi là: Nó sẽ làm gì với thông tin đó?"

    ## CHOICE: What does Mei expect?
    menu:
        mei_inner "Nó sẽ..."

        "Nói cho cả lớp — chắc chắn rồi, đứa nào mà không khoe":
            $ facade += 3
            $ vy_relationship -= 10
            $ empathy -= 3
            mei_inner "Nó sẽ kể cho mọi người. 'Tui biết nè, Mai Trần chỉ 5 điểm thôi!'"
            mei_inner "Rồi cả lớp sẽ cười. Mẹ sẽ biết. Thầy cô sẽ biết."
            mei_inner "Và mình... Sẽ không còn gì."
            mei_inner "Nên mình phải hành động trước."
            mei_inner "Phải tìm cách bịt miệng nó. Hay ít nhất... Khiến không ai tin nó."

        "Có thể nó sẽ quên. Nó vốn chẳng quan tâm ai":
            $ facade -= 2
            mei_inner "Vy... Nó có quan tâm chuyện người khác đâu."
            mei_inner "4 điểm hàng ngày mà nó cũng chẳng buồn lo."
            mei_inner "Thì chuyện mình điểm mấy, nó cũng kệ thôi..."
            mei_inner "... Phải không?"
            mei_inner "Mình đang tự trấn an. Và mình biết điều đó."

        "Không biết. Nhưng nếu nó tử tế... Sao?":
            $ empathy += 5
            $ vy_relationship += 5
            mei_inner "Nếu... Nếu Vy không nói cho ai?"
            mei_inner "Nếu nó chỉ... Biết, và giữ cho mình?"
            mei_inner "Mình nghĩ có ai sẽ làm vậy? Thật sao?"
            mei_inner "... Mình không biết."
            mei_inner "Mình không quen với sự tử tế không điều kiện."
            mei_inner "Nhưng cái nhìn của Vy lúc nãy..."
            mei_inner "Nó không phải thương hại. Nó giống..."
            mei_inner "Giống như: 'Mình hiểu.'"

    ## --------------------------------------------------------
    ## PART 7: MÁY ẢNH SỰ THẬT — CONNECTING THE DOTS
    ## --------------------------------------------------------

    scene_desc "Mei đi dọc sân trường, suy nghĩ miên man."

    mei_inner "Quay lại chuyện cái máy ảnh."
    mei_inner "Vy chĩa cái máy ảnh vào đề bài... Rồi bỗng nhiên biết hết đáp án?"
    mei_inner "'Máy Ảnh Sự Thật' — con mèo máy nói vậy."
    mei_inner "Nó chụp vật thể... Và biết được bản chất?"
    mei_inner "Vậy nó có chụp... Con người không?"
    mei_inner "Nó có chụp..."

    mei_inner "MÌNH?"

    mei_inner "Không. Vy không chụp mình."
    mei_inner "... Phải không?"
    mei_inner "Nếu nó chụp mình... Nó sẽ thấy gì?"

    ## CHOICE: What would the camera see?
    menu:
        mei_inner "Nếu cái máy ảnh đó chụp Mai Trần... Nó sẽ thấy..."

        "Bản chất thật: Một con alien cô đơn, mệt mỏi, sợ hãi":
            $ self_worth += 5
            $ facade -= 5
            mei_inner "Nó sẽ thấy... Maitopia."
            mei_inner "Một hành tinh cô đơn. Với một cư dân duy nhất."
            mei_inner "Đang ngồi giữa đống clone accounts, mì tôm 2 giờ sáng, và meme trầm cảm."
            mei_inner "Có đáng sợ không? Không."
            mei_inner "Có đáng thương không? ... Hơi."
            mei_inner "Nhưng ít nhất... Đó là thật."

        "Hư vô. Không có gì. Vì mình không có 'bản chất'":
            $ self_worth -= 5
            $ facade += 3
            mei_inner "Nó sẽ thấy... Không gì cả."
            mei_inner "Vì sau cái mặt nạ... Không có gì."
            mei_inner "Mình đeo mặt nạ quá lâu. Quá nhiều lớp."
            mei_inner "Đến mức... Mình cũng không biết bên dưới còn gì."
            mei_inner "Có khi... Không còn gì thật."

        "Ai biết? Mình cũng muốn biết lắm":
            $ empathy += 3
            mei_inner "Honestly? Mình cũng muốn biết."
            mei_inner "Mình đã tự hỏi câu 'mình thật sự là ai' quá nhiều lần."
            mei_inner "Mà không bao giờ trả lời được."
            mei_inner "Có khi... Mình cần ai đó chụp mình bằng cái máy ảnh đó."
            mei_inner "Để lần đầu tiên... Nhìn thấy bản thân mình."

    ## --------------------------------------------------------
    ## PART 8: CLOSING — THE CRACK WIDENS
    ## --------------------------------------------------------

    scene black with fade
    ## [BG: bg street_evening — Street, dusk]
    scene_desc "Đường về nhà. Nắng tắt dần. Bầu trời chuyển từ cam sang tím."

    mei_inner "Hôm nay..."
    mei_inner "Lần đầu tiên từ khi mình nhớ..."
    mei_inner "Có gì đó... Nứt."
    mei_inner "Cái pháo đài mình xây, cái mặt nạ mình đeo, cái kịch bản mình diễn..."
    mei_inner "Có một vết nứt nhỏ xíu."

    pause 0.5

    mei_inner "Và mình không biết..."
    mei_inner "Nên sợ... Hay nên nhẹ nhõm."

    pause 0.5

    mei_inner "Vì từ vết nứt đó... Ánh sáng rọi vào."
    mei_inner "Và mình nhìn thấy bên trong..."
    mei_inner "Vẫn có gì đó ở đây."
    mei_inner "Vẫn có ai đó."

    pause 1.0

    mei_inner "... Chưa biết là ai."
    mei_inner "Nhưng cô ấy vẫn ở đây."

    jump chapter3_end
