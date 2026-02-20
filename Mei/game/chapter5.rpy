## chapter5.rpy — Chương 5: Kết Nối (Connections)
## ============================================================
## Original Script Scene 5 from Mai's POV.
## Hương's love confession, Mai witnessing Vy help others,
## questioning her own walls.
## ============================================================

label chapter5_start:

    ## --------------------------------------------------------
    ## PART 1: SÁNG — MỘT NGÀY NHẸ HƠN?
    ## --------------------------------------------------------

    ## [BG: bg school_hallway — Morning hallway]
    scene_desc "Buổi sáng. Hành lang. Ánh nắng qua cửa kính."

    mei_inner "Hôm nay... Lạ."
    mei_inner "Mình vẫn đeo mặt nạ. Vẫn cười. Vẫn chào."
    mei_inner "Nhưng nó nhẹ hơn. Hơi hơi."
    mei_inner "Như thể cái mặt nạ... Mỏng đi một chút."

    scene_desc "Mei đi dọc hành lang. Nhìn xung quanh — học sinh cười đùa, chạy nhảy."

    mei_inner "Mọi người có vẻ... Bình thường."
    mei_inner "Hay mình bắt đầu nhìn họ... Khác?"

    scene_desc "Vy đi ngang qua, tai nghe cắm, mặt ngái ngủ. Gật đầu nhẹ khi thấy Mei."

    mei_inner "... Lại gật."
    mei_inner "Con bé này giao tiếp bằng đầu."
    mei_inner "Nhưng cái gật đó... Honest hơn nghìn lời chào hỏi xã giao."

    ## --------------------------------------------------------
    ## PART 2: THÀNH — BÓNG NGƯỜI KỲ LẠ
    ## --------------------------------------------------------

    scene_desc "Giờ ra chơi. Mei đi dạo sân trường — giờ đây đã thành thói quen."

    mei_inner "Từ hôm gặp Pi... Mình bắt đầu đi dạo nhiều hơn."
    mei_inner "Ngồi trong lớp thì phải diễn. Ra ngoài thì... Ít nhất có gió."

    scene_desc "Mei đi ngang qua một thằng con trai — Thành. Mặt hơi căng. Đi ngược hướng."

    mei_inner "Thành... Lớp bên cạnh. Yên lặng. Kiểu... Yên lặng thật, không phải giả vờ."
    mei_inner "Mặt nó hôm nay căng hơn bình thường."

    scene_desc "Thành đi qua, không nhìn ai. Vai xệ. Tay thọc túi."

    mei_inner "Next time: Tìm hiểu. Nhưng giờ... Đi tiếp."

    ## --------------------------------------------------------
    ## PART 3: HƯƠNG — NƯỚC MẮT VÀ BỤI
    ## --------------------------------------------------------

    ## [BG: bg school_bench — School bench area, secluded]
    scene_desc "Góc sân trường. Một cô gái đang ngồi ôm mặt."

    mei_inner "..."
    mei_inner "Lại? Sao trường này toàn người khóc vậy?"
    mei_inner "Trước Pi, giờ tới... Ai vậy?"

    scene_desc "Mei nhìn kỹ hơn. Tóc dài, áo trắng. Đó là Hương — ngồi bên cạnh Mai trong lớp cũ."

    mei_inner "Hương... Mình biết nó. Học cùng năm trước."
    mei_inner "Hiền. Tử tế. Kiểu con gái mà ai cũng quên tên."
    mei_inner "Và nó đang... Khóc."

    ## CHOICE: Approach or leave?
    menu:
        mei_inner "..."

        "Đi lại — lần trước mình đã không bước ra với Pi, lần này...":
            $ empathy += 5
            $ facade -= 5
            $ huong_bond += 10
            mei_inner "Okay. Mình sẽ thử."
            mei_inner "Không biết nói gì. Nhưng ít nhất... Đi lại."
            scene_desc "Mei ngồi xuống cạnh Hương. Nhẹ nhàng."
            mei "... Hey."
            huong "*dụi mắt* Hả? M-Mai?"
            huong "Tui ổn! Chỉ là... Bụi vào mắt thôi."
            mei_inner "'Bụi vào mắt.' Kinh điển."
            mei_inner "Mình dùng câu đó ít nhất 247 lần rồi."

        "Đi ngang qua — mình không giỏi mấy chuyện comfort":
            $ facade += 2
            $ empathy -= 2
            mei_inner "Mình không biết comfort. Mình chỉ biết script."
            mei_inner "Và không có script nào cho tình huống 'bạn học khóc ở góc sân trường.'"
            scene_desc "Mei đi qua. Nhưng... Quay lại nhìn."
            scene_desc "Hương vẫn khóc. Vai run."
            mei_inner "..."
            mei_inner "Sh*t."
            mei_inner "Mình vừa nhớ cả đống đêm mình khóc một mình."
            mei_inner "Không ai đi lại. Không ai hỏi."
            scene_desc "Mei dừng lại. Thở dài. Quay lại."
            mei "... Ê."
            huong "??"
            $ huong_bond += 5

        "Quan sát từ xa — xem có ai giúp không":
            $ empathy += 1
            mei_inner "Mình sẽ... Đứng đây. Xem tình hình."
            mei_inner "Nếu không ai đi lại... Thì..."
            scene_desc "Mei đứng xa. Nhìn. Đợi."
            scene_desc "1 phút. 2 phút. 5 phút."
            scene_desc "Không ai dừng lại. Ai cũng đi ngang, nhìn, rồi đi tiếp."
            mei_inner "... Không ai."
            mei_inner "Cũng giống mình. Khóc mà không ai thấy."
            scene_desc "Mei thở dài, rồi đi lại."
            mei "... Có sao không?"
            huong "*ngẩng lên*"
            $ huong_bond += 3

    ## The conversation — Hương's story
    scene_desc "Mei ngồi cạnh Hương. Đưa khăn giấy."

    mei_inner "Mình có khăn giấy vì mình luôn chuẩn bị mọi thứ."
    mei_inner "Perfectionist có lợi thế: Luôn có khăn giấy trong cặp."

    huong "*nhận khăn* Cám ơn..."
    mei "..."

    mei_inner "Nói gì đây? Mình không giỏi chuyện này."
    mei_inner "Khi ai khóc trước mặt mình, não mình crash như Windows XP."

    ## CHOICE: How to ask?
    menu:
        "Trực tiếp — \"Chuyện gì?\"":
            $ facade -= 2
            mei "Chuyện gì vậy?"
            huong "... Không có gì—"
            mei "Bụi vào mắt ở một góc kín gió? Không ai tin đâu."
            huong "*bật cười nhẹ qua nước mắt*"
            mei_inner "... Ơ. Nó cười?"
            mei_inner "Mình vừa... Làm ai đó cười?"
            mei_inner "Bằng sự thẳng thắn, không phải bằng script?"

        "Nhẹ nhàng — \"Mình ngồi đây được không?\"":
            $ empathy += 3
            mei "Mình ngồi đây tí nha. Kệ mình."
            huong "..."
            scene_desc "Im lặng. Nhưng dần dần, vai Hương thả lỏng."
            mei_inner "Đôi khi... Người ta chỉ cần ai đó ngồi cạnh."
            mei_inner "Mình biết. Vì mình ước mỗi đêm ai đó ngồi cạnh mình."

        "Đùa — \"Ê, nếu đang giấu xác ai thì cho tui biết, tui giúp\"":
            $ facade -= 3
            $ empathy += 2
            mei "Ê. Nếu mày đang giấu xác ai thì nói tao, tao giúp phi tang."
            huong "...HẢ?!"
            mei "Đùa. *mỉm cười*"
            huong "*bật cười qua nước mắt* Trời ơi, ai đùa vậy lúc này..."
            mei_inner "Mình vừa... Đùa kiểu clone account."
            mei_inner "Kiểu đùa đen mà mình chỉ dám đùa trên acc meme."
            mei_inner "Vậy mà... Nó cười?"
            mei_inner "... Thú vị."

    ## Hương opens up
    huong "*dần bình tĩnh* Tao... Có một đứa bạn thân. Là con trai."
    mei "Ừ."
    huong "Tụi tao quen biết 6 năm rồi. Quan hệ cũng bình thường, hầu như không có xích mích."
    mei_inner "6 năm. Đó là lâu. Lâu hơn bất kỳ mối quan hệ nào mình có."
    huong "Nhưng dạo này... Có vài thứ không ổn xảy ra..."
    mei "Chuyện gì?"
    huong "*lúng túng* Rằng t vừa nhận ra rằng... Hmm..."

    ## CHOICE: Mei's guess
    menu:
        mei_inner "Mình đoán..."

        "\"Mày thích nó.\" — Nói thẳng":
            $ facade -= 5
            $ empathy += 5
            mei "Mày thích nó."
            huong "...!!!"
            huong "Sao... Sao mày biết?!"
            mei "Vì mày đỏ mặt khi nói về nó. Và mày gọi nó là 'bạn thân' với giọng run."
            mei_inner "Mình không phải người hiểu tình cảm."
            mei_inner "Nhưng mình hiểu mặt nạ. Và mặt nạ của Hương... Dễ đọc."
            huong "... Ừ. Tui thích nó mất rồi."
            mei_inner "Nó thú nhận."
            mei_inner "Dễ vậy sao? Tại sao mình không dám thú nhận bất cứ điều gì?"

        "Chờ nó tự nói — mình không giỏi đoán":
            $ empathy += 2
            mei "..."
            scene_desc "Mei đợi. Im lặng."
            huong "*trầm ngâm* T nhận ra... T thích nó mất rồi."
            mei "Oh."
            mei_inner "Oh."
            mei_inner "Crush bạn thân. Classic."

        "\"Bạn mày là chủ tịch giả dạng?\" — Đùa lại":
            $ facade -= 3
            $ empathy += 3
            mei "Bạn mày là chủ tịch giả dạng? Hay người ngoài hành tinh?"
            huong "*bật cười* Đéooo! Là... T thích nó mất rồi."
            mei "*gật đầu* Biết mà."
            mei_inner "Mình biết."
            mei_inner "Mình chỉ muốn nó cười trước khi thú nhận thôi."

    ## Hương's dilemma
    huong "Giờ không biết làm gì nữa. Đành tạm cắt đứt quan hệ với nó vậy."
    huong "Nhưng mà do làm vậy nên nó giận t rồi. Đến sinh nhật t còn quên nữa."

    mei_inner "..."
    mei_inner "Cắt đứt quan hệ vì sợ..."
    mei_inner "Giống mình."
    mei_inner "Mình cắt đứt bản thân thật khỏi thế giới, vì sợ bị từ chối."
    mei_inner "Hương cắt đứt tình bạn, vì sợ mất nó."
    mei_inner "Cả hai đều... Phá hủy thứ mình yêu để bảo vệ nó."
    mei_inner "Self-sabotage."
    mei_inner "Mình biết tên cái pattern này. Vì mình sống với nó mỗi ngày."

    ## CHOICE: Mai's advice
    menu:
        mei_inner "Mình nên nói gì?"

        "Nói thật — \"Trốn chạy không giải quyết được gì\"":
            $ facade -= 8
            $ empathy += 8
            $ self_worth += 5
            $ huong_bond += 15
            $ helped_huong = True
            mei "Hương."
            huong "?"
            mei "Mày đang làm đúng điều mà mình làm mỗi ngày."
            huong "Hả?"
            mei "Trốn. Giấu. Chạy. Vì sợ."
            mei "Mày sợ nói thật vì nó có thể phá hỏng mọi thứ. Nhưng mày không thấy sao?"
            mei "Chính việc trốn chạy... Đang phá hỏng mọi thứ rồi."
            huong "..."
            mei "6 năm. 6 NĂM. Mày tưởng nó sẽ ghét mày vì mày thích nó?"
            mei "Nếu tình bạn 6 năm mà sụp vì một lời thú nhận... Thì nó đã sụp từ lâu rồi."
            mei_inner "*thở* Mình đang... Nói cho Hương, hay nói cho chính mình?"
            mei_inner "Vì mọi câu mình vừa nói... Đều apply cho mình."
            mei_inner "\"Trốn chạy không giải quyết được gì.\" Mình biết. Mình biết hơn ai hết."
            mei_inner "Nhưng biết và làm... Là hai thứ khác nhau."
            huong "... Mai."
            huong "Sao mày lại nói... Như thể mày hiểu?"
            mei "*cười buồn* Vì... Mình cũng đang trốn chạy. Chỉ là giỏi hơn mày thôi."

        "Thúc giục — \"Đi nói với nó đi!\"":
            $ empathy += 5
            $ huong_bond += 10
            $ helped_huong = True
            mei "Thôi! Đi nói với nó!"
            huong "Gì?! Bây giờ?!"
            mei "Ừ! Bây giờ! Chờ tới khi nào? Khi nó có người yêu? Khi tụi mày 60 tuổi?"
            huong "Nhưng—"
            mei "Không nhưng! Go! Now!"
            mei_inner "... Mình đang nghe giống Vy."
            mei_inner "Trùa ơi. Mình đang trở thành Vy."
            mei_inner "... Mà có sao đâu."

        "Im lặng, đưa khăn giấy — mình không đủ tư cách cho lời khuyên":
            $ facade += 2
            $ empathy += 2
            mei "..."
            scene_desc "Mei đưa thêm khăn giấy."
            mei "Mình... Không giỏi cho lời khuyên."
            mei "Vì mình cũng chẳng biết giải quyết vấn đề của mình."
            mei "Nhưng... Mình nghe xong rồi. Và mình nghĩ... Mày biết nên làm gì."
            huong "..."
            huong "... T biết. T chỉ sợ."
            mei "Sợ thì cứ sợ. Nhưng sợ mà vẫn làm... Đó mới là dũng cảm."
            mei_inner "Ai nói câu đó? Mình? Hay cái phần nào đó sâu trong mình mà mình luôn giấu?"

    ## --------------------------------------------------------
    ## PART 4: HƯƠNG GẶP THÀNH — THE CONFESSION
    ## --------------------------------------------------------

    ## [BG: bg school_yard — School yard, afternoon]
    scene_desc "Thành đang ngồi một mình phía sân sau. Ném đá về nơi xa xăm."

    scene_desc "Hương đứng cạnh Mei, run."

    mei "Bạn mày kìa."
    huong "*gật đầu, nuốt nước bọt*"
    mei "Go."
    huong "T... T can't do this..."

    ## CHOICE: How Mei pushes Hương
    menu:
        "Nhẹ nhàng — nắm tay Hương":
            $ empathy += 5
            $ facade -= 5
            scene_desc "Mei nắm tay Hương. Nhẹ nhưng chắc."
            mei "Mày run quá. *nắm chặt hơn* Nhưng mày không đi một mình."
            mei "Tui ở đây."
            huong "*nhìn Mei, mắt đỏ*"
            mei "Hít thở. Hít... Thở..."
            scene_desc "Hương hít thở. Tay bớt run."
            mei "Okay. Giờ đi. Tui đứng đây chờ."
            mei_inner "... Mình vừa nắm tay ai đó."
            mei_inner "Mình vừa chạm vào ai đó với mục đích duy nhất là... Cho họ dũng cảm."
            mei_inner "Cảm giác... Ấm."

        "Thẳng thắn — đẩy nhẹ ra":
            $ empathy += 3
            $ facade -= 3
            mei "Một lần này hoặc không bao giờ. Đi đi."
            scene_desc "Mei đẩy nhẹ vai Hương về phía Thành."
            mei "Now go get it, lil tiger."
            huong "...!"
            mei_inner "Mình vừa gọi ai đó 'lil tiger'??"
            mei_inner "Oh god. Mình thật sự đang biến thành Vy."
            mei_inner "... Nhưng mà... Vy cũng không tệ."

        "Logic — \"Tính xác suất đi: nó đã biết mày 6 năm, xác suất ghét mày thấp lắm\"":
            $ facade += 2
            $ empathy += 3
            mei "Okay nghe này. Tính logic."
            mei "Bạn 6 năm. Xác suất nó ghét mày vì mày thú nhận: thấp."
            mei "Xác suất nó giận mãi vì mày cắt liên lạc: cao hơn."
            mei "Xác suất mày hối hận nếu không nói: 100%."
            mei "Conclusion?"
            huong "... Đi?"
            mei "Đi."
            mei_inner "Mình dùng logic cho tình cảm. Peak Alien behavior."
            mei_inner "Nhưng nó hiệu quả."

    ## Hương walks toward Thành — Mei watches
    scene_desc "Hương đi ra. Từng bước. Chậm. Nhưng tiến về phía trước."

    scene_desc "Mei đứng lại, nhìn theo."

    mei_inner "Đi đi. Đi đi."
    mei_inner "Mày làm được. Tao tin mày."
    mei_inner "..."
    mei_inner "Đợi. Tao vừa 'tin' ai đó?"
    mei_inner "Mai Trần, kẻ không tin ai, vừa tin một đứa con gái mình mới nói chuyện 10 phút."

    ## The confession scene — from afar
    scene_desc "Hương dừng trước Thành."

    huong "Hi..."
    thanh "*nhìn, im*"
    huong "Ghét t rồi hả...?"

    scene_desc "Im lặng dài."
    scene_desc "Rồi Thành... Đứng dậy."

    thanh "... 3 tuần. Mày biến mất 3 tuần."
    thanh "T tưởng t làm gì sai."

    huong "Không! Không phải—"
    huong "Chỉ là... T..."
    huong "T thích m."

    scene_desc "Im lặng. Gió thổi."

    thanh "..."
    thanh "... Vậy thôi hả?"
    huong "Hả?"
    thanh "T tưởng chuyện gì lớn lắm. Mày biến mất 3 tuần vì... Thích t?"
    huong "... Ừ."
    thanh "... Ngốc."

    scene_desc "Thành mỉm cười. Nhẹ. Nhưng... Ấm."

    mei_inner "..."
    mei_inner "Nó cười."
    mei_inner "Thành cười."
    mei_inner "Và Hương đang khóc. Nhưng lần này... Khóc vui."

    scene_desc "Từ xa, Mei đứng nhìn hai bóng người — một đang gạt nước mắt, một đang chìa tay ra."

    mei_inner "... Vậy thôi hả."
    mei_inner "Thú nhận. Và được chấp nhận."
    mei_inner "Đơn giản vậy."
    mei_inner "Sao mình làm không được?"

    ## --------------------------------------------------------
    ## PART 5: VY XUẤT HIỆN — THE PARALLEL
    ## --------------------------------------------------------

    scene_desc "Từ phía hành lang — Vy xuất hiện. Cũng đang đi về hướng Hương."
    scene_desc "Vy nhìn thấy cảnh Hương và Thành. Cười."
    scene_desc "Rồi Vy nhìn sang — thấy Mei đứng xa xa, cũng đang nhìn."

    scene_desc "Ánh mắt hai người gặp nhau."

    mei_inner "... Vy."
    mei_inner "Nó cũng tới đây? Nó cũng định giúp Hương?"

    scene_desc "Vy gật đầu nhẹ. Như thể nói: 'Mày đã giúp nó rồi hả.'"

    mei_inner "..."
    mei_inner "Nó biết. Nó biết mình giúp Hương."
    mei_inner "Và nó... Gật đầu."
    mei_inner "Không ngạc nhiên. Không khinh thường."
    mei_inner "Chỉ gật. Như thể nó tin mình làm được."

    ## CHOICE: Mei's response to Vy
    menu:
        "Gật đầu lại — nhỏ thôi, nhưng thật":
            $ vy_relationship += 15
            $ facade -= 5
            $ empathy += 5
            scene_desc "Mei gật đầu. Nhẹ."
            mei_inner "Một cái gật."
            mei_inner "Giữa hai người không nói chuyện bao giờ."
            mei_inner "Nhưng trong khoảnh khắc đó..."
            mei_inner "Mình hiểu nó. Và nó hiểu mình."
            mei_inner "Không cần máy ảnh sự thật."
            mei_inner "Chỉ cần... Nhìn."

        "Quay đi — mình không quen được ai đó 'hiểu' mình":
            $ facade += 5
            $ empathy -= 2
            scene_desc "Mei quay mặt đi. Đi nhanh."
            mei_inner "Không. Cái nhìn đó quá nhiều."
            mei_inner "Mình không quen ai đó nhìn mình mà không phán xét."
            mei_inner "Sợ. Sợ vì... Nếu ai đó hiểu mình..."
            mei_inner "Thì mình sẽ phải thừa nhận rằng mình cần người khác."
            mei_inner "Và mình đã nói cả đời rằng mình không cần ai."

        "Mỉm cười — lần đầu tiên, không phải script":
            $ vy_relationship += 20
            $ facade -= 8
            $ empathy += 8
            $ self_worth += 5
            scene_desc "Mei mỉm cười. Nhẹ. Mắt hơi ướt."
            mei_inner "Mình đang cười."
            mei_inner "Và lần này... Không phải script."
            mei_inner "Không phải 'nụ cười hoàn hảo số 14'."
            mei_inner "Mà là... Mình."
            mei_inner "Ugly. Không đều. Hơi méo."
            mei_inner "Nhưng thật."
            scene_desc "Vy nhìn nụ cười đó. Và cũng cười. Kiểu cười ngốc ngốc, miệng hơi rộng."
            mei_inner "... Nụ cười hai đứa xấu vcl."
            mei_inner "Nhưng đẹp nhất mình từng thấy."

    ## --------------------------------------------------------
    ## PART 6: ĐÊM — ALONE BUT DIFFERENT
    ## --------------------------------------------------------

    scene black with fade
    ## [BG: bg mei_room_night — Room, night]
    scene_desc "Đêm. Phòng Mei. Ánh đèn bàn quen thuộc."

    mei_inner "Hôm nay..."
    mei_inner "Mình giúp ai đó."
    mei_inner "Thật sự giúp. Không phải vì script. Không phải vì hình ảnh."
    mei_inner "Mà vì... Mình muốn."

    scene_desc "Mei ngồi trước laptop. 9 tab clone vẫn mở."

    mei_inner "Maitopia."
    mei_inner "Hành tinh của mình."
    mei_inner "Nơi mình trốn. Nơi mình an toàn."

    ## CHOICE: Tonight's activity
    menu:
        mei_inner "Tối nay..."

        "Mở acc vent — nhưng lần này viết gì đó tích cực":
            $ self_worth += 5
            $ facade -= 3
            scene_desc "Tab 2: @______void______."
            scene_desc "Mei gõ:"
            scene_desc "'1:12am — hôm nay mình cười. thật. không biết lần cuối cười thật là khi nào.'"
            scene_desc "'có ai đó nhìn mình. thật sự nhìn. và mình không sợ.'"
            scene_desc "'chắc alien cũng biết cười.'"
            mei_inner "Lần đầu tiên... Acc vent có status không buồn."
            mei_inner "Lần đầu tiên... Mình viết cho hư vô mà... Tự hư vô cũng bỡ ngỡ."

        "Đóng laptop — tối nay muốn nghĩ, không muốn cuộn":
            $ self_worth += 3
            $ facade -= 5
            scene_desc "Mei đóng laptop. Phòng tối."
            scene_desc "Nằm trên giường, nhìn trần nhà."
            mei_inner "Hôm nay mình không cần clone."
            mei_inner "Hôm nay mình... Đủ."
            mei_inner "Không biết 'đủ' là gì. Nhưng nó nhẹ. Nhẹ lắm."
            mei_inner "Good night."
            mei_inner "Good night, Maitopia."
            mei_inner "Hôm nay cư dân Maitopia... Không cô đơn."

        "Lướt như bình thường — một ngày tốt không thay đổi gì đâu":
            $ facade += 3
            mei_inner "Don't get your hopes up."
            mei_inner "Hôm nay tốt. Ngày mai sẽ lại bình thường."
            mei_inner "Mình biết pattern này. Một ngày tốt → Hy vọng → Thất vọng → Tổn thương hơn."
            mei_inner "Nên thà đừng hy vọng."
            scene_desc "Mei cuộn feed. Meme. Creepypasta. Like. Share. Save."
            mei_inner "Loop. Safe. Predictable."
            mei_inner "... Nhưng sao hôm nay cuộn mà không vui?"

    ## TRANSITION
    scene black with fade
    pause 0.5

    mei_inner "Dù sao thì..."
    mei_inner "Hôm nay mình học được một thứ."
    mei_inner "Rằng nói thật... Không phải lúc nào cũng dẫn tới thảm họa."
    mei_inner "Đôi khi nó dẫn tới... Một nụ cười."
    mei_inner "Và đôi khi... Một cái gật đầu."

    pause 0.5

    mei_inner "Nhưng mình vẫn chưa biết..."
    mei_inner "Nếu mình thú nhận bản thân thật..."
    mei_inner "Ai sẽ gật đầu với mình?"

    jump chapter5_end
